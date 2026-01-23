.. _doc_item_asset_placeable:

Placeable Assets
================

The ItemPlaceableAsset class is a base class that other classes are derived from. Placeables are able to be placed by players.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Placeable Asset Properties
--------------------------

**ExplosionEffect_CopyModelPosition** *bool*: If true, effect spawns exactly at the model position without any offset. Defaults to false for backwards compatibility.

**ExplosionEffect_CopyModelRotation** *bool*: If true, effects spawns with same rotation as the model. Defaults to false for backwards compatibility.

**Item_Dropped_On_Destroy** :ref:`Asset Pointer <doc_data_assetptr>`: Item asset or spawn table for items dropped when destroyed.

This property can also be set to a string value of ``this``, which will use the the owning item's GUID. Useful to avoid accidentally writing the wrong ID.

**Min_Items_Dropped_On_Destroy** *int*: Minimum number of items to drop when destroyed. Defaults to 0.

**Max_Items_Dropped_On_Destroy** *int*: Maximum number of items to drop when destroyed. Defaults to 0.

**Items_Dropped_On_Destroy** *int*: Shorthand for setting both ``Min_Items_Dropped_On_Destroy`` and ``Max_Items_Dropped_On_Destroy``.

**Min_Items_Recovered_On_Salvage** *int*: Minimum number of items to receive when picked up below 100% health. Defaults to 1.

**Max_Items_Recovered_On_Salvage** *int*: Maximum number of items to receive when picked up below 100% health. Defaults to 1.

**Items_Recovered_On_Salvage** *int*: Shorthand for setting both ``Min_Items_Recovered_On_Salvage`` and ``Max_Items_Recovered_On_Salvage``.

**Min_Items_Recovered_On_Salvage_Full_Health** *int*: Minimum number of items to receive when picked up at 100% health. Defaults to 1.

**Max_Items_Recovered_On_Salvage_Full_Health** *int*: Maximum number of items to receive when picked up at 100% health. Defaults to 1.

**Items_Recovered_On_Salvage_Full_Health** *int*: Shorthand for setting both ``Min_Items_Recovered_On_Salvage_Full_Health`` and ``Max_Items_Recovered_On_Salvage_Full_Health``.

**PlaceableProvidesCraftingTags** list of :ref:`Asset Pointer <doc_data_assetptr>`: :ref:`doc_assets_tag` available to nearby players for blueprint requirements. Tags are listed in the item description as "crafting capabilities."

For example, the vanilla Brick Oven provides two tags:

.. code-block:: unturneddat

	PlaceableProvidesCraftingTags
	[
		// Heat Source (for backwards compatibility)
		20f30322bbcc4b01a4f116d22b24c21a
		// Enclosed Heat Source
		d2cc65b749e5477f95103601df89cdbc
	]

**SalvageItem** :ref:`Asset Pointer <doc_data_assetptr>`: Override the default salvaging behavior by pointing to a specific item or spawn table that should be added when salvaging a placeable that is below 100% health. By default, this property will choose a random item used in the placeable's blueprints.

**SalvageItem_FullHealth** :ref:`Asset Pointer <doc_data_assetptr>`: Defaults to self. Overrides the default pickup behavior by pointing to a specific item or spawn table that should be added when salvaging a placeable that is at 100% health.

This property can also be set to a string value of ``this``, which will use the the owning item's GUID. Useful to avoid accidentally writing the wrong ID.
