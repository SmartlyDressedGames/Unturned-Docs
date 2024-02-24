.. _doc_assets_crafting_blacklist:

Crafting Blacklist Assets
=========================

Prevents specific items or blueprints from being used while crafting. They are hidden from the item quick actions menu and recipe list.

**Type** *string*: ``SDG.Unturned.CraftingBlacklistAsset``

**Input_Items** array of Item :ref:`Asset Pointers <doc_data_assetptr>`: Any blueprints consuming these items cannot be crafted. For example (blacklisted items are highlighted):

.. code-block:: cpp
  :linenos:
  :emphasize-lines: 4, 7-10, 13-16

	"Input_Items"
	[
		// Orange Hoodie
		"GUID" "67c76cdf16024bf68b6e5d14d4c617ab"
		
		// Individual items can also be enclosed in brackets { }
		{
			// Eaglefire
			GUID b03d581a5c1a490f995f8deba57b0f17
		}

		// Jeans
		dab78cc4d66645bfb8169be7c15cf876
		55c69817a31448b685c7f788ec7d2d0c
		bdae9d26ca704d729b2b0f34812d2a36
		67a6ec52e4b24ffd89f75ceee0eb5179
	]

**Output_Items** array of Item :ref:`Asset Pointers <doc_data_assetptr>`: Any blueprints generating these items cannot be crafted.

**Blueprints** array: Prevent specific individual blueprints from being crafted. Each entry has an ``Item`` :ref:`Asset Pointer <doc_data_assetptr>` and ``Blueprint`` index. For example, to prevent the Chef Hat from being salvaged:

.. code-block:: text

	Blueprints
	[
		{
			Item a6099002318e4d58b8e59d431bcf1b8a
			Blueprint 0
		}
	]

**Allow_Core_Blueprints** *bool*: Defaults to true. If false, blueprints from the vanilla/built-in items are not allowed.
