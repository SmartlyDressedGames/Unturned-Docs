.. _doc_item_asset_placeable:

Placeable Assets
================

Placeables are able to be placed by players.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Placeable Asset Properties
--------------------------

**SalvageItem** :ref:`Asset Pointer <doc_data_assetptr>`: Item added when picking up below 100% health. Defaults to a random item used in the placeable's blueprints.

**Min_Items_Dropped_On_Destroy** *int*: Minimum number of items to drop when destroyed. Defaults to 0.

**Max_Items_Dropped_On_Destroy** *int*: Maximum number of items to drop when destroyed. Defaults to 0.

**Item_Dropped_On_Destroy** :ref:`Asset Pointer <doc_data_assetptr>`: Spawn table for items dropped when destroyed.
