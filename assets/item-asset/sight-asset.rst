.. _doc_item_asset_sight:

Sight Assets
============

Sight attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Item Asset Properties
`````````````````````

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Sight``)

**ID** *uint16*: Must be a unique identifier.

Sight Asset Properties
``````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 0

   * - **DistanceMarkers**
     - *list of dictionaries*
     - n/a
   * - **Holographic**
     - *flag*
     - n/a
   * - **Nightvision_Color**
     - :ref:`color <doc_data_file_format>`
     - See description
   * - **Nightvision_Fog_Intensity**
     - *float*
     - See description
   * - **Offset_Scope_Overlay_By_One_Texel**
     - *bool*
     - ``false``
   * - **Vision**
     - *enum* (``None``, ``Military``, ``Civilian``)
     - ``None``
   * - **Zoom**
     - *float*
     - ``1``
   * - **ThirdPerson_Zoom**
     - *float*
     - ``1.25``
   * - **Zoom_Using_Eyes**
     - *bool*
     - ``false``

Property Descriptions
`````````````````````

DistanceMarkers *list of dictionaries*
::::::::::::::::::::::::::::::::::::::

.. note:: Display-related properties like **LineOffset** and **LineWidth** are a 0-1 percentage of the scope size to keep them consistent between 2D and 3D. For example 0.25 is 25%.

- **Distance** *float*: Meters between player and target.
- **LineOffset** *float*: Distance between center line and start of horizontal line marker.
- **LineWidth** *float*: Length of horizontal line marker. Defaults to 0.05.
- **Side** *enum* (``Left`` or ``Right``): Direction the horizontal line and text expand in. Defaults to Right.
- **HasLabel** *bool*: If true, a label with **Distance** text is shown next to the horizontal line marker. Defaults to true.
- **Color** :ref:`color <doc_data_file_format>`: Horizontal line and text color. Defaults to black.

Holographic *flag*
::::::::::::::::::::::::::::

Specified if sight is holographic.

Nightvision_Color :ref:`color <doc_data_file_format>` = See description
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the default color when using ``Vision Military``. When using the legacy color parsing, the ``_R``, ``_G``, and ``_B`` keys are unsigned bytes. The default value for ``Vision Civilian`` is equivalent to ``#666666``. The default value for ``Vision Military`` is equivalent to ``#507814``.

Nightvision_Fog_Intensity *float* = See description
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Intensity of fog while nightvision is active. Default value for ``Vision Civilian`` is ``0.5``. Default value for ``Vision Military`` is ``0.25``.

Offset_Scope_Overlay_By_One_Texel *bool* = ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, 2D scope texture will be scaled up slightly to center the pixel that would otherwise be left of center. For example when enabled with a 512x512 texture the pixel at 255x255 will be centered on the display.

Vision *enum* (``None``, ``Military``, ``Civilian``) = ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Type of unique lighting vision effect to use. Use the "Military" enumerator when intending to assign a custom nightvision color via the color component properties.

Zoom *float* = ``1``
::::::::::::::::::::

Multiplicative amount of zoom. Should be set to a value greater than 1.

ThirdPerson_Zoom *float* = ``1.25``
:::::::::::::::::::::::::::::::::::

Zoom factor in third-person perspective. Should be set to a value greater than 1.

Zoom_Using_Eyes *bool* = ``false``
::::::::::::::::::::::::::::::::::

Whether main camera field of view should zoom without scope camera / scope overlay.