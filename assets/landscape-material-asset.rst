.. _doc_assets_landscape_material:

Landscape Material Asset
========================

Landscape materials represent textures that can be applied to map terrain. Each asset specifies the texture drawn on the terrain, the physics material used for footstep and impact audio, and optionally foilage to be baked on wherever the material is painted.

**AprilFools_Redirect** :ref:`doc_data_guid`: GUID of the landscape material to use instead during the April Fools event.

**Auto_Max_Angle_Begin** *float*: Slope angle at which the auto-painted weight begins to fade out. Defaults to ``0.0``.

**Auto_Max_Angle_End** *float*: Steepest slope angle that is auto-painted. Defaults to ``0.0``.

**Auto_Min_Angle_Begin** *float*: Shallowest slope angle that is auto-painted. Defaults to ``0.0``.

**Auto_Min_Angle_End** *float*: Slope angle at which auto-painted weight is full strength. Defaults to ``0.0``.

**Auto_Ray_Length** *float*: Length of the sphere cast downwards when utilizing auto foundation. This should be set when using auto foundation painting. Defaults to ``0.0``.

**Auto_Ray_Mask** :ref:`ERayMask <doc_data_builtin_types>`: Value of the raymask layers the auto foundation sphere cast can hit. Defaults to ``0``.

**Auto_Ray_Radius** *float*: Radius of the auto foundation sphere cast. Defaults to ``0.0``.

**Christmas_Redirect** :ref:`doc_data_guid`: GUID of the landscape material to use instead during the Christmas event.

**Foliage** :ref:`doc_data_guid`: Points to a foilage collection to bake wherever this material is painted. Refer to :ref:`Foliage Assets <doc_assets_foliage>`.

**Halloween_Redirect** :ref:`doc_data_guid`: GUID of the landscape material to use instead during the Halloween event.

**Mask** :ref:`doc_data_masterbundleptr`: Normal map for the terrain material. Despite its name, the terrain material's normal map is set to this texture. If not specified, a black texture is used.

**Physics_Material** *string*: Name of the physics material used. Determines footstep sounds, bullet impacts, and other effects. This is matched against the ``UnityName`` of :ref:`Physics Material Assets <doc_assets_physics_material>`.

**Texture** :ref:`doc_data_masterbundleptr`: Albedo texture drawn on the terrain. When unspecified, a black texture is used.

**Use_Auto_Foundation** *bool*: If true, the level editor's auto splatmap mode paints this material at full strength beneath objects.

**Use_Auto_Slope** *bool*: If true, the level editor's auto splatmap mode paints this material according to the terrain's slope angle.