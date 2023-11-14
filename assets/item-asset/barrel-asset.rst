.. _doc_item_asset_barrel:

Barrel Assets
=============

Barrel attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Item Asset Properties
`````````````````````

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Barrel``)

**ID** *uint16*: Must be a unique identifier.

Barrel Asset Properties
```````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 0

   * - **Ballistic_Drop**
     - *float*
     - ``1``
   * - **Braked**
     - *flag*
     - n/a
   * - **Durability**
     - *byte*
     - ``0``
   * - **Gunshot_Rolloff_Distance_Multiplier**
     - *float*
     - See description
   * - **Silenced**
     - *flag*
     - n/a
   * - **Volume**
     - *float*
     - ``1``

Property Descriptions
`````````````````````

Ballistic_Drop *float* = ``1``
::::::::::::::::::::::::::::::::

Gravity acceleration multiplier for bullets in flight.

----

Braked *flag*
::::::::::::::::::::::::

Muzzle flash should be hidden.

----

Durability *byte* = ``0``
::::::::::::::::::::::::::::

Amount of quality lost after each firing of the ranged weapon. When this value is greater than 0, the item always has a visible item quality shown.

----

Gunshot_Rolloff_Distance_Multiplier *float* = See description
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on gunshot rolloff distance. Defaults to ``0.5`` if ``Silenced``, otherwise to ``1``.

----

Silenced *flag*
::::::::::::::::

Alerts should not be generated.

----

Volume *float* = ``1``
::::::::::::::::::::::::

Multiplier on gunfire sound volume.