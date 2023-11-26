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

**Nightvision_Allowed_In_ThirdPerson** *bool*: If ``true``, nightvision works in third-person, not just first-person. Defaults to ``false`` for backwards compatibility. Vanilla nightvision has this set to true.

**Nightvision_Color** :ref:`color <doc_data_file_format>`: Overrides the default color when using ``Vision Military``. This property supports using legacy color parsing.

**Nightvision_Fog_Intensity** *float*: Intensity of fog while nightvision is active.

**Vision** *enum* (``None``, ``Military``, ``Civilian``, ``Headlamp``): Type of unique lighting vision effect to use. Defaults to ``None``. When intending to assign a custom nightvision color via the ``Nightvision_Color`` property, it is recommended to use the ``Military`` enumerator.