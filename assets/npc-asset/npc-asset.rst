.. _doc_object_asset_npc:

NPC Character Assets
====================

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``NPC``)

**ID** *uint16*: Must be a unique identifier.

**PlayerKnowsNameFlagID** *uint16*: If non-zero, NPC name is shown as ??? until bool flag is true. For example if set to 20 the NPC name is ??? until a Flag_Bool reward with ID 20 is set to true.

Clothing
--------

**Shirt** *uint16* or *GUID*: ID or GUID of shirt to wear.

**Pants** *uint16* or *GUID*: ID or GUID of pants to wear.

**Hat** *uint16* or *GUID*: ID or GUID of hat to wear.

**Backpack** *uint16* or *GUID*: ID or GUID of backpack to wear.

**Vest** *uint16* or *GUID*: ID or GUID of vest to wear.

**Mask** *uint16* or *GUID*: ID or GUID of mask to wear.

**Glasses** *uint16* or *GUID*: ID or GUID of glasses to wear.

Holiday outfits
```````````````

NPC characters can have event-specific outfits, which will only appear during the assigned seasonal event.

**Has_Halloween_Outfit** *flag*: Specified if event-specific clothing should be worn during the Halloween event.

**Halloween_Shirt** *uint16* or *GUID*: ID or GUID of shirt to wear during the Halloween event.

**Halloween_Pants** *uint16* or *GUID*: ID or GUID of pants to wear during the Halloween event.

**Halloween_Hat** *uint16* or *GUID*: ID or GUID of hat to wear during the Halloween event.

**Halloween_Backpack** *uint16* or *GUID*: ID or GUID of backpack to wear during the Halloween event.

**Halloween_Vest** *uint16* or *GUID*: ID or GUID of vest to wear during the Halloween event.

**Halloween_Mask** *uint16* or *GUID*: ID or GUID of mask to wear during the Halloween event.

**Halloween_Glasses** *uint16* or *GUID*: ID or GUID of glasses to wear during the Halloween event.

**Has_Christmas_Outfit** *flag*: Specified if event-specific clothing should be worn during the Festive event.

**Christmas_Shirt** *uint16* or *GUID*: ID or GUID of shirt to wear.

**Christmas_Pants** *uint16* or *GUID*: ID or GUID of pants to wear.

**Christmas_Hat** *uint16* or *GUID*: ID or GUID of hat to wear.

**Christmas_Backpack** *uint16* or *GUID*: ID or GUID of backpack to wear.

**Christmas_Vest** *uint16* or *GUID*: ID or GUID of vest to wear.

**Christmas_Mask** *uint16* or *GUID*: ID or GUID of mask to wear.

**Christmas_Glasses** *uint16* or *GUID*: ID or GUID of glasses to wear.

Appearance
----------

While in the Appearance menu in-game, modders can press Page Down to copy the player's current appearance to clipboard.

**Face** *int*: Index of face image.

**Hair** *int*: Index of hair mesh.

**Beard** *int*: Index of beard mesh.

**Color_Skin** *hex triplet*: Six-digit hexadecimal number representing RGB color.

**Color_Hair** *hex triplet*: Six-digit hexadecimal number representing RGB color.

**Backward** *flag*: Specified if character is left-handed.

Pose
----

**Primary** *uint16* or *GUID*: ID or GUID of the weapon carried on the character's back, parallel to the spine.

**Secondary** *uint16* or *GUID*: ID or GUID of the weapon carried on the character's hip, perpendicular to the spine.

**Tertiary** *uint16* or *GUID*: ID or GUID of a non-weapon item to carry.

**Equipped** *enum* (``Primary``, ``Secondary``, ``Tertiary``): The item in the specified slot will be held in the character's hands, rather than carried.

**Dialogue** *uint16* or *GUID*: ID or GUID of the dialogue asset to open when interacted with.

**Pose** *enum* (``Asleep``, ``Crouch``, ``Passive``, ``Prone``, ``Rest``, ``Sit``, ``Stand``, ``Surrender``, ``Under_Arrest``): Idle animation.

**Pose_Head_Offset** *float*: Offset of the NPC's head from their body, in meters. Positive numbers offset it forward, while negative numbers offset it backward. Defaults to 0.1.

**Pose_Lean** *float*: How far the NPC leans left or right, as a number from -1 to 1. Positive numbers learn to the NPC's left, while negative numbers lean to the NPC's right. Defaults to 0.

**Pose_Pitch** *float*: How far the NPC leans forward or backward, in degrees. Numbers greater than 90 lean forward, while numbers less than 90 lean backward. Defaults to 90.

Conditions
----------

An NPC character can be made to only appear while certain :ref:`conditions <doc_npc_asset_conditions>` are met by the player.

Localization
------------

**Name** *string*: Object name in level editors.

**Character** *string*: Character name displayed when interacted with. 
