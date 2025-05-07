.. _doc_item_asset_blueprints:

Blueprints
==========

Blueprints can be added to items. These function as "crafting recipes", which allow players to craft other items, or even modify the state of the current item. Blueprints are not restricted to affecting the item they have been added to, and a blueprint's inputs and outputs can consist entirely of unrelated items.

:ref:`Context actions <doc_item_asset_actions>` are able to reference blueprints. Depending on the type of blueprint added to the item, the game may automatically generate a corresponding context action as well.

Game Data File
--------------

The ``Blueprints``, ``Blueprint_#_Type``, ``Blueprint_#_Supplies``, and ``Blueprint_#_Supply_#_ID`` properties are required by all blueprints. Blueprints also require that an output has been configured.

There are two methods available for configuring an output. When a blueprint only needs to output one item ID, the ``Blueprint_#_Products`` and ``Blueprint_#_Product`` properties can be used. Alternatively, blueprints can use the ``Blueprint_#_Outputs``, ``Blueprint_#_Output_#_ID``, and ``Blueprint_#_Output_#_Amount`` properties to output multiple, different item IDs.

It is very common that a blueprint will also use the ``Blueprint_#_Build``, ``Blueprint_#_Tool``, or ``Blueprint_#_Skill`` properties. Other properties for blueprints have more niche uses, and are less common.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Blueprint_#_Build <doc_item_asset_blueprints:blueprint_#_build>`
     - :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
     -
   * - :ref:`Blueprint_#_Level <doc_item_asset_blueprints:blueprint_#_level>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Map <doc_item_asset_blueprints:blueprint_#_map>`
     - :ref:`string <doc_data_builtin_types>`
     -
   * - :ref:`Blueprint_#_Origin <doc_item_asset_blueprints:blueprint_#_origin>`
     - :ref:`doc_data_eitemorigin`
     - ``Craft``
   * - :ref:`Blueprint_#_Output_#_Amount <doc_item_asset_blueprints:blueprint_#_output_#_amount>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Output_#_ID <doc_item_asset_blueprints:blueprint_#_output_#_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Output_#_Origin <doc_item_asset_blueprints:blueprint_#_output_#_origin>`
     - :ref:`doc_data_eitemorigin`
     - ``Craft``
   * - :ref:`Blueprint_#_Outputs <doc_item_asset_blueprints:blueprint_#_outputs>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Product <doc_item_asset_blueprints:blueprint_#_product>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - See description
   * - :ref:`Blueprint_#_Products <doc_item_asset_blueprints:blueprint_#_products>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`Blueprint_#_Searchable <doc_item_asset_blueprints:blueprint_#_searchable>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Blueprint_#_Skill <doc_item_asset_blueprints:blueprint_#_skill>`
     - :ref:`EBlueprintSkill <doc_item_asset_blueprints:eblueprinttype_enumeration>`
     - ``None``
   * - :ref:`Blueprint_#_State_Transfer <doc_item_asset_blueprints:blueprint_#_state_transfer>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Blueprint_#_State_Transfer_Delete_Attachments <doc_item_asset_blueprints:blueprint_#_state_transfer_delete_attachments>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Blueprint_#_Supplies <doc_item_asset_blueprints:blueprint_#_supplies>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Supply_#_AllowEmpty <doc_item_asset_blueprints:blueprint_#_supply_#_allowempty>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Blueprint_#_Supply_#_Amount <doc_item_asset_blueprints:blueprint_#_supply_#_amount>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Supply_#_Critical <doc_item_asset_blueprints:blueprint_#_supply_#_critical>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Blueprint_#_Supply_#_ID <doc_item_asset_blueprints:blueprint_#_supply_#_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
     -
   * - :ref:`Blueprint_#_Supply_#_Prioritization <doc_item_asset_blueprints:blueprint_#_supply_#_prioritization>`
     - :ref:`enum <doc_data_flag>`
     -
   * - :ref:`Blueprint_#_Tool <doc_item_asset_blueprints:blueprint_#_tool>`
     - :ref:`uint16 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Tool_Critical <doc_item_asset_blueprints:blueprint_#_type>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Blueprint_#_Type <doc_item_asset_blueprints:blueprint_#_tool_critical>`
     - :ref:`EBlueprintType <doc_item_asset_blueprints:eblueprinttype_enumeration>`
     -
   * - :ref:`Blueprints <doc_item_asset_blueprints:blueprints>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``

.. _doc_item_asset_blueprints:eblueprinttype_enumeration:

EBlueprintType Enumeration
``````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``Ammo``
     - Blueprint appears in the "Ammunition" tab.
   * - ``Apparel``
     - Blueprint appears in the "Apparel" tab.
   * - ``Barricade``
     - Blueprint appears in the "Barricades" tab.
   * - ``Furniture``
     - Blueprint appears in the "Furniture" tab.
   * - ``Gear``
     - Blueprint appears in the "Gear" tab.
   * - ``Repair``
     - Blueprint appears in the "Repair" tab.
   * - ``Structure``
     - Blueprint appears in the "Structures" tab.
   * - ``Supply``
     - Blueprint appears in the "Supplies" tab.
   * - ``Tool``
     - Blueprint appears in the "Tools" tab.
   * - ``Utilities``
     - Blueprint appears in the "Utilities" tab.

.. _doc_item_asset_blueprints:eblueprintskill_enumeration:

EBlueprintSkill Enumeration
```````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``None``
     - No skill is required.
   * - ``Craft``
     - "Crafting" skill is required.
   * - ``Cook``
     - "Cooking" skill is required.
   * - ``Repair``
     - "Engineer" skill is required.

Property Descriptions
`````````````````````

.. _doc_item_asset_blueprints:blueprint_#_build:

Blueprint_#_Build :ref:`doc_data_guid` or :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

GUID or legacy ID of an audio effect to play upon crafting.

----

.. _doc_item_asset_blueprints:blueprint_#_level:

Blueprint_#_Level :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If the blueprint requires a skill, its level must be equal to this value. This property is used in conjunction with ``Blueprint_#_Skill``.

----

.. _doc_item_asset_blueprints:blueprint_#_map:

Blueprint_#_Map :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Name of a map that this blueprint is restricted to. The blueprint will only be visible while on this map. For other maps, the blueprint is hidden from view.

----

.. _doc_item_asset_blueprints:blueprint_#_origin:

Blueprint_#_Origin :ref:`doc_data_eitemorigin` ``Craft``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. This property requires ``Blueprint_#_Product``.

----

.. _doc_item_asset_blueprints:blueprint_#_output_#_amount:

Blueprint_#_Output_#_Amount :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Quantity of the product created. For example, a quantity value of ``2`` would create two of the item specified in ``Blueprint_#_Output_#_ID``.

----

.. _doc_item_asset_blueprints:blueprint_#_output_#_id:

Blueprint_#_Output_#_ID :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of an item created as a product (i.e., an output that is provided after crafting the blueprint). This property requires ``Blueprint_#_Outputs``.

----

.. _doc_item_asset_blueprints:blueprint_#_output_#_origin:

Blueprint_#_Output_#_Origin :ref:`doc_data_eitemorigin` ``Craft``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Set the item origin. For example, setting the origin to ``Admin`` will cause items to spawn at full quality. This property requires ``Blueprint_#_Output_#_ID``.

----

.. _doc_item_asset_blueprints:blueprint_#_outputs:

Blueprint_#_Outputs :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Total number of ``Blueprint_#_Output_#_ID`` properties that have been configured.

----

.. _doc_item_asset_blueprints:blueprint_#_product:

Blueprint_#_Product :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of the item created as the product (i.e., an output that is provided after crafting the blueprint). To output multiple *different* items, refer to the ``Blueprint_#_Outputs`` and ``Blueprint_#_Output_#_ID`` properties instead.

When left unconfigured, this property will default to the value of the parent item's ``ID`` value.

----

.. _doc_item_asset_blueprints:blueprint_#_products:

Blueprint_#_Products :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Quantity of the product created. For example, a quantity value of ``2`` would create two of the item specified in ``Blueprint_#_Product``. This property requires that ``Blueprint_#_Product`` has been set.

----

.. _doc_item_asset_blueprints:blueprint_#_searchable:

Blueprint_#_Searchable :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, this blueprint is visible in the search results even when the player lacks the required items. This property can be used to hide blueprints intended for debugging that are not acquirable through normal gameplay.

----

.. _doc_item_asset_blueprints:blueprint_#_skill:

Blueprint_#_Skill :ref:`EBlueprintSkill <doc_item_asset_blueprints:eblueprintskill_enumeration>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The player must have leveled the specified skill in order to craft this blueprint. When set to ``Cook``, the player will also need to be next to a heat source (such as a lit Campfire). This property is used in conjunction with ``Blueprint_#_Level``.

----

.. _doc_item_asset_blueprints:blueprint_#_state_transfer:

Blueprint_#_State_Transfer :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Transfer the current state of any supplies to the product, when applicable. For example, some states that can be transferred include: amount (e.g., rounds in an ammunition box), quality percentage, selected firing mode, or fuel units (e.g., from a gas can).

----

.. _doc_item_asset_blueprints:blueprint_#_state_transfer_delete_attachments:

Blueprint_#_State_Transfer_Delete_Attachments :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true`` and ``State_Transfer`` is enabled, any output guns will have all of their attachments deleted.

----

.. _doc_item_asset_blueprints:blueprint_#_supplies:

Blueprint_#_Supplies :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Total number of ``Blueprint_#_Supply_#_ID`` properties that have been configured.

----

.. _doc_item_asset_blueprints:blueprint_#_supply_#_allowempty:

Blueprint_#_Supply_#_AllowEmpty :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, items with an "amount" of zero—such as empty magazines—are treated as an amount of one. In vanilla this is used to enable salvaging empty magazines.

----

.. _doc_item_asset_blueprints:blueprint_#_supply_#_amount:

Blueprint_#_Supply_#_Amount :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Quantity of the supply required. For example, a quantity value of ``2`` would require two of the item specified in ``Blueprint_#_Supply_#_ID``.

----

.. _doc_item_asset_blueprints:blueprint_#_supply_#_critical:

Blueprint_#_Supply_#_Critical :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The blueprint is only visible while the player has this supply. This property requires ``Blueprint_#_Supply_#_ID``.

----

.. _doc_item_asset_blueprints:blueprint_#_supply_#_id:

Blueprint_#_Supply_#_ID :ref:`uint16 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of an item that is required as a supply (i.e., an input that is consumed when crafting the blueprint). This property requires ``Blueprint_#_Supplies``.

This property can also be set to a string value of ``this``, which will use the the owning item's legacy ID. Useful for salvaging blueprints to avoid accidentally writing the wrong ID.

----

.. _doc_item_asset_blueprints:blueprint_#_supply_#_prioritization:

Blueprint_#_Supply_#_Prioritization :ref:`enum <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Controls which items are used first. Can be set to ``LowestAmount`` or ``LowestQuality``.

- ``LowestAmount`` sorts items by their amount (e.g., number of bullets in magazine) from lowest to highest, and consumes the emptiest ones first.
- ``LowestQuality`` sorts items by their quality from lowest (0%) to highest (100%), and consumes those nearest 0% first.

``AMMO`` type blueprints default to ``LowestAmount``, otherwise defaults to ``LowestQuality``.

----

.. _doc_item_asset_blueprints:blueprint_#_tool:

Blueprint_#_Tool :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Legacy ID of an item that is required as a "tool" for this blueprint. This item is not consumed when the blueprint is crafted.

----

.. _doc_item_asset_blueprints:blueprint_#_tool_critical:

Blueprint_#_Tool_Critical :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

If the blueprint requires a tool, it will only be visible while the player has that tool. This property requires ``Blueprint_#_Tool``.

----

.. _doc_item_asset_blueprints:blueprint_#_type:

Blueprint_#_Type :ref:`EBlueprintType <doc_item_asset_blueprints:eblueprinttype_enumeration>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This value determines which tab of the crafting menu that this blueprint appears under. All blueprints require that this has been configured.

----

.. _doc_item_asset_blueprints:blueprints:

Blueprints :ref:`int <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Total number of blueprints. All blueprints require that this has been configured.

Conditions and Rewards
``````````````````````

Blueprints can use quest conditions and rewards. A common usage is to make it so a blueprint is only available during a seasonal event. For more information, refer to the documentation for :ref:`Conditions <doc_npc_asset_conditions>` and :ref:`Rewards <doc_npc_asset_rewards>` respectively.

Blueprint conditions and rewards are prefixed with ``Blueprint_#_``. For example, ``Blueprint_0_Condition_0_Type Holiday``.

Game Data File v2
-----------------

.. warning:: Under construction! We might move this to a different page.

Starting with version 3.25.5.0, Blueprints can be specified as a :ref:`list <doc_data_file_format>` rather than prefixing each property with ``Blueprint_#_``. For example:

.. code-block:: unturneddat

	Blueprints
	[
		{
			// First blueprint properties
		}
		{
			// Second blueprint properties
		}
	]

Each blueprint dictionary has the following properties:

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`CategoryTag <doc_item_asset_blueprints:blueprint_v2_categorytag>`
     - :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_tag`
     -
   * - :ref:`Conditions <doc_item_asset_blueprints:blueprint_v2_conditions>`
     - :ref:`doc_npc_asset_conditions`
     -
   * - :ref:`Effect <doc_item_asset_blueprints:blueprint_v2_effect>`
     - :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_effect`
     -
   * - :ref:`InputItems <doc_item_asset_blueprints:blueprint_v2_inputitems>`
     - :ref:`list <doc_data_file_format>` of :ref:`doc_item_asset_blueprints_inputitem`
     -
   * - :ref:`Map <doc_item_asset_blueprints:blueprint_v2_map>`
     - :ref:`string <doc_data_builtin_types>`
     - ``""``
   * - :ref:`Name <doc_item_asset_blueprints:blueprint_v2_name>`
     - :ref:`string <doc_data_builtin_types>`
     - ``""``
   * - :ref:`Operation <doc_item_asset_blueprints:blueprint_v2_operation>`
     - :ref:`EBlueprintOperation <doc_item_asset_blueprints:eblueprintoperation_enumeration>`
     - ``None``
   * - :ref:`OutputItems <doc_item_asset_blueprints:blueprint_v2_outputitems>`
     - :ref:`list <doc_data_file_format>` of :ref:`doc_item_asset_blueprints_outputitem`
     -
   * - :ref:`RequiresNearbyCraftingTags <doc_item_asset_blueprints:blueprint_v2_requiresnearbycraftingtags>`
     - :ref:`list <doc_data_file_format>` of :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_tag`
     -
   * - :ref:`Rewards <doc_item_asset_blueprints:blueprint_v2_rewards>`
     - :ref:`doc_npc_asset_rewards`
     -
   * - :ref:`Searchable <doc_item_asset_blueprints:blueprint_v2_searchable>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Skill <doc_item_asset_blueprints:blueprint_v2_skill>`
     - :ref:`EBlueprintSkill <doc_item_asset_blueprints:eblueprintskill_enumeration>`
     - ``None``
   * - :ref:`Skill_Level <doc_item_asset_blueprints:blueprint_v2_skill_level>`
     - :ref:`int32 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`StateTransfer <doc_item_asset_blueprints:blueprint_v2_statetransfer>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`StateTransfer_DeleteAttachments <doc_item_asset_blueprints:blueprint_v2_statetransfer_deleteattachments>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Type <doc_item_asset_blueprints:blueprint_v2_type>`
     - :ref:`EBlueprintType <doc_item_asset_blueprints:eblueprinttype_enumeration>`
     - Deprecated.
   * - :ref:`VisibleWithUnmetConditions <doc_item_asset_blueprints:blueprint_v2_visiblewithunmetconditions>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``

.. _doc_item_asset_blueprints:eblueprintoperation_enumeration:

EBlueprintOperation Enumeration
```````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``None``
     - No special modification.
   * - ``RepairTargetItem``
     - Restore target item to full quality.
   * - ``FillTargetItem``
     - Transfer amount from first input item to target item.

----

.. _doc_item_asset_blueprints:blueprint_v2_categorytag:

CategoryTag :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_tag`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Determines which category the blueprint appears under in the crafting menu. Enables the creation of custom categories.

This replaces the ``Type`` property which acted as both a hardcoded category and modified behavior of crafting.

----

.. _doc_item_asset_blueprints:blueprint_v2_conditions:

Conditions :ref:`doc_npc_asset_conditions`
::::::::::::::::::::::::::::::::::::::::::

NPC conditions which must be met before the blueprint can be crafted.

.. note:: By default, the blueprint will be hidden until all of the conditions are met. If you have configured display text for your conditions you can enable :ref:`VisibleWithUnmetConditions <doc_item_asset_blueprints:blueprint_v2_visiblewithunmetconditions>`.

----

.. _doc_item_asset_blueprints:blueprint_v2_effect:

Effect :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_effect`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

An effect to play upon successfully crafting.

----

.. _doc_item_asset_blueprints:blueprint_v2_inputitems:

InputItems :ref:`list <doc_data_file_format>` of :ref:`doc_item_asset_blueprints_inputitem`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Required ingredients/supplies needed to craft this blueprint.

----

.. _doc_item_asset_blueprints:blueprint_v2_map:

Map :ref:`string <doc_data_builtin_types>` ``""``
:::::::::::::::::::::::::::::::::::::::::::::::::

Name of a map that this blueprint is restricted to. The blueprint will only be visible while on this map. For other maps, the blueprint is hidden from view.

----

.. _doc_item_asset_blueprints:blueprint_v2_name:

Name :ref:`string <doc_data_builtin_types>` ``""``
::::::::::::::::::::::::::::::::::::::::::::::::::

Optional case-sensitive identifier in list of blueprints. Can be used, for example, to reference this blueprint from a context menu action or a list of prohibited blueprints.

----

.. _doc_item_asset_blueprints:blueprint_v2_operation:

Operation :ref:`EBlueprintOperation <doc_item_asset_blueprints:eblueprintoperation_enumeration>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Controls what blueprint does with input items.

----

.. _doc_item_asset_blueprints:blueprint_v2_outputitems:

OutputItems :ref:`list <doc_data_file_format>` of :ref:`doc_item_asset_blueprints_outputitem`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Items created by this blueprint.

----

.. _doc_item_asset_blueprints:blueprint_v2_requiresnearbycraftingtags:

RequiresNearbyCraftingTags :ref:`list <doc_data_file_format>` of :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`doc_assets_tag`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:ref:`doc_assets_tag` that must be available from nearby crafting tag providers (workstations).

For example, to require both Chemical Mixing and Workbench:

.. code-block:: unturneddat

	RequiresNearbyCraftingTags
	[
		// Chemical Mixing
		99896da563a748148460c67b9962874f

		// Workbench
		7b82c125a5a54984b8bb26576b59e977
	]

----

.. _doc_item_asset_blueprints:blueprint_v2_rewards:

Rewards :ref:`doc_npc_asset_rewards`
::::::::::::::::::::::::::::::::::::

NPC rewards granted when crafting this blueprint.

----

.. _doc_item_asset_blueprints:blueprint_v2_searchable:

Searchable :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When ``true``, this blueprint is visible in the search results even when the player lacks the required items. This property can be used to hide blueprints intended for debugging that are not acquirable through normal gameplay.

----

.. _doc_item_asset_blueprints:blueprint_v2_skill:

Skill :ref:`EBlueprintSkill <doc_item_asset_blueprints:eblueprintskill_enumeration>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

The player must have leveled the specified skill in order to craft this blueprint. This property is used in conjunction with ``Skill_Level``.

----

.. _doc_item_asset_blueprints:blueprint_v2_skill_level:

Skill_Level :ref:`int32 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

If the blueprint requires a skill, its level must be greater than or equal to this value. This property is used in conjunction with ``Skill``.

----

.. _doc_item_asset_blueprints:blueprint_v2_statetransfer:

StateTransfer :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Transfer the current state the first input item to the product, when applicable. For example, some states that can be transferred include: amount (e.g., rounds in an ammunition box), quality percentage, selected firing mode, or fuel units (e.g., from a gas can).

----

.. _doc_item_asset_blueprints:blueprint_v2_statetransfer_deleteattachments:

StateTransfer_DeleteAttachments :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true`` and ``StateTransfer`` is enabled, any output guns will have all of their attachments deleted.

----

.. _doc_item_asset_blueprints:blueprint_v2_type:

Type :ref:`EBlueprintType <doc_item_asset_blueprints:eblueprinttype_enumeration>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Should not be used. Type acted as both a hardcoded category and modified behavior of crafting. These have been separated into the ``CategoryTag`` and ``Operation`` properties instead.

----

.. _doc_item_asset_blueprints:blueprint_v2_visiblewithunmetconditions:

VisibleWithUnmetConditions :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, blueprint can become visible in the crafting list even when NPC conditions are not met. This should typically only be enabled if all conditions are configured to be visible in the details panel. Otherwise, the default "conditions unmet" label isn't very informative for players.