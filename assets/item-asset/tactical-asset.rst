.. _doc_item_asset_tactical:

Tactical Assets
===============

Tactical attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Item Asset Properties
`````````````````````

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Tactical``)

**ID** *uint16*: Must be a unique identifier.

Tactical Asset Properties
`````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Laser <doc_item_asset_tactical_property_laser>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Laser_Color <doc_item_asset_tactical_property_laser_color>`
     - :ref:`color <doc_data_file_format>`
     - ``#FF0000``
   * - :ref:`Light <doc_item_asset_tactical_property_light>`
     - :ref:`flag <doc_data_builtin_types>`
     - n/a
   * - :ref:`Melee <doc_item_asset_tactical_property_melee>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Rangefinder <doc_item_asset_tactical_property_rangefinder>`
     - :ref:`flag <doc_data_flag>`
     - n/a

Property Descriptions
`````````````````````

.. _doc_item_asset_tactical_property_laser:

Laser :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::

Provides a toggleable laser.

----

.. _doc_item_asset_tactical_property_laser_color:

Laser_Color :ref:`color <doc_data_file_format>` ``#FF0000``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the default red color. When using the legacy color parsing, the ``_R``, ``_G``, and ``_B`` keys are floats within the range of [0, 1].

----

.. _doc_item_asset_tactical_property_light:

Light :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::

Provides a toggleable flashlight, and allows for using :ref:`PlayerSpotLightConfig <doc_data_playerspotlightconfig>` properties.

----

.. _doc_item_asset_tactical_property_melee:

Melee :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::

Provides the ability to perform a melee attack.

----

.. _doc_item_asset_tactical_property_rangefinder:

Rangefinder :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::::

Provides a toggleable rangefinder.