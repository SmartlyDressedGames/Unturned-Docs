.. _doc_assets_material_palette:

Material Palette Assets
=======================

The ``MaterialPaletteAsset`` type allows an object to have multiple potential materials that it can use. A random material from the material palette is chosen every time the object is spawned in the level editor. In the level editor, material palettes can also be manually assigned to a selected object.

Metadata
--------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *string*: ``SDG.Unturned.MaterialPaletteAsset``

Material Palette Properties
---------------------------

**Materials** *array* of :ref:`Master Bundle Pointer <doc_data_masterbundleptr>` *dictionaries*: Each dictionary in the list should point to a material bundled in Unity.

.. code-block:: cs
	
	"Asset"
	{
		"Materials"
		[
			{
				"Name" "core.masterbundle"
				"Path" "Objects/Material_Palettes/House/House_00.mat"
			}
			{
				"Name" "core.masterbundle"
				"Path" "Objects/Material_Palettes/House/House_01.mat"
			}
		]
	}
