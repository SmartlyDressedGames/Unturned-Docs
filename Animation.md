**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/animation.html) instead.*

Animation
=========

Unturned's (3.0) character rig is terrible. Using existing animations is recommended for your sanity. Unturned II's (4.0) rig is significantly more user friendly.

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
