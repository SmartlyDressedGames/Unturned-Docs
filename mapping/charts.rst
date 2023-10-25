.. _doc_mapping_charts:

Charts
======

The Charts.unity3d file determines the colors usable by a map's chart view. This file contains two 32 × 1 px textures: "Height_Strip" and "Layer_Strip".

Height_Strip
------------

Height_Strip is used for topographical colors. The leftmost pixel (0, 0) is used for water. Other pixels are sampled based on the height of the terrain, going from the lowest potential point (1, 0) to the highest potential point (31, 0).

.. note:: Objects can also be configured to sample from the "Water" pixel (0, 0) or the "Ground" pixel (20, 0) of the Height_Strip.

Layer_Strip
-----------

Layer_Strip is used when something obstructs the terrain, such as an object or tree. The pixel sampled depends on the type of obstruction. Objects can be configured to use a different part of the Layer_Strip than their default, with some pixels only being used by such objects.

- (0, 0): Concrete roads wider than 8 meters use this pixel. Usable by objects.
- (1, 0): Concrete roads where width is less than or equal to 8 meters use this pixel. Usable by objects.
- (2, 0): Usable by objects.
- (3, 0): Non-concrete roads. Usable by objects.
- (4, 0): Usable by objects.
- (14, 0): Resources.
- (15, 0): Large-type objects. Usable by objects.
- (16, 0): Medium-type objects. Usable by objects.