.. _doc_item_asset_tactical:

Tactical Assets
===============

Tactical attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Tactical attachments inherit properties from the CaliberAsset class, which in turn inherits properties from the ItemAsset class. Properties that are required to be included are listed in the table below.

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
     - ``Tactical``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Laser <doc_item_asset_tactical:laser>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Laser_Color <doc_item_asset_tactical:laser_color>`
     - :ref:`color <doc_data_color>`
     - ``#FF0000``
   * - :ref:`Light <doc_item_asset_tactical:light>`
     - :ref:`flag <doc_data_builtin_types>`
     - 
   * - :ref:`Melee <doc_item_asset_tactical:melee>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Rangefinder <doc_item_asset_tactical:rangefinder>`
     - :ref:`flag <doc_data_flag>`
     - 

Property Descriptions
`````````````````````

.. _doc_item_asset_tactical:laser:

Laser :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Provides a toggleable laser.

----

.. _doc_item_asset_tactical:laser_color:

Laser_Color :ref:`color <doc_data_color>` ``#FF0000``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Override the default red color with the specified value. This property supports using legacy color parsing.

----

.. _doc_item_asset_tactical:light:

Light :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Provides a toggleable flashlight, and allows for using :ref:`PlayerSpotLightConfig <doc_data_playerspotlightconfig>` properties.

----

.. _doc_item_asset_tactical:melee:

Melee :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

Provides the ability to perform a melee attack. This attack does 40 damage, and is not configurable.

----

.. _doc_item_asset_tactical:rangefinder:

Rangefinder :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::

Provides a toggleable rangefinder.