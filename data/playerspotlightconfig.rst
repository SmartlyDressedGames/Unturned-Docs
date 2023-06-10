.. _doc_data_playerspotlightconfig:

PlayerSpotLightConfig
=====================

The PlayerSpotLightConfig struct contains properties for configuring player spot lights. Certain item assets are able to utilize these properties.

Properties
``````````

**SpotLight_Enabled** *bool*: When true, this item should have a toggleable light source. Defaults to true.

**SpotLight_Range** *float*: Range of the light source's beam, in meters. Defaults to 64.

**SpotLight_Angle** *float*: Angle of the light source's beam in degrees. Defaults to 90.

**SpotLight_Intensity** *float*: Intensity of the light source's beam. Defaults to 1.3.

**SpotLight_Color** :ref:`color <doc_data_file_format>`: Color of the light source's beam. Defaults to #f5df93.