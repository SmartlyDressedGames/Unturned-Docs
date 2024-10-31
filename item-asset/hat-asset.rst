.. _doc_item_asset_hat:

Hat Assets
==========

The ItemHatAsset class is used by clothing items occupying the "hat" slot. Hats can be worn by players and zombies, and cover their head.

Game Data File
--------------

The ItemHatAsset class inherits properties from the :ref:`ItemGearAsset <doc_item_asset_gear>` class. Properties that are required (or recommended) are listed in the table below.

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
     - ``Hat``
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Useable <doc_item_asset_intro:useable>`
     - ``Clothing``

Properties
``````````

Hats have no unique properties. Refer to parent classes for additional properties instead.