.. _doc_assets_foliage:

Foliage Assets
==============

There are sub-types of foliage asset for different uses, most notably instanced meshes (grass, pebbles) and resources (trees). Unlike the older system, tree baking cannot be configured directly within the level editor yet, but there are two benefits to separating baking settings from the trees themselves:

1. Different biomes or levels can use the same trees with different parameters. For example a dense forest material with less dense forest surrounding it, or using tree assets from a different map with custom configuration.
2. Eventually the resource system should be converted into a regular objects (this will be automatic) but most objects do not need foliage parameters.

FoliageResourceInfoAsset Properties Reference
---------------------------------------------

``Type`` *string*: ``SDG.Unturned.FoliageResourceInfoAsset``

``Resource`` :ref:`Asset Pointer <doc_data_assetptr>`: actual tree to spawn.

``Obstruction_Radius`` *float*: spawn position is invalid if a sphere with this radius overlaps anything.

``Density`` *float*: this value is poorly named. One tree will try to spawn per this many square meters. For example a value of 4 will spawn approximately once per 2m x 2m area.

``Min_Weight`` *float*: [0, 1] only spawn if landscape material weight is greater than this value.

``Max_Weight`` *float*: [0, 1] only spawn if landscape material weight is less than this value.

``Min_Angle`` *float*: [0, 90] degrees only spawn if surface angle is greater than this value. For example a boulder only spawning on slopes steeper than 45 degrees.

``Max_Angle`` *float*: [0, 90] degrees only spawn if surface angle is less than this value. For example a tree not growing on slopes steeper than 30 degrees.

Upgrade Devkit Foliage from V1 to V2
------------------------------------

.. note::

	Maps with auto-converted terrain from the 3.22.8.0 update will have already been converted to V2.

V1 of devkit foliage saved each small, individual region into their own files, which made maps slow to copy, download, and install. V2 fixes this by storing pointers for each region into a single file, at the cost of RAM in the map editor.

Following the 3.22.20.0 update, maps using v1 foliage will automatically update to v2 the next time they are saved, without needing to use the ``-SaveFoliageUsingV2`` command-line argument. The older v1 foliage files are still kept in the map's Foliage directory as a backup. These v1 files can be manually removed after having converted to v2, in order to free up space.
