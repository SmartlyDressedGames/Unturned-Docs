Sight Assets
============

Sight attachments are inventory items that can be attached to ranged weapons.

This inherits the [CaliberAsset](/ItemAsset/CaliberAsset.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Sight`)

**ID** *uint16*: Must be a unique identifier.

Sight Asset Properties
----------------------

**Holographic** *bool*: Specified if sight is holographic.

**Nightvision_Color_B** *uint8*: The blue color component of an RGBA color, represented as a byte. Default value for Civilian is equivalent to 102. Default value for Military is 20.

**Nightvision_Color_G** *uint8*: The green color component of an RGBA color, represented as a byte. Default value for Civilian is equivalent to 102. Default value for Military is 120.

**Nightvision_Color_R** *uint8*: The red color component of an RGBA color, represented as a byte. Default value for Civilian is equivalent to 102. Default value for Military is 80.

**Nightvision_Fog_Intensity** *float*: Intensity of fog while nightvision is active. Default value for Civilian is 0.5. Default value for Military is 0.25.

**Vision** *enum* (`None`, `Military`, `Civilian`, `Headlamp`): Type of unique lighting vision effect to use. Defaults to None.

**Zoom** *float*: Multiplicative amount of zoom. Defaults to 1.
