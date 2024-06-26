.. _doc_data_ebatterymode:

EBatteryMode
============

The EBatteryMode enumerated type is used to determine how a vehicle battery should behave.

Enumerators
```````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``None``
     - Battery charge remains unchanged.
   * - ``Burn``
     - Battery charge will deplete over time.
   * - ``Charge``
     - Battery charge will replenish over time.
