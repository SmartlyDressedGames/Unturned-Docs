.. _doc_item_asset_glasses:

Glasses Assets
==============

Glasses can be worn by players and zombies.

This inherits the :ref:`GearAsset <doc_item_asset_gear>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Glasses``)

**Useable** *enum* (``Clothing``)

**ID** *uint16*: Must be a unique identifier.

Glasses Asset Properties
------------------------

**Blindfold** *flag*: Specified if glasses should blacken the player's screen.

**Nightvision_Color** :ref:`color <doc_data_file_format>`: Overrides the default color when using ``Vision Military``. When using the legacy color parsing, the ``_R``, ``_G``, and ``_B`` keys are unsigned bytes. The default value for ``Vision Civilian`` is equivalent to #666666. The default value for ``Vision Military`` is equivalent to #507814.

**Nightvision_Fog_Intensity** *float*: Intensity of fog while nightvision is active. Default value for ``Vision Civilian`` is 0.5. Default value for ``Vision Military`` is 0.25.

**Vision** *enum* (``None``, ``Military``, ``Civilian``, ``Headlamp``): Type of unique lighting vision effect to use. Defaults to "None". Use the "Military" enumerator when intending to assign a custom nightvision color via the color component properties.
