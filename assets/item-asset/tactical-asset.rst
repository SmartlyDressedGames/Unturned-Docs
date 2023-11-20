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

**Light** *flag*: Provides a toggleable flashlight, and allows for using :ref:`PlayerSpotLightConfig <doc_data_playerspotlightconfig>` properties.

**Melee** *flag*: Provides the ability to perform a melee attack, dealing 40 damage. This damage value is not configurable.

**Rangefinder** *flag*: Provides a toggleable rangefinder.