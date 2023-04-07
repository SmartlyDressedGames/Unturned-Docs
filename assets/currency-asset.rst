.. _doc_assets_currency:

Currency Assets
===============

Any collection of items with different numeric values can be associated together in a **Currency** asset. NPCs can then automatically convert between the different items, and vendor menus can display information using the linked currency. This is intended to be useful beyond real-world currencies, e.g. bartering ammunition.

.. figure:: img/VendorCurrency.jpg
	
	P.Riso's Hot Stuff vendor.

Asset Setup
-----------

This is an :ref:`Asset v2 <doc_assets_v2>` class.

The currency asset defines how numbers are formatted, which items make up the currency, and their individual values. An example can be found at Bundles/Items/Supplies/CanadianCurrency.asset.

**ValueFormat** *string*: String to format numeric value into. For example "${0:N0} CAD" is the vanilla Canadian currency format.

**DefaultConditionFormat** *string*: If an NPC currency condition does not specify a formatting string this is used as the default. {0} is the total value held in the player's inventory, and {1} is the condition value. For example "${0:N0}/{1:N0} CAD" is the vanilla Canadian currency format.

**Entries**: Array of items in the currency. Each has an **Item** GUID and **Value** integer. Optionally **Is_Visible_In_Vendor_Menu** bool can be false to hide the item from the NPC vendor currency list. For example these are the $10 and $20 notes in the Canadian currency:

.. code-block:: cs
	
	{
		"Item"
		{
			"GUID" "b6b87dfad5f342dc91bbb2de950f56ee"
		}
		"Value" "10"
	}
	{
		"Item"
		{
			"GUID" "3b9847bb328d445495b64be9e5ea9400"
		}
		"Value" "20"
	}

To link a vendor with a currency set the vendor asset's **Currency** to the currency asset's GUID. Vendors display all of the items sorted from lowest to highest value.

NPC Logic
---------

Conditions can use the **Currency** type to require different total amounts in the player's inventory. Rewards can use the **Currency** type as well to grant amounts. Refer to :ref:`Conditions <doc_npc_asset_conditions>` documentation and :ref:`Rewards <doc_npc_asset_rewards>` documentation for documentation.

Testing
-------

The built-in "give" command accepts currency GUIDs as an alternative to item IDs. For example the following grants $1,000 CAD to the local player:

.. code-block:: bash
	
	/give 5150ca8f765d4a68bfe54912146da410/1000
