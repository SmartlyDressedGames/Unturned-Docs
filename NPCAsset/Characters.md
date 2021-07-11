NPC Character
=============

**GUID** *32-digit hexadecimal*: Refer to [GUID](GUID.md) documentation.

**Type** *enum* (`NPC`)

**ID** *uint16*: Must be a unique identifier.

Clothing
--------

**Shirt** *uint16*: ID of shirt to wear.

**Pants** *uint16*: ID of pants to wear.

**Hat** *uint16*: ID of hat to wear.

**Backpack** *uint16*: ID of backpack to wear.

**Vest** *uint16*: ID of vest to wear.

**Mask** *uint16*: ID of mask to wear.

**Glasses** *uint16*: ID of glasses to wear.

### Holiday outfits

NPC characters can have event-specific outfits, which will only appear during the assigned seasonal event.

**Has_Halloween_Outfit** *bool*: Event-specific clothing should be worn during the Halloween event.

**Halloween_Shirt** *uint16*: ID of shirt to wear during the Halloween event.

**Halloween_Pants** *uint16*: ID of pants to wear during the Halloween event.

**Halloween_Hat** *uint16*: ID of hat to wear during the Halloween event.

**Halloween_Backpack** *uint16*: ID of backpack to wear during the Halloween event.

**Halloween_Vest** *uint16*: ID of vest to wear during the Halloween event.

**Halloween_Mask** *uint16*: ID of mask to wear during the Halloween event.

**Halloween_Glasses** *uint16*: ID of glasses to wear during the Halloween event.

**Has_Christmas_Outfit** *bool*: Event-specific clothing should be worn during the Festive event.

**Christmas_Shirt** *uint16*: ID of shirt to wear.

**Christmas_Pants** *uint16*: ID of pants to wear.

**Christmas_Hat** *uint16*: ID of hat to wear.

**Christmas_Backpack** *uint16*: ID of backpack to wear.

**Christmas_Vest** *uint16*: ID of vest to wear.

**Christmas_Mask** *uint16*: ID of mask to wear.

**Christmas_Glasses** *uint16*: ID of glasses to wear.

Appearance
----------

While in the Appearance menu in-game, modders can press Page Down to copy the player's current appearance to clipboard.

**Face** *int*: Index of face image.

**Hair** *int*: Index of hair mesh.

**Beard** *int*: Index of beard mesh.

**Color_Skin** *hex triplet*: Six-digit hexadecimal number representing RGB color.

**Color_Hair** *hex triplet*: Six-digit hexadecimal number representing RGB color.

**Backward** *bool*: Character is left-handed.

Pose
----

**Primary** *uint16*: Weapon carried on the character's back, parallel to the spine.

**Secondary** *uint16*: Weapon carried on the character's hip, perpendicular to the spine.

**Tertiary** *uint16*: Non-weapon item to carry.

**Equipped** *enum* (`Primary`, `Secondary`, `Tertiary`): The item in the specified slot will be held in the character's hands, rather than carried.

**Dialogue** *uint16*: ID of the dialogue asset to open when interacted with.

**Pose** *enum* (`Asleep`, `Crouch`, `Passive`, `Prone`, `Rest`, `Sit`, `Stand`, `Surrender`, `Under_Arrest`): Idle animation.

Localization
------------

**Name** *string*: Object name in level editors.

**Character** *string*: Character name displayed when interacted with. 
