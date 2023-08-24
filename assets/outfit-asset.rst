.. _doc_assets_outfit:

Outfit Assets
=============

A selection of clothing items that should be worn together when generating preview images for outfits. Outfit preview images can be generated with the \[F1] menu available from the Workshop section of the main menu.

Metadata
--------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *string*: ``SDG.Unturned.OutfitAsset``

Outfit Properties
-----------------

**Items** *array* of :ref:`Asset Pointers <doc_data_assetptr>`: Asset pointers to clothing item(s). These clothing items will be worn together in any preview images generated of this outfit. For example:

.. code-block:: cs
	
	"Asset"
	{
		"Items"
		[
			// Top
			"9fd6032f9a24404eaf28961fc7f2d289"

			// Bottom
			"d4ec52a157f746edbc3a4df8ae79ddef"

			// Mask
			"1adc30f0dbf246eba1c0c6a183206aad"

			// Hat
			"daf02a225ebc4b76ae51ca485706e470"
		]
	}