.. _doc_data_eassettype:

EAssetType
==========

The EAssetType enumerated type is used as a scope for legacy IDs. Each legacy ID is unique within an EAssetType (allowing multiple assets to share the same legacy ID when they are different types). This is only used in older code or for maintaining backwards compatibility.

Enumerators
```````````

.. list-table::
   :widths: 20 10 70
   :header-rows: 1

   * - Named Value
     - Index
     - Description
   * - ``None``
     - 0
     - Asset type is not applicable.
   * - ``Item``
     - 1
     - Asset is an item.
   * - ``Effect``
     - 2
     - Asset is an effect.
   * - ``Object``
     - 3
     - Asset is an object (this includes NPC characters).
   * - ``Resource``
     - 4
     - Asset is a resource.
   * - ``Vehicle``
     - 5
     - Asset is a vehicle.
   * - ``Animal``
     - 6
     - Asset is an animal.
   * - ``Mythic``
     - 7
     - Asset is a mythical effect.
   * - ``Skin``
     - 8
     - Asset is a skin.
   * - ``Spawn``
     - 9
     - Asset is a spawn table.
   * - ``NPC``
     - 10
     - Asset is related to NPCs (such as quests, vendors, or dialogues).
