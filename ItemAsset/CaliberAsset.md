**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/item-asset/caliber-asset.html) instead.*

Caliber Assets
==============

This inherits the [ItemAsset](/ItemAsset/README.md) class.

Caliber Asset Properties
------------------------

**Aiming\_Movement\_Speed\_Multiplier** *float*: Character movement speed multiplier while the gun is aiming down sights.

**Aiming\_Recoil\_Multiplier** *float*: Recoil magnitude multiplier while the gun is aiming down sights.

**Aim\_Duration\_Multiplier** *float*: Multiplier for `Aim_In_Duration` value.

**Ballistic_Damage_Multiplier** *float*: Multiplier on damage. Defaults to the value used for the Damage property.

**Calibers** *uint16*: Total amount of unique calibers.

**Caliber_#** *uint16*: Caliber ID for acceptable attachment compatibility.

**Damage** *float*: Multiplier on damage. Defaults to 1. Deprecated in favor of Ballistic_Damage_Multiplier.

**Destroy_Attachment_Colliders** *bool*: If false, colliders are not destroyed when the base gun item's colliders are destroyed. Kept for compatibility if mods relied on attachments having colliders, but it is not recommended because there have been reports of low performance with some mods having complex colliders on every modded attachment in the level. Defaults to true.

**Firerate** *byte*: Amount to decrease ranged weapon's firerate value by. Decreasing by a larger value will allow the ranged weapon to fire more often.

**Paintable** *flag*: Specified if the attachment should be affected by Steam Economy ranged weapon skins that include support for attachments.

**Recoil_X** *float*: Multiplier on horizontal recoil.

**Recoil_Y** *float*: Multiplier on vertical recoil.

**Shake** *float*: Multiplier on shake.

**Spread** *float*: Multiplier on spread.

**Sway** *float*: Multiplier on sway.
