.. _doc_item_asset_placeable:

Placeable Assets
================

Placeables are able to be placed by players.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Placeable Asset Properties
--------------------------

**Item_Dropped_On_Destroy** :ref:`Asset Pointer <doc_data_assetptr>`: Spawn table for items dropped when destroyed.

**Min_Items_Dropped_On_Destroy** *int*: Minimum number of items to drop when destroyed. Defaults to 0.

**Max_Items_Dropped_On_Destroy** *int*: Maximum number of items to drop when destroyed. Defaults to 0.

**SalvageItem** :ref:`Asset Pointer <doc_data_assetptr>`: Override the default salvaging behavior by pointing to a specific item that should be added when salvaging a placeable that is below 100% health. This property cannot point to a :ref:`SpawnAsset <doc_assets_spawn>` – only :ref:`ItemAssets <doc_item_asset_intro>` are supported. By default, this property will choose a random item used in the placeable's blueprints.
