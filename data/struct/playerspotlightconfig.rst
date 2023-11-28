.. _doc_data_playerspotlightconfig:

PlayerSpotLightConfig
=====================

The PlayerSpotLightConfig struct contains properties for configuring player spot lights. Certain item assets are able to utilize these properties.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`SpotLight_Enabled <doc_data_playerspotlightconfig:spotlight_enabled>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`SpotLight_Range <doc_data_playerspotlightconfig:spotlight_range>`
     - :ref:`float <doc_data_builtin_types>`
     - ``64``
   * - :ref:`SpotLight_Angle <doc_data_playerspotlightconfig:spotlight_angle>`
     - :ref:`float <doc_data_builtin_types>`
     - ``90``
   * - :ref:`SpotLight_Intensity <doc_data_playerspotlightconfig:spotlight_intensity>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1.3``
   * - :ref:`SpotLight_Color <doc_data_playerspotlightconfig:spotlight_color>`
     - :ref:`color <doc_data_file_format>`
     - ``#f5df93``

Property Descriptions
`````````````````````

.. _doc_data_playerspotlightconfig:spotlight_enabled:

SpotLight_Enabled :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, this item should have a toggleable light source.

----

.. _doc_data_playerspotlightconfig:spotlight_range:

SpotLight_Range :ref:`float <doc_data_builtin_types>` ``64``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Range of the light source's beam, measured in meters.

----

.. _doc_data_playerspotlightconfig:spotlight_angle:

SpotLight_Angle :ref:`float <doc_data_builtin_types>` ``90``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Angle of the light source's beam, measured in degrees.

----

.. _doc_data_playerspotlightconfig:spotlight_intensity:

SpotLight_Intensity :ref:`float <doc_data_builtin_types>` ``1.3``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Intensity of the light source's beam.

----

.. _doc_data_playerspotlightconfig:spotlight_color:

SpotLight_Color :ref:`color <doc_data_file_format>` ``#f5df93``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Color of the light source's beam.