.. _doc_asset_definitions:

Asset Definitions
=================

Unturned **asset definitions** associate game data with Unity asset bundles. They are stored in ``.dat`` or ``.asset`` files.

For information about the file format please refer to :ref:`Data File Format <doc_data_file_format>`.

Header
------

Each asset has a common ``GUID`` and ``Type`` header:

**GUID** :ref:`GUID <doc_data_guid>`: Unique ID used to link assets together. If left empty the game will prepend a newly generated GUID during startup.

**Type** *string*: Specific guides will list individual type names. This determines which keys the game will read. It can also be set to the fully qualified name of any class in any module.

.. note::
	
	``Type`` and ``GUID`` can either be specified in the root dictionary (default), or in a ``Metadata`` sub-dictionary. For example this is valid as well:

	.. code-block:: text

		Metadata
		{
			GUID 7e4b847061b64272b42ea8869fd053c7
			Type SDG.Unturned.Asset
		}
	
	If ``GUID`` is specified in the ``Metadata`` sub-dictionary the game cannot (as of 2023-04-13) automatically prepend a newly generated one during startup.

Body
----

The body contains any class properties. Individual asset type documentation elaborates on these.

**ID** *uint16*: 16-bit identifier. Unfortunately this ID must be unique within each category of assets (vehicles, items, animals, etc). Objects are the exception from this legacy restriction because they have been upgraded to fully use GUIDs.

Optionally the body properties can be placed into an ``Asset`` sub-dictionary. For example:

.. code-block:: text
	
	GUID [...]
	Type [...]
	Asset
	{
		ID [...]
		Key1 Value
		Key2 Value
	}

Is equivalent to:

.. code-block:: text
	
	GUID [...]
	Type [...]
	ID [...]
	Key1 Value
	Key2 Value

Unity Asset Bundles
-------------------

Each Unturned asset is associated with a Unity asset bundle. If there is a master bundle in the file hierarchy that takes priority, otherwise a ``.unity3d`` bundle with the same name as the ``.dat`` file is used. There are several keys available to control the asset bundle:

**Asset_Bundle_Version** *int*: Indicates which version of Unity this ``.unity3d`` bundle was built for. When Unturned upgrades Unity versions it tries to maintain backwards compatibility based on this number. 1 is Unity 5.5, 2 is 2017.4 LTS and 3 is 2018.4 LTS.

**Master_Bundle_Override** *string*: Name of a master bundle to use rather than the ``.unity3d`` bundle or master bundle found in the hierarchy.

**Exclude_From_Master_Bundle** *string*: If this key exists the asset will look for a ``.unity3d`` bundle instead of the hierarchy.

**Bundle_Override_Path** *string*: Path within the master bundle to load rather than this asset's file path.

Localization
------------

Each asset looks for a localization ``.dat`` file in the same directory based on the current language. For example: ``English.dat`` or ``French.dat``.

Loading Order
-------------

When scanning a folder for assets the game checks in this order:

1. Is there a ``.asset`` file with the same name as the folder? e.g. Eaglefire.asset in the Eaglefire folder
2. Is there a ``.dat`` file with the same name as the folder? e.g. Eaglefire.dat in the Eaglefire folder
3. Is there an ``Asset.dat`` file?
4. Otherwise, load all files with the ``.asset`` extension in the folder.
