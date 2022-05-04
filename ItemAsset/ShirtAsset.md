Shirt Assets
============

Shirts can be worn by players and zombies.

This inherits the [BagAsset](/ItemAsset/BagAsset.md) class.

Shirt Asset Properties
----------------------

**Ignore_Hand** *flag*: Specified if shirt should ignore a player's left-handed setting.

Body Mesh Replacements
----------------------

See [CharacterMeshReplacement.md](/CharacterMeshReplacement.md) for full documentation.

**Has_1P_Character_Mesh_Override** *bool*: A prefab named "Character_Mesh_1P_Override_0" should be loaded. Defaults to false.

**Character_Mesh_3P_Override_LODs** *uint16*: Number of prefabs to load for each LOD index. Defaults to 0.

**Has_Character_Material_Override** *bool*: A material named "Character_Material_Override" should be loaded to replace the firstperson and thirdperson mesh materials. Defaults to false.
