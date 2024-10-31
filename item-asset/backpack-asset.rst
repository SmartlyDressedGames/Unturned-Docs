.. _doc_item_asset_backpack:

Backpack Assets
===============

The ItemBackpackAsset class is used by clothing items occupying the "backpack" slot. Backpacks can be worn by players and zombies.

Game Data File
--------------

The ItemBackpackAsset class inherits properties from the :ref:`ItemBagAsset <doc_item_asset_bag>` class. Properties that are required (or recommended) are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1
   
   * - Class
     - Property Name
     - Required Value
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`GUID <doc_item_asset_intro:guid>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`ID <doc_item_asset_intro:id>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Type <doc_item_asset_intro:type>`
     - ``Backpack``
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Useable <doc_item_asset_intro:useable>`
     - ``Clothing``

Some inherited properties behave differently when used by this class. Notably, these are:

#. | :ref:`Armor <doc_item_asset_clothing:armor>` (from :ref:`ItemClothingAsset <doc_item_asset_clothing>`). Backpacks do not cover any body part(s) when worn, so this property has no effect.

#. | :ref:`InventoryAudio <doc_item_asset_intro:inventoryaudio>` (from :ref:`ItemAsset <doc_item_asset_intro>`). Defaults to ``Sounds/Inventory/LightMetalEquipment.asset`` when :ref:`Width <doc_item_asset_bag:width>` or :ref:`Height <doc_item_asset_bag:height>` are less than ``3``. To ``Sounds/Inventory/MediumMetalEquipment.asset`` when less than ``6``. Otherwise, to ``Sounds/Inventory/HeavyMetalEquipment.asset``.

Properties
``````````

Backpacks have no unique properties. Refer to parent classes for additional properties instead.