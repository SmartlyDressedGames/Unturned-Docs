.. _doc_assets_mythical:

Mythical Effect Assets
======================

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Mythic``)

**ID** *uint16*: Must be a unique identifier.

.. note:: At the time of writing (2025-02-04) mythical effects aren't moddable, sorry! This document is primarily for item creators working on curated updates, as well as preparation for eventual open sourcing.

When testing, we recommend attaching your mythicals to some items' Effect transform in the editor and resetting the local transform. This helps visualize how they will appear in-game.

Unity Prefabs
-------------

**System_Area**: Instantiated multiple times to cover a larger area. Mythical shirts and pants attach them to character bones, and mythical vehicle skins attach them to several points on the surface. As such, this shouldn't rely on any specific orientation. Layer should be set to Enemy.

**System_Hook**: Attached to a cosmetic item's "Effect" prefab. Layer should be set to Enemy.

.. figure:: /img/EffectTransform.png

	Example "Effect" transform positioning and orientation.

For silly legacy reasons the orientation is rather unfortunate: +Z is the mythical's up direction and +Y is the mythical's forward direction.

**System_Third**: Attached to third-person weapon skin. Unlike for cosmetics, +Z is forward and +Y is up. It may be helpful to increase particle size to make them more visible over the shoulder. Emission typically uses a box of size 25x25x50 cm. Layer should be set to Item.

**System_First**: Attached to first-person weapon skin. Particles should be smaller than usual, and try to avoid the up direction to reduce blocking the player's aim. First-person particles are typically half the size, but use the same emission shape size as third-person. Layer should be set to Viewmodel.

Localization
------------

**Particle_Tag_Name** *string*: When a mythical item is crafted with this effect, this is the display name shown in the inventory.
