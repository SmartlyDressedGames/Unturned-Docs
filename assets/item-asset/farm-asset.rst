.. _doc_item_asset_farm:

Farm Assets
===========

Farms (localized as "plants") are a placeable seeds capable of growing into harvestable crops. When a seed is planted, it will grow over time until eventually harvestable. Growing can be finished immediately by either rainfall, or by using a :ref:`growth supplement <doc_item_asset_grower>` on the plant. A fully-grown crop can be harvested, which deals 2 damage to the crop. A crop can be harvested until it has 0 health remaining.

This inherits the :ref:`BarricadeAsset <doc_item_asset_barricade>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Farm``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Farm``)

**ID** *uint16*: Must be a unique identifier.

Farm Asset Properties
---------------------

**Affected_By_Agriculture_Skill** *bool*: If true, the amount of crops acquired when harvesting the plant is affected by the `Agriculture skill <https://wiki.smartlydressedgames.com/wiki/Skills>`_. Defaults to true.

**Allow_Fertilizer** *bool*: If true, allows the player to use fertilizer to fully grow the plant. Defaults to true.

**Grow** *ushort*: Legacy ID of the item to spawn when harvested.

**Grow_SpawnTable** :ref:`GUID <doc_data_guid>`: GUID of a spawntable from which to spawn an item when harvested.

**Growth** *uint*: In seconds, how long before the crop is fully grown.

**Harvest_Reward_Experience** *uint*: The amount of experience gained upon harvesting. Defaults to 1.

**Ignore_Soil_Restrictions** *bool*: If false, only allow placement on Soil Materials. If true, allow placement anywhere. Default to false.

**Rain_Affects_Growth** *bool*: If true, the plant will fully finish growing after rainy weather. Defaults to true.

**Harvest_Rewards**: NPC reward list granted when harvesting the grown plant. For more information, please refer to the :ref:`Rewards <doc_npc_asset_rewards>` documentation.

.. tip::
	
	The ``Health`` property from the parent ItemAsset class can be configured to allow for harvesting a crop multiple times. A plant can be harvested a number of items equal to ``Health / 2``. For example, a plant with 10 health can be harvested up to 5 times.
