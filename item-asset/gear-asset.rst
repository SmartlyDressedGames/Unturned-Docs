.. _doc_item_asset_gear:

Gear Assets
===========

The ItemGearAsset class is a base class that other classes are derived from. It is unusable on its own.

Game Data File
--------------

The ItemGearAsset class inherits properties from the :ref:`ItemClothingAsset <doc_item_asset_clothing>` class.

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Beard <doc_item_asset_gear:beard>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Hair <doc_item_asset_gear:hair>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Hair_Override <doc_item_asset_gear:hair_override>`
     - :ref:`string <doc_data_builtin_types>`
     - 

Some inherited properties behave differently when used by this class. Notably, these are:

#. | :ref:`Beard_Visible <doc_item_asset_clothing:beard_visible>` (from :ref:`ItemClothingAsset <doc_item_asset_clothing>`). This property's default behavior is altered. Refer to this class's ``Beard`` property instead.

#. | :ref:`Hair_Visible <doc_item_asset_clothing:hair_visible>` (from :ref:`ItemClothingAsset <doc_item_asset_clothing>`). This property's default behavior is altered. Refer to this class's ``Hair`` property instead.

Property Descriptions
`````````````````````

.. _doc_item_asset_gear:beard:

Beard :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::

When this flag is not included, the parent class's :ref:`Beard_Visible <doc_item_asset_clothing:beard_visible>` property is set to false. This flag must be included if the character's facial hair should be visible.

----

.. _doc_item_asset_gear:hair:

Hair :ref:`flag <doc_data_flag>`
::::::::::::::::::::::::::::::::

When this flag is not included, the parent class's :ref:`Hair_Visible <doc_item_asset_clothing:hair_visible>` property is set to false. This flag must be included if the character's hair should be visible.

----

.. _doc_item_asset_gear:hair_override:

Hair_Override :ref:`string <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::::

When this property is set, the game will look for a child Mesh Renderer component in Unity that has the same name as this property's value. If a matching Mesh Renderer is found, its material will be changed to the character's hair material. This property is used by certain cosmetics that entirely cover the character's hair, so that the player's selected hair color can still be used for customization.