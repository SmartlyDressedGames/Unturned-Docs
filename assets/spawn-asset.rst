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

    **Table\_#\_Spawn_ID** *uint16*: ID of a spawn table to recursively spawn a child from.

    **Table\_#\_Asset_ID** *uint16*: ID of asset to spawn.

    **Table\_#\_Weight** *int32*: Weight of this child in the table.

    **Table\_#\_GUID** :ref:`GUID <doc_data_guid>`: GUID of an asset to spawn or a spawn table to recursively spawn a child from. Used if ``Spawn_ID`` and ``Asset_ID`` are both unset or zero.

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

    **Root\_#\_Spawn\_ID** *uint16*: ID of parent spawn table.

    **Root\_#\_Override** *flag*: Zeroes the weight of default spawns in the parent spawn table. Useful for mods intended to replace official content, such as with total conversions.

    **Root\_#\_Weight** *int32*: Weight of this entry in the parent spawn table.

    **Root\_#\_GUID** :ref:`GUID <doc_data_guid>`: GUID of parent spawn table. Used if ``Spawn_ID`` is unset or zero.