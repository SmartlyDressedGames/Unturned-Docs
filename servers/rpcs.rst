.. _doc_servers_rpcs:

NetMethods and NetIds
=====================

NetMethods
----------

**NetMethods** are remote procedure (RPCs) used to communicate between the server and clients. A NetMethod can come in the form of either **static**, calling a static method, or **instance**, calling a method on specific object identified by a **NetId**. These have various use cases in :ref:`modules <doc_servers_modules>` ran on both the server and client.

In most typical use cases, a NetMethod is a method with the ``SteamCall`` attribute. These are then paired with a static handle used to invoke it remotely. The vanilla naming convention on these is prefixing this method with ``Receive`` and its handle with ``Send``.

The following are the four handle types, each have different call directions and designation of either static or instance:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Handle
     - Direction
     - Receive Method
   * - ``ClientStaticMethod``
     - Server to client
     - Static method. No NetId is sent.
   * - ``ClientInstanceMethod``
     - Server to client
     - Instance method on the object paired with the given NetId.
   * - ``ServerStaticMethod``
     - Client to server
     - Static method. No NetId is sent.
   * - ``ServerInstanceMethod``
     - Client to server
     - Instance method on the object paired with the given NetId.

These handles also have generic versions for methods that have parameters. For example, ``ClientStaticMethod<string>`` invokes a static client method with one ``string`` parameter passed in.

There also exists read and write methods for the networking data of each NetMethod. These are :ref:`Generated Methods <doc_servers_rpcs:generated_methods>` and will have to be generated or manually created.

.. note:: The server and client must have identical method lists. Creating these in an environment of various modules / modifications will require synchronization. Therefore, serverside plugins aren't capable of adding new RPCs.

Static Methods
``````````````

Static NetMethods are used for anything that isn't tied to an instance object, such as chat messages. When received, the game will call the static receiving method directly when read.

The following snippet from ``EffectManager`` is a good example of static methods being used for both directions of communication:

.. code-block:: cs

	// Server to client. Modifies the text of an element within a UI effect.
	private static readonly ClientStaticMethod<short, string, string> SendUIEffectText = ClientStaticMethod<short, string, string>.Get(ReceiveUIEffectText);

	[SteamCall(ESteamCallValidation.ONLY_FROM_SERVER, legacyName = nameof(tellUIEffectText))]
	public static void ReceiveUIEffectText(short key, string childNameOrPath, string text)
	{
		// ...
	}

	// Client to server. Notifies the server that a button in a UI effect was clicked.
	private static readonly ServerStaticMethod<string> SendEffectClicked = ServerStaticMethod<string>.Get(ReceiveEffectClicked);

	[SteamCall(ESteamCallValidation.SERVERSIDE, ratelimitHz = 20, legacyName = nameof(tellEffectClicked))]
	public static void ReceiveEffectClicked(in ServerInvocationContext context, string buttonName)
	{
		Player player = context.GetPlayer();
		if (player == null)
			return;

        // Invoke the event on the server to alert any listening plugins.
		onEffectButtonClicked?.Invoke(player, buttonName);
	}

Instance Methods
````````````````

Instance NetMethods call a method on one specific object. When received, the generated ``_Read`` method reads the NetId, finds the object paired with it, and called the receive method on that object. The call is ignored if no pairing is found, or if the object type is unexpected.

Because the receive method is not static, the handle is created from the type and method name instead. The following snippet from ``InteractableFarm`` is a good example of instance methods being used for both directions of communication:

.. code-block:: cs

	// Server to client. Updates when this crop was planted.
	internal static readonly ClientInstanceMethod<uint> SendPlanted = ClientInstanceMethod<uint>.Get(typeof(InteractableFarm), nameof(ReceivePlanted));

	[SteamCall(ESteamCallValidation.ONLY_FROM_SERVER, deferMode = ENetInvocationDeferMode.Queue)]
	public void ReceivePlanted(uint newPlanted)
	{
		updatePlanted(newPlanted);
	}

	// Client to server. Requests to harvest this crop.
	private static readonly ServerInstanceMethod SendHarvestRequest = ServerInstanceMethod.Get(typeof(InteractableFarm), nameof(ReceiveHarvestRequest));

    // Invokes the static handle to trigger the harvest request.
	public void ClientHarvest()
	{
		SendHarvestRequest.Invoke(GetNetId(), ENetReliability.Unreliable);
	}

	[SteamCall(ESteamCallValidation.SERVERSIDE, ratelimitHz = 10)]
	public void ReceiveHarvestRequest(in ServerInvocationContext context)
	{
		// ...
	}

Reading and Writing Parameters
------------------------------

How a NetMethod's data is read and written depends on the receive method's parameters.

Generated Parameters
````````````````````

If the receive method has basic parameters, like ``ReceiveUIEffectText(short key, string childNameOrPath, string text)``, the NetMethod is read and written by generated code. The handle's type arguments have to match the parameters, and the parameter values are passed in directly on invocation.

.. code-block:: cs

	SendUIEffectText.Invoke(reliability, transportConnection, key, childNameOrPath, text);

The receive method can also take an invocation context  (``in ClientInvocationContext`` or ``in ServerInvocationContext``) as the first parameter. The generated ``_Read`` method passes it along. Server methods commonly use this to find the calling player, such as ``ReceiveEffectClicked`` above.

Manual Parameters
`````````````````

If the receive method *only* has a parameter that is the invocation context, no code will be generated for its parameters. Instead, the receive method is made responsible for reading its own data from ``context.reader``, and the sender is resposible for writing it. This is typically used for data that the generator can't handle, such as large batches of objects (e.g. barricade or structure regions).

For instance methods, a ``_Read`` method will still be generated. This method still reads the NetId and find the object it points to. It then calls the receive method, which reads the rest of the data.

.. code-block:: cs

	private static readonly ClientInstanceMethod SendScreenshotDestination = ClientInstanceMethod.Get(typeof(Player), nameof(ReceiveScreenshotDestination));

	// Writes the data using a callback.
	SendScreenshotDestination.Invoke(GetNetId(), ENetReliability.Reliable, transportConnection, SendScreenshotDestination_Write, length, data);

	private void SendScreenshotDestination_Write(NetPakWriter writer, ushort length, byte[] data)
	{
		writer.WriteUInt16(length);
		writer.WriteBytes(data);
	}

	// Reads the data in the same order.
	[SteamCall(ESteamCallValidation.ONLY_FROM_SERVER)]
	public void ReceiveScreenshotDestination(in ClientInvocationContext context)
	{
		NetPakReader reader = context.reader;
		ushort length;
		reader.ReadUInt16(out length);
		byte[] data = new byte[length];
		reader.ReadBytes(data);
		HandleScreenshotData(data);
	}

.. note:: As with most networking data, data must be read in the same order and format that it was written in. Mismatches may cause silent errors.

NetIds
------

A ``NetId`` is a struct that wraps a 32-bit unsigned integer (``uint``). The ``NetIdRegistry`` class pairs each NetId with an object (e.g. ``InteractableFarm`` or ``Player``) or specifically a ``Transform``. This is then used to allow the server and client to agree on which object an instance NetMethod should call its receive method on. A NetId of ``0`` represents an invalid identifier.

For example, there could be many farm crops around the map. When a client attempts to harvest one, it sends that crop's NetId over so the server knows which specific ``InteractableFarm`` it was for.

NetIds are assigned by either the server or calculated from the level. For the server, it claims a block of NetIds for each new barricade, structure, vehicle, or player. For the level, trees and objects calculate their NetIds based on their level data position, so they don't need to be sent over the network.

The registry is cleared before a level is loaded. NetIds are considered volatile and should not be saved or reused between sessions / restarts.

.. tip:: Most objects that have an assigned NetId such as ``Player``, ``SteamPlayer``, ``BarricadeDrop``, ``StructureDrop``, and ``Interactable`` have a ``GetNetId()`` method. You can use ``NetIdRegistry.Get<T>(netId)`` to find the object paired with a NetId.

SteamCall Attribute
-------------------

Required for receive methods of any NetMethod.

**validation** *ESteamCallValidation* (``ONLY_FROM_SERVER``, ``SERVERSIDE``, ``ONLY_FROM_OWNER``): Determines who is allowed to invoke the method.

**ratelimitHz** *int32*: Maximum number of calls per second for each player. Players that repeatedly exceed the limit may be kicked.

**deferMode** *ENetInvocationDeferMode* (``Queue``, ``Discard``): Determines the method behaviour when a client receives an instance method for a NetId that is not registered yet. This may be the case for objects that are pending instantiation. ``Queue`` holds the call until the object exists. ``Discard`` will ignore it.

**legacyName** *string*: Older name for the method. This has been kept for backwards compatibility with plugins that invoked RPCs by name. Usage is deprecated.

.. _doc_servers_rpcs:generated_methods:

Generated Methods
-----------------

NetMethods require methods for reading and writing networking data. These are automatically generated for the game and are contained within ``<Type>_NetMethods`` classes containing ``_Read`` and ``_Write`` methods. You can generate this code in Unity using the ``Window > Unturned > Net Gen`` menu.