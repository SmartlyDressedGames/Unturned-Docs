.. _doc_assets_spawn:

Spawn Assets
============

The spawn asset type represents the weighted chances of an individual item, vehicle, or animal spawning at an any given spawn point. Create custom spawn tables that can be used on custom, curated, and official maps.

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Spawn``)

**ID** *uint16*: Must be a unique identifier. IDs 1‒1000 are reserved for official content.

Tables
------

Tables are the assets spawned from the spawner, referenced by ID. These could be additional spawn tables; or individual assets like items, vehicles, and animals.

**Tables**: list of dictionaries. Each dictionary entry can contain these properties:

**Guid** :ref:`GUID <doc_data_guid>`: GUID of an asset to spawn or a spawn table to recursively spawn a child from. Used if ``LegacySpawnId`` and ``LegacyAssetId`` are both unset or zero.

**LegacySpawnId** *uint16*: ID of a spawn table to recursively spawn a child from. Use of ``Guid`` is encouraged instead to prevent ID conflicts between mods.

**LegacyAssetId** *uint16*: ID of asset to spawn. Use of ``Guid`` is encouraged instead to prevent ID conflicts between mods.

**Weight** *int32*: Weight of this entry in the table.

For example, this configuration has a 90% chance of spawning a Military Magazine and a 10% chance of spawning an Eaglefire:

.. code-block:: text

    Tables
    [
        {
            // Military Magazine
            Guid dbfb1d0d11ca438e9dffb95f76e61274
            Weight 180
        }
        {
            // Eaglefire
            Guid b03d581a5c1a490f995f8deba57b0f17
            Weight 20
        }
    ]

.. note:: This older format is used by most spawn assets. The newer format is recommended because it is more user-friendly, but the older format will continue to be supported.

    **Tables** *int32*: Total number of children.

    **Table_#_Spawn_ID** *uint16*: ID of a spawn table to recursively spawn a child from.

    **Table_#_Asset_ID** *uint16*: ID of asset to spawn.

    **Table_#_Weight** *int32*: Weight of this child in the table.

    **Table_#_GUID** :ref:`GUID <doc_data_guid>`: GUID of an asset to spawn or a spawn table to recursively spawn a child from. Used if ``Spawn_ID`` and ``Asset_ID`` are both unset or zero.

Roots
-----

Roots are the spawners that your spawn table will attach itself to. This is useful when adding new spawn tables to preexisting spawn tables, such as those used by official maps. Tables are the things that will get spawned by your spawner. A spawner at the bottom of the chain will be entirely assetIDs, whereas one near the top will likely be entirely spawnIDs.

**Roots**: list of dictionaries. Each dictionary entry can contain these properties:

**Guid** :ref:`GUID <doc_data_guid>`: GUID of parent spawn table. Used if ``LegacySpawnId`` is unset or zero.

**LegacySpawnId** *uint16*: ID of parent spawn table. Use of ``Guid`` is encouraged instead to prevent ID conflicts between mods.

**IsOverride** *bool*: If true, zeroes the weight of default spawns in the parent spawn table. Useful for mods intended to replace official content, such as with total conversions.

**Weight** *int32*: Weight of this entry in the parent spawn table.

.. note:: This older format is used by most spawn assets. The newer format is recommended because it is more user-friendly, but the older format will continue to be supported.

    **Roots** *int32*: Total number of parents.

    **Root_#_Spawn_ID** *uint16*: ID of parent spawn table.

    **Root_#_Override** *flag*: Zeroes the weight of default spawns in the parent spawn table. Useful for mods intended to replace official content, such as with total conversions.

    **Root_#_Weight** *int32*: Weight of this entry in the parent spawn table.

    **Root_#_GUID** :ref:`GUID <doc_data_guid>`: GUID of parent spawn table. Used if ``Spawn_ID`` is unset or zero.

Exporting Legacy Spawn Tables
-----------------------------

Legacy spawn tables can be created within the level editor. For the most, using the legacy spawn system is probably fine for most modded maps. But if you would like to take advantage of automatically keeping up-to-date with new official content—along with better supporting modded content on your map—then you should create spawn assets instead.

You might have already created some legacy spawn tables within the level editor. Fortunately, it is fairly straightforward to export those tables as spawn assets!

Open your map in the level editor. When you are ready to export, open the pause menu. Next to the button called "Legacy Spawns", enter a number above ``1000`` that should be used as the starting ID for your converted tables. Clicking the "Legacy Spawns" button will now generate spawn assets based on your legacy spawn tables.

This process will usually only take a couple seconds. As part of this process, all of the legacy spawn tables on your map will be automatically updated to point to your newly-created spawn assets instead. You should save the game before exiting.

These files will appear within a subfolder named "Exported_Legacy_Spawn_Tables", located within your map's folder. Root tables are prefixed with the map's name, while the converted tiers have been prefixed with the table's name. To start using your converted tables, create a folder named "Bundles" within your map folder, and move the contents of the "Exported_Legacy_Spawn_Tables" folder into it.

.. tip::

	You can use the "Proxy Tables" button to generate empty spawn asset files instead! This is a quick way to get started with creating spawn assets on a newly-created map, where you do not have any legacy spawn tables that need to be converted.

Along with converting the map's legacy spawn tables, the game will generate a spreadsheet named "IDs.csv". This spreadsheet can be used to more easily keep track of the IDs of each of your spawn assets.
