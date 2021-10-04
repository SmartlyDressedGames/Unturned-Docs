Grip Assets
============

Grip attachments are inventory items that can be attached to ranged weapons.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Grip`)

**ID** *uint16*: Must be a unique identifier.

Caliber Asset Properties
------------------------

**Ballistic_Damage_Multiplier** *float*: Multiplier on damage. Defaults to the value used for the Damage property.

**Damage** *float*: Multiplier on damage. Defaults to 1. Deprecated in favor of Ballistic_Damage_Multiplier.

**Firerate** *byte*: Amount to decrease ranged weapon's firerate value by. Decreasing by a larger value will allow the ranged weapon to fire more often.

**Paintable** *bool*: Specified if the attachment should be affected by Steam Economy ranged weapon skins that include support for attachments.

**Recoil_X** *float*: Multiplier on horizontal recoil.

**Recoil_Y** *float*: Multiplier on vertical recoil.

**Shake** *float*: Multiplier on shake.

**Spread** *float*: Multiplier on spread.

**Sway** *float*: Multiplier on sway.

Grip Asset Properties
---------------------

**Bipod** *bool*: Specified if effects should only take place while prone.
