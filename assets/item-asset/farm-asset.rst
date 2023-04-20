.. _doc_item_asset_farm:

Farm Assets
===========

Temporarily noting this here, until farm assets are properly documented.

**Grow** *ushort*: The item ID to spawn when harvested.

**Grow_SpawnTable** *GUID*: GUID of a spawntable from which to spawn an item when harvested.

**Growth** *uint*: In seconds, how long before the crop is fully grown.

**Affected_By_Agriculture_Skill** *bool*: If true, the amount of crops acquired when harvesting the plant is affected by the Agriculture skill. Defaults to true.

**Allow_Fertilizer** *bool*: If true, allows the player to use fertilizer to fully grow the plant. Defaults to true.

**Ignore_Soil_Restrictions** *bool*: If false, only allow placement on Soil Materials. If true, allow placement anywhere. Default to false.

**Harvest_Reward_Experience** *uint*: The amount of experience gained upon harvesting. Defaults to 1.

===========

.. note::
	
	To have crops that can be harvested multiple times, use the following calculation ``Health / 2 = Number of Harvests``.
