.. _doc_data_eslottype:

ESlotType
=========

The ESlotType enumerated type is used for item placement in displays or on characters, and determines which item slot(s) an equippable item can be placed in. Some assets may only support using specific enumerators.

Enumerators
```````````

.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Named Value
     - Description
   * - ``None``
     - Does not correspond to any slot. Equippables can be hotkeyed.
   * - ``Primary``
     - Corresponds to the "Primary" slot. Equippables can be used from the primary slot.
   * - ``Secondary``
     - Corresponds to the "Secondary" slot. Equippables from the primary or secondary slot.
   * - ``Tertiary``
     - Corresponds to the "Tertiary" slot. This is only used by NPCs.
   * - ``Any``
     - Corresponds to any/all item slots. Equippables can be used from any slot, or hotkeyed.