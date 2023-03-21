Crafting Blacklist Asset
========================

Prevents specific items or blueprints from being used while crafting. They are hidden from the item quick actions menu and recipe list.

``Input_Items`` array of Item `Asset Pointers <AssetPtr.rst>`_: Any blueprints consuming these items are cannot be crafted.

.. code-block:: cs
	
	"Input_Items"
	[
		"### this is a GUID number ###"
		"### guid ###"
		{
			"NoteToSelf" "eaglefire"
			"GUID" "b03d581a5c1a490f995f8deba57b0f17"
		}
		"### another GUID number ###"
	]

``Output_Items`` array of Item `Asset Pointers <AssetPtr.rst>`_: Any blueprints generating these items cannot be crafted.

``Blueprints`` array: Prevent specific individual blueprints from being crafted. Each entry has an ``Item`` `Asset Pointer <AssetPtr.rst>`_ and ``Blueprint`` index. For example to prevent the Chef Hat from being salvaged:

.. code-block:: cs
	
	"Blueprints"
	[
		{
			"Item" "a6099002318e4d58b8e59d431bcf1b8a"
			"Blueprint" "0"
		}
	]

This is an `Asset v2 <AssetsV2.rst>`_ class.
