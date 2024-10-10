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
   * - :ref:`Blueprint_#_Supply_#_Amount <doc_item_asset_blueprints:blueprint_#_supply_#_amount>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Blueprint_#_Supply_#_Critical <doc_item_asset_blueprints:blueprint_#_supply_#_critical>`
     - :ref:`flag <doc_data_flag>`
     -
   * - :ref:`Blueprint_#_Supply_#_ID <doc_item_asset_blueprints:blueprint_#_supply_#_id>`
     - :ref:`uint16 <doc_data_builtin_types>`
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

Can also be set to a string "this" to use the owning item's legacy ID. Useful for salvaging blueprints to avoid accidentally writing the wrong ID.

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
