.. _doc_item_asset_vest:

Vest Assets
===========

The ItemVestAsset class is used by clothing items occupying the "vest" slot. Vests can be worn by players and zombies, and cover their torso.

Game Data File
--------------

The ItemVestAsset class inherits properties from the :ref:`ItemBagAsset <doc_item_asset_bag>` class. Properties that are required (or recommended) are listed in the table below.

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
     - ``Vest``
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Useable <doc_item_asset_intro:useable>`
     - ``Clothing``

Properties
``````````

Vests have no unique properties. Refer to parent classes for additional properties instead.