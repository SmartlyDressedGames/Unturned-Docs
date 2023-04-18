.. _doc_item_asset_farm:

Farm Assets
===========

**Grow** *ushort*: The item ID to spawn when harvested.

**Grow_SpawnTable** *GUID*: GUID of a spawntable from which to spawn an item when harvested.

**Growth** *uint*: How long before its fully grown. In seconds

**Affected_By_Agriculture_Skill** *bool*: If true, the amount of crops acquired when harvesting the plant is affected by the Agriculture skill. Defaults to true.

**Allow_Fertilizer** *bool*: If true, allows the player to use fertilizer to fully grow the plant. Defaults to true.

**Ignore_Soil_Restrictions** *bool*: If false, only allow placement on Soil Materials. If true, allow placement anywhere. Default to false.

**Harvest_Reward_Experience** *uint*: The amount of experience gained upon harvesting.

===========

**NOTICE**: To have multi-harvest crops, use the following calcul "HP / 2 = Amount of possible harvests"
