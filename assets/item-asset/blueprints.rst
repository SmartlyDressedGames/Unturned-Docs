.. _doc_item_asset_blueprints:

Blueprints
==========

**Blueprints** *int*: Total number of blueprints.

**Blueprint\_#\_Type** *enum* (``Ammo``, ``Apparel``, ``Barricade``, ``Furniture``, ``Gear``, ``Repair``, ``Structure``, ``Supply``, ``Tool``, ``Utilities``): Section of the crafting menu that the blueprint listing should appear under.

**Blueprint\_#\_Supplies** *int*: Total number of unique supplies required for the blueprint.

**Blueprint\_#\_Supply\_#\_ID** *int16*: ID of the unique supply required.

**Blueprint\_#\_Supply\_#\_Amount** *int*: Quantity of the unique supply required.

**Blueprint\_#\_Supply\_#\_Critical** *flag*: The unique supply is a prerequisite to showing the blueprint listing.

**Blueprint\_#\_State\_Transfer** *flag*: Transfer current state of supplies to product.

**Blueprint\_#\_Tool** *int16*: ID of the unique non-consumed tool required.

**Blueprint\_#\_Tool_Critical** *flag*: The unique non-consumed tool is a prerequisite to showing the blueprint listing.

**Blueprint\_#\_Level** *int*: Skill level required.

**Blueprint\_#\_Skill** *enum* (``Cook``, ``Craft``, ``None``, ``Repair``): The skill required. If value is set to "Cook", then the player will also need to be next to a heat source (such as a lit Campfire).

**Blueprint\_#\_Build** *int16* or *GUID*: ID or GUID of auditory effect to play upon crafting.

**Blueprint\_#\_Map** *string*: Name of the map that the blueprint is restricted to.

**Blueprint_#_Searchable** *bool*: If true, blueprint can be visible in search results without the required items. Defaults to true. Useful to hide debug blueprints that are not acquirable through gameplay.

Product Properties
------------------

Product properties are used for blueprints where only one unique item is outputted. Output properties are used for blueprints that should output multiple unique items.

**Blueprint\_#\_Product** *int16*: ID of the product created.

**Blueprint\_#\_Products** *int*: Quantity of the product created.

**Blueprint\_#\_Outputs** *int*: Total number of unique products created.

**Blueprint\_#\_Output\_#\_ID** *int16*: ID of the unique product created.

**Blueprint\_#\_Output\_#\_Amount** *int*: Quantity of the unique product created.

Conditions
----------

Blueprints can use quest conditions and rewards. A common usage is to make it so a blueprint is only available during a seasonal event. For more information, refer to the documentation for :ref:`Conditions <doc_npc_asset_conditions>` and :ref:`Rewards <doc_npc_asset_rewards>` respectively.

Blueprint conditions and rewards are prefixed with ``Blueprint_#_``. For example, ``Blueprint_0_Condition_0_Type Holiday``.
