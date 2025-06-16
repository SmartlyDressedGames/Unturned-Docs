.. _doc_mapping_redirectors:

Editor Asset Redirectors
========================

**Editor Asset Redirectors** allow for quickly replacing objects, resources, materials, or foliage assets in bulk.

Redirects apply while loading a map in the level editor. Any changes are then kept when saving the map.

Create a file named "**EditorAssetRedirectors.txt**" in the Unturned folder.

- Empty lines are ignored.
- Lines starting with ``//`` or ``#`` are ignored.
- Each redirect should include two :ref:`GUIDs <doc_data_guid>` separated by an arrow ``->``.

For example:

.. code-block:: text

	// Replace Boulder_00 with Boulder_01
	6125b4de591b44359237f6d7191dd919 -> ee402fc9debe4f03bffb31a49eb04fb7

	// Replace Maple_0 with Maple_3
	63cb368c94b14000aabc5325b048cfa3 -> 011d1369cd56497488827b44509b0b4b
