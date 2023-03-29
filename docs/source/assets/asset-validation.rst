.. _doc_asset_validation:

Asset Validation
================

During startup the game runs fast basic health checks on assets while loading, but there are a variety of slower tests available. These can be enabled with the ``-ValidateAssets`` command-line flag. Errors are logged to the Client.log file, as well as to the Asset Errors menu.

**Navmesh Readable**: Object navmeshes should have the CPU Readable flag enabled in Unity. This is required for Recast to be able to generate the level navmesh.

**Mesh Readable**: Most non-navmesh meshes do not need to have the CPU Readable flag enabled in Unity. This is not currently enforced however, as the core content has lots of cases which still need cleaning up.

**Missing Meshes**: Mesh filters without a mesh, or mesh renderers without a mesh filter are found and logged.

**Mesh Vertex Counts**: Meshes with unusually high numbers of vertices are recommended to be optimized. Typically this is simply a matter of removing unused faces and vertices. Colliders have a lower recommended target because collision against complex meshes is slower than rendering complex meshes.

**Missing Materials**: Renderers without materials are found and logged. One exception to this is "DepthMask" renderers which are set by the game.

**Material Counts**: Renderers with high numbers of materials are recommended to be merged and simplified. Each individual material needs to be rendered separately (usually), so less materials is better. Good practice is to have one material for each render type on an object, i.e. a material for the opaque surfaces and a material for the transparent surfaces (if any).

**Texture Readable**: Most textures do not need to have the CPU Readable flag enabled in Unity. Disabling means a copy is not kept in RAM. One exception is shirt and pants textures which are layered on the CPU.

**Texture NPOT**: Most textures should have power-of-two dimensions, e.g. 1 x 2, 4 x 4, 64 x 32, etc. GPUs are best equipped for drawing these resolutions. Unity has import options for scaling up or down to the nearest power of two.

**Audio Samples**: Long audio clips with high frequencies are found and logged. Generally the clips are fairly small files.
