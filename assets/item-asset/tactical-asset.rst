.. _doc_item_asset_tactical:

Tactical Assets
===============

Tactical attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Tactical``)

**ID** *uint16*: Must be a unique identifier.

Tactical Asset Properties
-------------------------

**Laser** *flag*: Provides a toggleable laser.

**Laser_Color** :ref:`color <doc_data_file_format>`: Overrides the default red color. When using the legacy color parsing, the ``_R``, ``_G``, and ``_B`` keys are floats within the range of [0, 1].

**Light** *flag*: Provides a toggleable flashlight, and allows for using the SpotLight dictionary.

**Melee** *flag*: Provides the ability to perform a melee attack.

**Rangefinder** *flag*: Provides a toggleable rangefinder.

SpotLight Dictionary
````````````````````

**SpotLight_Enabled** *bool*: When true, this item should have a toggleable light source. Defaults to true.

**SpotLight_Range** *float*: Range of the light source's beam, in meters. Defaults to 64.

**SpotLight_Angle** *float*: Angle of the light source's beam in degrees. Defaults to 90.

**SpotLight_Intensity** *float*: Intensity of the light source's beam. Defaults to 1.3.

**SpotLight_Color** :ref:`color <doc_data_file_format>`: Color of the light source's beam. Defaults to #f5df93.