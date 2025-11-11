.. _doc_server_hosting:

Setting up a Server
===================

Players can host their own multiplayer servers through the **Unturned Dedicated Server** tool. (This can be abbreviated as "**U3DS**".)

This tool is provided alongside Unturned but must be installed separately. It can be installed and ran from your Steam Library, or instead through :ref:`SteamCMD <doc_steamcmd>` for a much more advanced setup.

.. figure:: /img/U3DS_SteamLibrary.png

	Find the **Unturned Dedicated Server** app in your Steam Library.

Servers can be hosted on Windows and Linux operating systems. There is no support for hosting on macOS devices.

.. _doc_server_hosting:simple_setup:

Simple Setup
------------

This section provides a quick guide to creating your own server—perfect for hosting a *private* multiplayer world for just you and a few friends.

Port forwarding and other optional – *but useful* – features are not covered in this section. Consider reading more advanced setup instructions once your server is functional.

1. Launch the Unturned Dedicated Server app
```````````````````````````````````````````

Launch the **Unturned Dedicated Server** app from your Steam Library.

The Server Console will open in a new window. It may take a few minutes for your server to boot up while it generates any necessary files and loads your world data.

.. figure:: /img/U3DS_LoadingLevel.png

You should see "Loading level: 100%" when it finishes booting, along with a :ref:`Server Code <doc_servers_server_codes>`.

2. Invite your Friends
``````````````````````

You can invite players to your server through your Steam Friends List.

Players can also join your server by using the 17-digit **Server Code** created when you opened your server. This randomly-generated code will change each time you launch the server. It can found be clicking the "Copy Server Code" button while in your server, or by copying it from your Server Console.

.. hint::

	Players—including yourself—can join your server by inputting the server's **Server Code** in the **Connect Directly** menu. For friends, it's often quickest to just invite them through Steam!

By default, your server is not visible to others from the Multiplayer menu unless they are on the same LAN connection. Without following more advanced setup instructions, this *functionally* means that players can only join via your Steam Friends List or if you share the Server Code with them.

Save and Shutdown
-----------------

There is no built-in autosave feature. You must use the ``Save`` command to manually save your server while its still running, or the ``Shutdown`` command to safely save and close your server.

Savedata and configuration files can be found in the ``...\U3DS\Servers\`` directory. You will see a folder for each server you have created.

.. _doc_server_hosting:configuration:

Configure Server Settings
-------------------------

Configuration files can be found inside your server's server folder. Most settings cannot be configured while the server is open.

.. hint::

	If you created a server using the :ref:`Simple Setup <doc_server_hosting:simple_setup>` guide, you can find your server's settings from the ``...\U3DS\Servers\Default\`` directory.

Commonly-used configuration files are:

- | **\\Server\\Commands.dat** – Configure basic server settings, such as: Map, Password, and Max Players.

- | **\\Config.txt** – Adjust difficulty settings and advanced server settings, such as: increasing Item Spawn Chance or assigning a Game Server Login Token. (see :ref:`doc_servers_server_configuration`)

- | **\\WorkshopDownloadConfig.json** – Download mods from the Steam Workshop.

Commands
````````

Commands—sometimes referred to as console commands or cheat commands—range from tweaking server settings to spawning items. Most commands are set in the **Commands.dat** file, with each command separated by a newline.

Learn more about available commands on the `Unturned Wiki <https://unturned.wiki.gg/Commands>`_. Below is an example setup that includes many commonly-used commands:

.. code-block:: unturneddat

	// [[ SERVER CONFIGURATION ]]
	// Lines starting with "//" are comments – which aren't read when launching your server.
	// Read more about commands on the game's wiki: https://unturned.wiki.gg/Commands

	// Name of your server in the server list.
	Name My Unturned Server

	// Specify which map to load, by name.
	// Official maps include PEI, Washington, Yukon, Russia, and Germany.
	// Use the WorkshopDownloadConfig.json file to download Workshop maps.
	Map PEI

	// Maximum number of players that can be on the server.
	MaxPlayers 24

	// Assign a player's steamID64 as the "Owner" to give them administrator privileges, such as invoking cheat commands while in-game.
	// Owner YourSteamID

	// Enable "cheat commands" for administrators, such as spawning items or vehicles.
	Cheats

	// Require a password to join the server.
	// Password ExamplePassword1234

	// Disable player-versus-player combat.
	// PvE

	// Limit players to a certain camera perspective, such as only first-person. By default, players can use both first-person and third-person perspectives.
	// Perspective First
	// Perspective Third
	Perspective Both
	// Perspective Vehicle

	// Which port should be used when port forwarding.
	// Port 27015

Runtime
~~~~~~~

Some commands only work during runtime. For example, the ``Save`` command only works while the server is running.

You can use runtime commands in two ways:

a. Type them into the **Server Console**.
b. From the **in-game chat** (only if you are an administrator) while prefixing them with ``@`` or ``/``.

.. tip::

	Add your Steam ID as an administrator (a) via the ``Owner`` command, (b) by using the ``Admin`` command during runtime, or (c) by including it in the **Adminlist.dat** file.

Use the ``Help`` command to either view a list of *all* commands, or describe a specific command.

Some runtime commands require ``Cheats`` to be enabled. For example, ``Give`` is a cheat command used to spawn items.

Learn about more commands on the `Unturned Wiki <https://unturned.wiki.gg/Commands>`_.

Difficulty Settings
```````````````````

Configure your server's game rules, public server listing, and many other options from the :ref:`doc_servers_server_configuration` file.

By default, there are separate config files for each difficulty preset – Easy, Normal, and Hard. By default, servers use the Normal difficulty file.

.. hint::

	You can use the ``Difficulty`` command to use the settings configured in either the Easy or Hard files.

Steam Workshop Mods
```````````````````

Use the  **WorkshopDownloadConfig.json** file to install mods from the Steam Workshop for use on your server. Players attempting to join your server will automatically download any mods configured in this file!

1. | Open the **WorkshopDownloadConfig.json** file.

2. | Find a mod on the Steam Workshop and copy the **File ID** in the URL. For example, the `Hawaii <https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636>`_ map.

	.. code-block:: text

		URL: https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636
		File ID: 1753134636


3. | Add the File ID to the **File_IDs** list. Example:

	.. code-block:: json

		"File_IDs":
		[
			1753134636
		],

.. tip::

	You can add multiple mods by separating each File ID with a comma. Example:

	.. code-block:: json

		"File_IDs":
		[
			1753134636,
			1702240229
		],

4. During server startup, any specified mods (and their dependencies) will be installed and updated. Players will automatically begin downloading any mods while connecting to the server.

Curated maps—and a few official arena maps—are only accessible via the Steam Workshop. Like other mods, they need to be downloaded by the server in order to be used:

.. csv-table::
   :file: /img/WorkshopMapIDs.csv
   :widths: 30, 70
   :header-rows: 1

.. _doc_server_hosting:internet_server:

Switching to an Internet Server
-------------------------------

Servers are hosted as a **LAN server** by default. This means players can only join when invited through your Steam friends list, or by using your randomly-generated Server Code. LAN servers are *not* visible from the Internet server list. There are a couple options for switching from a LAN server to an **Internet server**.

.. attention::

	Internet servers should follow our :ref:`Server Hosting Rules <doc_server_hosting_rules>`.

Get started by adding a :ref:`Game Server Login Token <doc_servers_gslt>` (GSLT). This login token is necessary when hosting an Internet server. Configuring it also means your Server Code will no longer change each time you launch your server.

For an Internet server, you must configure either :ref:`Fake IP <doc_servers_fake_ip>` or :ref:`Port Forwarding <doc_servers_port_forward>`. Configuring both is **not necessary**. Fake IP is easier to enable, and it should be adequate for most servers.

Related Topics
--------------

Some servers may benefit from a more advanced setup than the one provided in our :ref:`Simple Setup <doc_server_hosting:simple_setup>` guide. Chiefly:

- :ref:`Use SteamCMD <doc_steamcmd>` to host multiple servers at once.
- Install plugins through frameworks like :ref:`Rocket (LDM) <doc_servers_rocket>` or :ref:`OpenMod <doc_servers_openmod>`.
