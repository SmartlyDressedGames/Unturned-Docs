.. _doc_data_eassettype:

EAssetType
============

The EAssetType enumerated type is used as a scope for legacy IDs. Each legacy ID is unique within an EAssetType (allowing multiple assets to share the same legacy ID when they are different types). This is only used in older code or for maintaining backwards compatibility.

Enumerators
```````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``None``
     - Asset type is not applicable.
   * - ``Item``
     - Asset is an item.
   * - ``Effect``
     - Asset is an effect.
   * - ``Object``
     - Asset is an object (this includes NPC characters).
   * - ``Resource``
     - Asset is a resource.
   * - ``Vehicle``
     - Asset is a vehicle.
   * - ``Animal``
     - Asset is an animal.
   * - ``Mythic``
     - Asset is a mythical effect.
   * - ``Skin``
     - Asset is a skin.
   * - ``Spawn``
     - Asset is a spawn table.
   * - ``NPC``
     - Asset is related to NPCs (such as quests, vendors, or dialogues).
