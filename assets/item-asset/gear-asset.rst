.. _doc_item_asset_gear:

Gear Assets
===========

Clothing gear can be worn by players and zombies. The inherited Hair_Visible and Beard_Visible properties default to the gear asset's corresponding Hair and Beard flag properties.

This inherits the :ref:`ClothingAsset <doc_item_asset_clothing>` class.

Gear Asset Properties
---------------------

**Hair** *flag*: Specified if hair should be visible.

**Beard** *flag*: Specified if facial hair should be visible.

**Hair_Override** *string*: When this property is set, the game will look for a child Mesh Renderer component in Unity that has the same name as this property's value. If a matching Mesh Renderer is found, its material will be changed to the character's hair material. This property is used by certain cosmetics that entirely cover the character's hair, so that the player's selected hair color can still be used for customization.