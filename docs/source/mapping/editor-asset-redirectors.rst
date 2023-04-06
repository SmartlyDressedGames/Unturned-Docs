.. _doc_mapping_redirectors:

Editor Asset Redirectors
========================

If many objects need to be replaced on a map the old object guid can be redirected to a new guid rather than manually replacing them. This works similarly to the automatic holiday object replacements, but applies while loading a map in the editor, and changes are kept when the map is saved.

The game looks for a file named "EditorAssetRedirectors.txt" in the Unturned folder. Empty lines and lines starting with "//" or "#" (comments) are ignored. The .txt file extension was chosen because it is the notepad default. Each line contains two guids separated by an arrow "->".

For example:

.. code-block:: text
	
	// Replace Boulder_00 with Boulder_01
	6125b4de591b44359237f6d7191dd919 -> ee402fc9debe4f03bffb31a49eb04fb7
	
	// Replace Grass_1 with Grass_France_1
	9a9655656f704b3caf717cea5a3b3cc2 -> d6dc5cc36f43429da668525e6ad174da
