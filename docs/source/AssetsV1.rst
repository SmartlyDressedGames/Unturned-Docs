Assets v1
=========

Unturned **assets** associate game data with Unity asset bundles. They are stored in ``.dat`` files. When scanning a folder for assets the game looks for a ``.dat`` file with the same name as the folder, or an ``Asset.dat`` file.

Newer features use `Assets v2 <AssetsV2.rst>`_, but it is unlikely that older features will be ported.

File Format
-----------

Empty lines and lines starting with ``//`` are treated as comments. Otherwise every line is a key-value pair with a space separating the key from the value. Keys must be unique within the file.

Arrays or lists are typically handled by a key specifying the number of items, and then appending the index number to each element's key. For example:

.. code-block:: cs
	
	// Total number of elements in list
	Blueprints 2

	// First element has an index of 0
	Blueprint_0 A

	// Second element has an index of 1
	Blueprint_1 B

Occasionally there are asset types that simply look for the presence of a particular key, not its value. These are referred to as flags. For example: item assets check for the ``Pro`` flag marking that it is a Steam economy item.

Game Data
---------

``Type`` *string*: Specific guides will list individual type names. This determines which keys the game will read.

``ID`` *int*: 16-bit identifier. Unfortunately this id must be unique within each category of assets (vehicles, items, animals, etc). Objects are the exception from this legacy restriction because they have been upgraded to fully use GUIDs.

``GUID`` *string*: Refer to `GUID <GUID.rst>`_ documentation. Several newer features refer to v1 assets by their GUID. If left empty the game will prepend a GUID during startup.

Unity Asset Bundles
-------------------

Each Unturned asset is associated with a Unity asset bundle. If there is a master bundle in the file hierarchy that takes priority, otherwise a ``.unity3d`` bundle with the same name as the `.dat` file is used. There are several keys available to control the asset bundle:

`Asset_Bundle_Version` *int*: Indicates which version of Unity this ``.unity3d`` bundle was built for. When Unturned upgrades Unity versions it tries to maintain backwards compatibility based on this number. 1 is Unity 5.5, 2 is 2017.4 LTS and 3 is 2018.4 LTS.

`Master_Bundle_Override` *string*: Name of a master bundle to use rather than the ``.unity3d`` bundle or master bundle found in the hierarchy.

`Exclude_From_Master_Bundle` *string*: If this key exists the asset will look for a ``.unity3d`` bundle instead of the hierarchy.

`Bundle_Override_Path` *string*: Path within the master bundle to load rather than this asset's file path.

Localization
------------

Each asset looks for a localization `.dat` file in the same directory based on the current language. For example: ``English.dat`` or ``French.dat``.
