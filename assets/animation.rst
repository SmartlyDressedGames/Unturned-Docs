.. _doc_assets_animation:

Animation
=========

Unturned's character rig is terrible – so using existing animations is recommended for your sanity.

Export
------

1. Ensure scene unit system is metric with unit scale set to 1.0 and length set to meters.
2. Select the Skeleton node.
3. File > Export > FBX
4. Selected Objects: True
5. Apply Scale: FBX Units Scale
6. Add Leaf Bones: False
7. Primary Bone Axis: +X
8. Secondary Bone Axis: -Y

Note that the Item.prefab from Unity is attached to the left or right hook with a local rotation of (0, 0, 90).
