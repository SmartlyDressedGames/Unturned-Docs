.. _doc_item_asset_barrel:

Barrel Assets
=============

Barrel attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Barrel attachments inherit properties from the CaliberAsset class, which in turn inherits properties from the ItemAsset class. Properties that are required to be included are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1
   
   * - Class
     - Property Name
     - Required Value
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`GUID <doc_item_asset_intro:guid>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`ID <doc_item_asset_intro:id>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Type <doc_item_asset_intro:type>`
     - ``Barrel``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Ballistic_Drop <doc_item_asset_barrel:ballistic_drop>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Braked <doc_item_asset_barrel:braked>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Durability <doc_item_asset_barrel:durability>`
     - :ref:`byte <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Gunshot_Rolloff_Distance_Multiplier <doc_item_asset_barrel:gunshot_rolloff_distance_multiplier>`
     - :ref:`float <doc_data_builtin_types>`
     - See description
   * - :ref:`Silenced <doc_item_asset_barrel:silenced>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Volume <doc_item_asset_barrel:volume>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``

Property Descriptions
`````````````````````

.. _doc_item_asset_barrel:ballistic_drop:

Ballistic_Drop :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Gravity acceleration multiplier for bullets in flight.

----

.. _doc_item_asset_barrel:braked:

Braked :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::

Muzzle flash should be hidden.

----

.. _doc_item_asset_barrel:durability:

Durability :ref:`byte <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Amount of quality lost after each firing of the ranged weapon. When this value is greater than ``0``, the item always has a visible item quality shown.

----

.. _doc_item_asset_barrel:gunshot_rolloff_distance_multiplier:

Gunshot_Rolloff_Distance_Multiplier :ref:`float <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on gunshot rolloff distance. Defaults to ``0.5`` if ``Silenced``, otherwise to ``1``.

----

.. _doc_item_asset_barrel:silenced:

Silenced :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::

Alerts should not be generated when firing.

----

.. _doc_item_asset_barrel:volume:

Volume :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplier on gunfire sound volume. This is often used alongside with ``Silenced``, but doing so is not required.