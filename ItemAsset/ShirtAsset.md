**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/item-asset/shirt-asset.html) instead.*

Shirt Assets
============

Shirts can be worn by players and zombies.

This inherits the [BagAsset](/ItemAsset/BagAsset.md) class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to [GUID](/GUID.md) documentation.

**Type** *enum* (`Shirt`)

**Useable** *enum* (`Clothing`)

**ID** *uint16*: Must be a unique identifier.

Shirt Asset Properties
----------------------

**Ignore_Hand** *flag*: Specified if shirt should ignore a player's left-handed setting.

Body Mesh Replacements
----------------------

See [CharacterMeshReplacement.md](/CharacterMeshReplacement.md) for full documentation.

**Has_1P_Character_Mesh_Override** *bool*: A prefab named "Character_Mesh_1P_Override_0" should be loaded. Defaults to false.

**Character_Mesh_3P_Override_LODs** *uint16*: Number of prefabs to load for each LOD index. Defaults to 0.

**Has_Character_Material_Override** *bool*: A material named "Character_Material_Override" should be loaded to replace the firstperson and thirdperson mesh materials. Defaults to false.
