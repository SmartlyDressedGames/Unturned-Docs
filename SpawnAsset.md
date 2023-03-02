Spawn Assets
============

The spawn asset type represents the weighted chances of an individual item, vehicle, or animal spawning at an any given spawn point. Create custom spawn tables that can be used on custom, curated, and official maps.

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Spawn`)

**ID** *uint16*: Must be a unique identifier. IDs 1‒1000 are reserved for official content.

Roots
-----

Roots are the spawners that your spawn table will attach itself to. This is useful when adding new spawn tables to preexisting spawn tables, such as those used by official maps. Tables are the things that will get spawned by your spawner. A spawner at the bottom of the chain will be entirely assetIDs, whereas one near the top will likely be entirely spawnIDs.

**Roots** *int*: Total number of parents.

**Root\_#\_Spawn\_ID** *uint16*:  ID of parent spawn table.

**Root\_#\_Override** *flag*: Zeroes the weight of default spawns in the parent spawn table. Useful for mods intended to replace official content, such as with total conversions.

**Root\_#\_Weight** *int*: Weight of this table in the parent spawn table.

Tables
------

Tables are the assets spawned from the spawner, referenced by ID. These could be additional spawn tables; or individual assets like items, vehicles, and animals.

**Tables** *int*: Total number of children.

**Table\_#\_Spawn_ID** *uint16*: ID of a spawn table to recursively spawn a child from.

**Table\_#\_Asset_ID** *uint16*: ID of asset to spawn.

**Table\_#\_Weight** *int*: Weight of this child in the table.
