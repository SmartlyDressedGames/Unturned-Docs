.. _doc_itemasset_placeable:

Placeable Assets
================

Temporarily noting this here, until placeable assets are properly documented.

Not ideal to be adding this so late in development, but at least it is a step in the right direction because barricade/structure have a lot in common.

**SalvageItem** `Asset Pointer <AssetPtr.rst>`_: Item added when picking up below 100% health. Defaults to a random item used in the placeable's blueprints.

**Min_Items_Dropped_On_Destroy** *int*: Minimum number of items to drop when destroyed.

**Max_Items_Dropped_On_Destroy** *int*: Maximum number of items to drop when destroyed.

**Item_Dropped_On_Destroy** :ref:`Asset Pointer <doc_data_assetptr>`: Spawn table for items dropped when destroyed.
