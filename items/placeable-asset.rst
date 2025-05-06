.. _doc_item_asset_placeable:

Placeable Assets
================

The ItemPlaceableAsset class is a base class that other classes are derived from. Placeables are able to be placed by players.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Placeable Asset Properties
--------------------------

**Item_Dropped_On_Destroy** :ref:`Asset Pointer <doc_data_assetptr>`: Spawn table for items dropped when destroyed.

**Min_Items_Dropped_On_Destroy** *int*: Minimum number of items to drop when destroyed. Defaults to 0.

**Max_Items_Dropped_On_Destroy** *int*: Maximum number of items to drop when destroyed. Defaults to 0.

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

**SalvageItem** :ref:`Asset Pointer <doc_data_assetptr>`: Override the default salvaging behavior by pointing to a specific item that should be added when salvaging a placeable that is below 100% health. This property cannot point to a :ref:`SpawnAsset <doc_assets_spawn>` – only :ref:`ItemAssets <doc_item_asset_intro>` are supported. By default, this property will choose a random item used in the placeable's blueprints.
