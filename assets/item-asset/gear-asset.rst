.. _doc_item_asset_gear:

Gear Assets
===========

Clothing gear can be worn by players and zombies. The inherited Hair_Visible and Beard_Visible properties default to the gear asset's corresponding Hair and Beard flag properties.

This inherits the :ref:`ClothingAsset <doc_item_asset_clothing>` class.

Gear Asset Properties
---------------------

**Hair** *flag*: Specified if hair should be visible.

**Beard** *flag*: Specified if facial hair should be visible.

**Hair_Override** *string*: Optional name of a renderer that should use the player's hair material. Used by hats which entirely cover the player's hair so that the hair color can still be used for customization.
