Foliage
=======

This is an `Asset v2 <AssetsV2.rst>`_ class.

There are sub-types of foliage asset for different uses, most notably instanced meshes (grass, pebbles) and resources (trees). Unlike the older system, tree baking cannot be configured directly within the level editor yet, but there are two benefits to separating baking settings from the trees themselves:

1. Different biomes or levels can use the same trees with different parameters. For example a dense forest material with less dense forest surrounding it, or using tree assets from a different map with custom configuration.
2. Eventually the resource system should be converted into a regular objects (this will be automatic) but most objects do not need foliage parameters.

FoliageResourceInfoAsset Properties Reference
---------------------------------------------

``Resource`` `Asset Pointer <AssetPtr.rst>`_: actual tree to spawn.

``Obstruction_Radius`` *float*: spawn position is invalid if a sphere with this radius overlaps anything.

``Density`` *float*: this value is poorly named. One tree will try to spawn per this many square meters. For example a value of 4 will spawn approximately once per 2m x 2m area.

``Min_Weight`` *float*: [0, 1] only spawn if landscape material weight is greater than this value.

``Max_Weight`` *float*: [0, 1] only spawn if landscape material weight is less than this value.

``Min_Angle`` *float*: [0, 90] degrees only spawn if surface angle is greater than this value. For example a boulder only spawning on slopes steeper than 45 degrees.

``Max_Angle`` *float*: [0, 90] degrees only spawn if surface angle is less than this value. For example a tree not growing on slopes steeper than 30 degrees.

Upgrade Devkit Foliage from V1 to V2
------------------------------------

Note: maps with auto-converted terrain from the 3.22.8.0 update will already have been converted to V2.

V1 of devkit foliage unfortunately saved small individual regions into their own files, which makes maps slow to copy, download and install. V2 fixes this by storing pointers for each region into a single file at the cost of RAM in editor.

Following the 3.22.20.0 update, maps with foliage V1 will default to saving as V2 without the ``-SaveFoliageUsingV2`` command-line argument. The older files are still kept in the map's Foliage directory as a backup, so they should be manually removed after conversion to free up space.
