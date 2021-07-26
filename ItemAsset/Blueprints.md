Blueprints
==========

**Blueprints** *int*: Total number of blueprints.

**Blueprint\_#\_Type** *enum* (`Ammo`, `Apparel`, `Barricade`, `Furniture`, `Gear`, `Repair`, `Structure`, `Supply`, `Tool`, `Utilities`): Section of the crafting menu that the blueprint listing should appear under.

**Blueprint\_#\_Supplies** *int*: Total number of unique supplies required for the blueprint.

**Blueprint\_#\_Supply\_#\_ID** *int16*: ID of the unique supply required.

**Blueprint\_#\_Supply\_#\_Amount** *int*: Quantity of the unique supply required.

**Blueprint\_#\_Supply\_#\_Critical** *bool*: The unique supply is a prerequisite to showing the blueprint listing.

**Blueprint\_#\_State\_Transfer** *bool*: Transfer current state of supplies to product.

**Blueprint\_#\_Tool** *int16*: ID of the unique non-consumed tool required.

**Blueprint\_#\_Tool_Critical** *bool*: The unique non-consumed tool is a prerequisite to showing the blueprint listing.

**Blueprint\_#\_Level** *int*: Skill level required.

**Blueprint\_#\_Skill** *enum* (`Cook`, `Craft`, `None`, `Repair`): The skill required.

**Blueprint\_#\_Build** *int16*: Auditory effect ID to play upon crafting.

**Blueprint\_#\_Map** *string*: Name of the map that the blueprint is restricted to.

Product Properties
------------------

Product properties are used for blueprints where only one unique item is outputted.  Output properties are used for blueprints that should output multiple unique items.

**Blueprint\_#\_Product** *int16*: ID of the product created.

**Blueprint\_#\_Products** *int*: Quantity of the product created.

**Blueprint\_#\_Outputs** *int*: Total number of unique products created.

**Blueprint\_#\_Output\_#\_ID** *int16*: ID of the unique product created.

**Blueprint\_#\_Output\_#\_Amount** *int*: Quantity of the unique product created.

Conditions
----------

Blueprints can use quest conditions and rewards. A common usage is to make it so a blueprint is only available during a seasonal event. Refer to [Conditions.md](/NPCAsset/Conditions.md) and [Rewards.md](/NPCAsset/Rewards.md) for additional documentation.

Blueprint conditions and rewards are prefixed with `Blueprint_#_`. For example, `Blueprint_0_Condition_0_Type Holiday`.
