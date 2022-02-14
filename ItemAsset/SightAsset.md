Sight Assets
============

Sight attachments are inventory items that can be attached to ranged weapons.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Sight`)

**ID** *uint16*: Must be a unique identifier.

Caliber Asset Properties
------------------------

**Ballistic_Damage_Multiplier** *float*: Multiplier on damage. Defaults to the value used for the Damage property.

**Calibers** *uint16*: Total amount of unique calibers.

**Caliber_#** *uint16*: Caliber ID for acceptable attachment compatibility.

**Damage** *float*: Multiplier on damage. Defaults to 1. Deprecated in favor of Ballistic_Damage_Multiplier.

**Firerate** *byte*: Amount to decrease ranged weapon's firerate value by. Decreasing by a larger value will allow the ranged weapon to fire more often.

**Paintable** *bool*: Specified if the attachment should be affected by Steam Economy ranged weapon skins that include support for attachments.

**Recoil_X** *float*: Multiplier on horizontal recoil.

**Recoil_Y** *float*: Multiplier on vertical recoil.

**Shake** *float*: Multiplier on shake.

**Spread** *float*: Multiplier on spread.

**Sway** *float*: Multiplier on sway.

Sight Asset Properties
----------------------

**Holographic** *bool*: Specified if sight is holographic.

**Nightvision_Color_B** (*byte* or *float*): The blue color component of an RGBA color, represented as either a byte or a float. Default value for Civilian is 0.4. Default value for `Vision Military` is 20.

**Nightvision_Color_G** (*byte* or *float*): The green color component of an RGBA color, represented as either a byte or a float. Default value for Civilian is 0.4. Default value for `Vision Military` is 120.

**Nightvision_Color_R** (*byte* or *float*): The red color component of an RGBA color, represented as either a byte or a float. Default value for Civilian is 0.4. Default value for `Vision Military` is 80.

**Nightvision_Fog_Intensity** *float*: Intensity of fog while nightvision is active. Default value for `Vision Civilian` is 0.5. Default value for Military is 0.25.

**Vision** *enum* (`None`, `Military`, `Civilian`, `Headlamp`): Type of unique lighting vision effect to use. Defaults to None.

**Zoom** *float*: Multiplicative amount of zoom. Defaults to 1.
