**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/item-asset/actions.html) instead.*

Actions
=======

Add additional context actions; the system currently supports [blueprint](Blueprints.md) actions. The game will automatically add various actions such as repairing and salvaging items, refilling magazines, stripping attachments, and crafting seeds.

**Actions** *int*: Total number of context actions.

**Action\_#\_Type** *enum* (`Blueprint`)

**Action\_#\_Source** *uint16*: ID of the item to source actions from. Default source is the current item.

**Action\_#\_Blueprints** *int*: Total number of blueprint indices.

**Action\_#\_Blueprint\_#\_Index** *int*: Index of the blueprint that action should perform.

**Action\_#\_Blueprint\_#\_Link** *flag*: Action should redirect to the associated blueprint listing, rather than immediately craft the item.

Button Properties
-----------------

**Action\_#\_Text** *string*: Context button name.

**Action\_#\_Tooltip** *string*: Context button tooltip.

**Action\_#\_Key** *string*: Translation key that can be used instead of a custom button name and tooltip. Valid translation keys and their localization can be found in the PlayerDashboardInventory.dat localization file. Valid keys include: `Attachments`, `Craft_Bandage`, `Craft_Dressing`, `Craft_Rag`, `Craft_Seed`, `Dequip`, `Drop`, `Equip`, `Pickup`, `Refill`, `Repair`, `Salvage`, `Store`, `Take`.
