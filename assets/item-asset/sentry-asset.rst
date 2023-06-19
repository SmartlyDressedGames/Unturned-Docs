.. _doc_item_asset_sentry:

Sentry Assets
=============

Sentries (localized as "robotic turrets") are placeables that can automatically detect, track, and attack target under certain conditions. Storing a ranged weapon inside a sentry allows it to use that weapon when attacking target.

This inherits the :ref:`StorageAsset <doc_item_asset_storage>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Sentry``)

**Useable** *enum* (``Barricade``)

**Build** *enum* (``Sentry``)

**ID** *uint16*: Must be a unique identifier.

Sentry Asset Properties
-----------------------

**Detection_Radius** *float*: Radius for initially detecting targets, in meters. Defaults to 48.

**Mode** *enum* (``Friendly``, ``Neutral``, ``Hostile``): The sentry's "Mode" determines what the sentry considers a valid target. Defaults to ``Mode Neutral``.

**Infinite_Ammo** *bool*: Whether or not the magazine attachments in the stored ranged weapon should be depleted during use. If true, the ranged weapon has infinite ammo and any attached magazine attachment will not be depleted during use. Defaults to false.

**Infinite_Quality** *bool*: Whether or not the stored ranged weapon should degrade during use. If true, the ranged weapon's quality will not degrade during use. Defaults to false.

**Requires_Power** *bool*: Whether or not the sentry requires power from a generator. If true, the sentry must be powered in order for it to detect, track, and attack targets. Defaults to true.

**Target_Acquired_Effect** :ref:`Asset Pointer <doc_data_assetptr>`: The audio effect played when a target is detected. Defaults to ab5f0056b54545c8a051159659da8bea.

**Target_Lost_Effect** :ref:`Asset Pointer <doc_data_assetptr>`: The audio effect played when a target is no longer detected. Defaults to 288b98b718084699ba3653c592e57803.

**Target_Loss_Radius** *float*: Radius for continuing to track targets after they have left the initial detection radius, in meters. Defaults to ``Detection_Radius * 1.2f`` (i.e., 20% higher than ``Detection_Radius``).