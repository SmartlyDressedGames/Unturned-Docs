**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/item-asset/glasses-asset.html) instead.*

Glasses Assets
==============

Glasses can be worn by players and zombies.

This inherits the [GearAsset](/ItemAsset/GearAsset.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Glasses`)

**Useable** *enum* (`Clothing`)

**ID** *uint16*: Must be a unique identifier.

Glasses Asset Properties
------------------------

**Blindfold** *flag*: Specified if glasses should blacken the player's screen.

**Nightvision_Color_B** *uint8*: The blue color component of an RGBA color, represented as a byte. Default value for Civilian is equivalent to 102. Default value for Military is 20. Use with Vision Military and the other two color component properties to assign a custom nightvision color.

**Nightvision_Color_G** *uint8*: The green color component of an RGBA color, represented as a byte. Default value for Civilian is equivalent to 102. Default value for Military is 120. Use with Vision Military and the other two color component properties to assign a custom nightvision color.

**Nightvision_Color_R** *uint8*: The red color component of an RGBA color, represented as a byte. Default value for Civilian is equivalent to 102. Default value for Military is 80. Use with Vision Military and the other two color component properties to assign a custom nightvision color.

**Nightvision_Fog_Intensity** *float*: Intensity of fog while nightvision is active. Default value for Civilian is 0.5. Default value for Military is 0.25.

**Vision** *enum* (`None`, `Military`, `Civilian`, `Headlamp`): Type of unique lighting vision effect to use. Defaults to None. Use the Military enumerator when intending to assign a custom nightvision color via the color component properties.
