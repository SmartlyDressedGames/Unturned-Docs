.. _doc_assets_itemdata:

Item Data (outdated)
====================

.. warning::
	
	This documentation file has been deprecated, and is no longer receiving updates. It has been superseded in favor of the `item-asset directory <item-asset>`_, which contains individual documentation files for each item asset class.
	
	This deprecated documentation file will be progressively phased out as the new documentation sources are expanded.

**Items** in *Unturned* encompass anything that can be carried in a player's in-game inventory. All items share some properties, while each item type has its own unique data.

Non-specific Data
-----------------

* Refer to :ref:`doc_item_asset_intro` instead.

**Durability**: Either a decimal probability chance of quality loss upon action, or guaranteed loss and durability value is instead representative of the amount lost.

- *Canteens*: Guaranteed quality loss occurs upon drinking. Durability value represents the amount of quality loss.
- *Melee Weapons*: Decimal probability chance of quality loss occurs upon hitting.
- *Ranged Weapons*: Decimal probability chance of quality loss occurs upon shooting.

**Wear**: Increment to degrade quality by. Only applicable to items where durability represents a decimal probability chance of quality loss.

**Invulnerable**: Specified if damage ignores structures, barricades, and vehicles that are considered invulnerable to low-power weaponry. Not applicable to explosive damage, which always ignores invulnerability.

Asset Bundles and Error Handling
````````````````````````````````

See :ref:`Asset Bundles <doc_asset_bundles>` for full documentation regarding asset bundles.