.. _doc_item_asset_sight:

Sight Assets
============

Sight attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Sight``)

**ID** *uint16*: Must be a unique identifier.

Sight Asset Properties
----------------------

**Holographic** *flag*: Specified if sight is holographic.

**Nightvision_Color** :ref:`color <doc_data_file_format>`: Overrides the default color when using ``Vision Military``. When using the legacy color parsing, the ``_R``, ``_G``, and ``_B`` keys are unsigned bytes. The default value for ``Vision Civilian`` is equivalent to #666666. The default value for ``Vision Military`` is equivalent to #507814.

**Nightvision_Fog_Intensity** *float*: Intensity of fog while nightvision is active. Default value for ``Vision Civilian`` is 0.5. Default value for ``Vision Military`` is 0.25.

**Vision** *enum* (``None``, ``Military``, ``Civilian``): Type of unique lighting vision effect to use. Defaults to "None". Use the "Military" enumerator when intending to assign a custom nightvision color via the color component properties.

**Zoom** *float*: Multiplicative amount of zoom. Should be set to a value greater than 1. Defaults to 1.

**Zoom\_Using\_Eyes** *bool*: Whether main camera field of view should zoom without scope camera / scope overlay.
