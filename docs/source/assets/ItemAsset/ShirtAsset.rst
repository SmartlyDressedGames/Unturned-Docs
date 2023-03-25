.. _doc_itemasset_shirt:

Shirt Assets
============

Shirts can be worn by players and zombies.

This inherits the :ref:`BagAsset <doc_itemasset_bag>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Shirt``)

**Useable** *enum* (``Clothing``)

**ID** *uint16*: Must be a unique identifier.

Shirt Asset Properties
----------------------

**Ignore_Hand** *flag*: Specified if shirt should ignore a player's left-handed setting.

Body Mesh Replacements
----------------------

For the full documentation, refer to the :ref:Character Mesh Replacement <doc_character_mesh_replacement>` documentation.

**Has_1P_Character_Mesh_Override** *bool*: A prefab named "Character_Mesh_1P_Override_0" should be loaded. Defaults to false.

**Character_Mesh_3P_Override_LODs** *uint16*: Number of prefabs to load for each LOD index. Defaults to 0.

**Has_Character_Material_Override** *bool*: A material named "Character_Material_Override" should be loaded to replace the first-person and third-person mesh materials. Defaults to false.
