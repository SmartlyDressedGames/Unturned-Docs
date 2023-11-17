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
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Ballistic_Drop <doc_item_asset_barrel_property_ballistic_drop>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Braked <doc_item_asset_barrel_property_braked>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Durability <doc_item_asset_barrel_property_durability>`
     - :ref:`byte <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Gunshot_Rolloff_Distance_Multiplier <doc_item_asset_barrel_property_gunshot_rolloff_distance_multiplier>`
     - :ref:`float <doc_data_builtin_types>`
     - See description
   * - :ref:`Silenced <doc_item_asset_barrel_property_silenced>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Volume <doc_item_asset_barrel_property_volume>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``

Property Descriptions
`````````````````````

.. _doc_item_asset_barrel_property_ballistic_drop:

Ballistic_Drop :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Gravity acceleration multiplier for bullets in flight.

----

.. _doc_item_asset_barrel_property_braked:

Braked :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::

Muzzle flash should be hidden.

----

.. _doc_item_asset_barrel_property_durability:

Durability :ref:`byte <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Amount of quality lost after each firing of the ranged weapon. When this value is greater than 0, the item always has a visible item quality shown.

----

.. _doc_item_asset_barrel_property_gunshot_rolloff_distance_multiplier:

Gunshot_Rolloff_Distance_Multiplier :ref:`float <doc_data_builtin_types>` See description
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on gunshot rolloff distance. Defaults to ``0.5`` if ``Silenced``, otherwise to ``1``.

----

.. _doc_item_asset_barrel_property_silenced:

Silenced :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::

Alerts should not be generated.

----

.. _doc_item_asset_barrel_property_volume:

Volume :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on gunfire sound volume.