.. _doc_item_asset_structure:

Structure Assets
================

.. attention::
	Structure assets are not properly documented yet. Some of the information here may be slightly outdated, and most properties are undocumented.

Structures can be placed by players. Some structure pieces require another structure piece in order to be placed.

This inherits the :ref:`PlaceableAsset <doc_item_asset_placeable>` class.

Structure Asset Properties
--------------------------

**Explosion** *uint16* or *GUID*: ID or GUID of effect to play when destroyed.

**Terrain_Test_Height** *float*: Length of raycast downward from pivot to check floor is above terrain. Vanilla floors can be placed a maximum of 10 meters above terrain.
