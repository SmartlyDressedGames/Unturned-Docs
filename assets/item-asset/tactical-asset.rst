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

**Laser_Color** *color*: Overrides default red color. Consists of **Laser_Color_R**, **Laser_Color_G**, **Laser_Color_B** *float* [0, 1].

**Light** *flag*: Provides a toggleable flashlight.

**Melee** *flag*: Provides the ability to perform a melee attack.

**Rangefinder** *flag*: Provides a toggleable rangefinder.
