.. _doc_item_asset_actions:

Actions
=======

Context actions appear when a player right-clicks an item from their inventory menu. Some items may have set a of automatically-generated context actions, but additional context actions can be added to any item. The system currently supports adding additional :ref:`blueprint <doc_item_asset_blueprints>` actions.

Depending on an item's configuration, the game may automatically add context actions for various actions.

Game Data File
--------------

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Action_#_Blueprint_#_Index <doc_item_asset_actions:action_blueprint_index>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Action_#_Blueprint_#_Link <doc_item_asset_actions:action_blueprint_link>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Action_#_Blueprints <doc_item_asset_actions:action_blueprints>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``
   * - :ref:`Action_#_Key <doc_item_asset_actions:action_key>`
     - :ref:`string <doc_data_builtin_types>`
     - 
   * - :ref:`Action_#_Source <doc_item_asset_actions:action_source>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``uint16``
   * - :ref:`Action_#_Text <doc_item_asset_actions:action_text>`
     - :ref:`string <doc_data_builtin_types>`
     - 
   * - :ref:`Action_#_Tooltip <doc_item_asset_actions:action_tooltip>`
     - :ref:`string <doc_data_builtin_types>`
     - 
   * - :ref:`Action_#_Type <doc_item_asset_actions:action_type>`
     - :ref:`EActionType <doc_item_asset_actions:eactiontype>`
     - 
   * - :ref:`Actions <doc_item_asset_actions:actions>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``0``

.. _doc_item_asset_actions:eactiontype:

EActionType Enumeration
```````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Named Value
     - Description
   * - ``Blueprint``
     - Action is linked a crafting blueprint.

Property Descriptions
`````````````````````

.. _doc_item_asset_actions:action_blueprint_index:

Action_#_Blueprint_#_Index :ref:`uint8 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Index of the blueprint that action should perform.

----

.. _doc_item_asset_actions:action_blueprint_link:

Action_#_Blueprint_#_Link :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Action should redirect to the associated blueprint listing in the crafting menu, rather than immediately craft the item.

----

.. _doc_item_asset_actions:action_blueprints:

Action_#_Blueprints :ref:`uint8 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Total number of blueprint indices.

----

.. _doc_item_asset_actions:action_key:

Action_#_Key :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::

Translation key that should be used instead of a custom button name and tooltip. Valid translation keys and their localization can be found in the ``PlayerDashboardInventory.dat`` localization file.

Valid keys include: ``Attachments``, ``Craft_Bandage``, ``Craft_Dressing``, ``Craft_Rag``, ``Craft_Seed``, ``Dequip``, ``Drop``, ``Equip``, ``Pickup``, ``Refill``, ``Repair``, ``Salvage``, ``Store``, and ``Take``.

This property cannot be used in combination with ``Action_#_Text`` or ``Action_#_Tooltip``. If set, the value of this property will always override any custom button name or tooltip that has been set.

----

.. _doc_item_asset_actions:action_source:

Action_#_Source :ref:`uint16 <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ID of the item to source actions from. Default source is the current item.

----

.. _doc_item_asset_actions:action_text:

Action_#_Text :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::

Context button name. This property is usually used in combination with ``Action_#_Tooltip``.

----

.. _doc_item_asset_actions:action_tooltip:

Action_#_Tooltip :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

Context button tooltip. This property is usually used in combination with ``Action_#_Text``.

----

.. _doc_item_asset_actions:action_type:

Action_#_Type :ref:`EActionType <doc_item_asset_actions:eactiontype>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Type of action to perform. Currently, only the ``Blueprint`` action type exists.

----

.. _doc_item_asset_actions:actions:

Actions :ref:`int <doc_data_builtin_types>` ``1``
:::::::::::::::::::::::::::::::::::::::::::::::::

Total number of context actions.

Default Actions
---------------

Depending on the blueprints an item has, some blueprint actions may be automatically added to the item as well. These actions will be linked to the blueprint they were automatically generated from.

- When a blueprint only has one supply, with a supply ID of the item itself, an action using the ``Salvage`` localization key is generated.
- When a blueprint uses the ``Repair`` type, an action using the ``Repair`` localization key is generated.
- When a blueprint uses the ``Refill`` type, an action using the ``Refill`` localization key is generated.