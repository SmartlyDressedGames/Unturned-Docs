**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/character-mesh-replacement.html) instead.*

Character Mesh Replacement
==========================

The player's character mesh can be entirely replaced with a special [shirt item](/ItemAsset/ShirtAsset.md). There's an example CharacterMeshReplacementTest item (ID 1522), as well as example source files in the ExampleAssets.unitypackage under the Shirts directory.

Two limitations are that it must be a shirt because only shirts are loaded for first person (1P) views, and the 1P model should only contain the arms because the rest of the body is not animated.

Asset properties:

* Has_1P_Character_Mesh_Override: true
* Character_Mesh_3P_Override_LODs: >0
* Has_Character_Material_Override: true
* Hair_Visible: true/false
* Beard_Visible: true/false

If Has_1P_Character_Mesh_Override is true then the game will try to load a prefab named "Character_Mesh_1P_Override_0". This should have a MeshFilter component with the first person arms replacement mesh.

If Character_Mesh_3P_Override_LODs is greater than zero then the game will try to load prefabs for each LOD index (e.g., Character_Mesh_3P_Override_0). These should have MeshFilter components for the third person replacement meshes.

If Has_Character_Material_Override is true then the game will try to load a material named "Character_Material_Override" to replace the 1P and 3P mesh materials. Without this, equipped shirt and pants textures will be used by default.
