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

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`DistanceMarkers <doc_item_asset_sight_property_distancemarkers>`
     - :ref:`list of DistanceMarker <doc_data_item_asset_sight_distancemarker_dictionary_descriptions>`
     - n/a
   * - :ref:`Holographic <doc_item_asset_sight_property_holographic>`
     - :ref:`flag <doc_data_flag>`
     - n/a
   * - :ref:`Nightvision_Color <doc_item_asset_sight_property_nightvision_color>`
     - :ref:`color <doc_data_file_format>`
     - See description
   * - :ref:`Nightvision_Fog_Intensity <doc_item_asset_sight_property_nightvision_fog_intensity>`
     - :ref:`float <doc_data_builtin_types>`
     - See description
   * - :ref:`Offset_Scope_Overlay_By_One_Texel <doc_item_asset_sight_property_offset_scope_overlay_by_one_texel>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Vision <doc_item_asset_sight_property_vision>`
     - :ref:`ELightingVision <doc_data_elightingvision>`
     - ``None``
   * - :ref:`Zoom <doc_item_asset_sight_property_zoom>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`ThirdPerson_Zoom <doc_item_asset_sight_property_thirdperson_zoom>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1.25``
   * - :ref:`Zoom_Using_Eyes <doc_item_asset_sight_property_zoom_using_eyes>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``

DistanceMarker Dictionary
`````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Distance <doc_data_item_asset_sight_distancemarker_distance>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`LineOffset <doc_data_item_asset_sight_distancemarker_lineoffset>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`LineWidth <doc_data_item_asset_sight_distancemarker_linewidth>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0.05``
   * - :ref:`Side <doc_data_item_asset_sight_distancemarker_side>`
     - :ref:`ESide <doc_data_item_asset_sight_eside_enumeration>`
     - ``Right``
   * - :ref:`HasLabel <doc_data_item_asset_sight_distancemarker_haslabel>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Color <doc_data_item_asset_sight_distancemarker_color>`
     - :ref:`color <doc_data_file_format>`
     - ``black``

.. _doc_data_item_asset_sight_eside_enumeration:

ESide Enumeration
`````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Named Value
     - Description
   * - ``Left``
     - Marking extends to the left from the center.
   * - ``Right``
     - Marking extends to the right from the center.

Property Descriptions
`````````````````````

.. _doc_item_asset_sight_property_distancemarkers:

DistanceMarkers :ref:`list of DistanceMarker <doc_data_item_asset_sight_distancemarker_dictionary_descriptions>`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property is a list of DistanceMarker dictionaries. It can be used to add visible (and accurate) distance markers to the scope that account for the weapon's bullet drop.

----

.. _doc_item_asset_sight_property_holographic:

Holographic :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::::::::::

This sight should be holographic.

----

.. _doc_item_asset_sight_property_nightvision_color:

Nightvision_Color :ref:`color <doc_data_file_format>` (See description)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Overrides the default color when using ``Vision Military``. This property supports using legacy color parsing.

----

.. _doc_item_asset_sight_property_nightvision_fog_intensity:

Nightvision_Fog_Intensity :ref:`float <doc_data_builtin_types>` (See description)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Intensity of fog while nightvision is active.

----

.. _doc_item_asset_sight_property_offset_scope_overlay_by_one_texel:

Offset_Scope_Overlay_By_One_Texel :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, 2D scope texture will be scaled up slightly to center the pixel that would otherwise be left of center. For example when enabled with a 512x512 texture the pixel at 255x255 will be centered on the display.

----

.. _doc_item_asset_sight_property_vision:

Vision :ref:`ELightingVision <doc_data_elightingvision>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Type of unique lighting vision effect to use. Use the ``Military`` enumerator when intending to assign a custom nightvision color via the ``Nightvision_Color`` property. The ``Headlamp`` enumerator is not supported by this property.

----

.. _doc_item_asset_sight_property_zoom:

Zoom :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Multiplicative amount of zoom. Should be set to a value greater than 1.

----

.. _doc_item_asset_sight_property_thirdperson_zoom:

ThirdPerson_Zoom :ref:`float <doc_data_builtin_types>` ``1.25``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Zoom factor in third-person perspective. Should be set to a value greater than 1.

----

.. _doc_item_asset_sight_property_zoom_using_eyes:

Zoom_Using_Eyes :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether main camera field of view should zoom without scope camera / scope overlay.

.. _doc_data_item_asset_sight_distancemarker_dictionary_descriptions:

DistanceMarker Dictionary Descriptions
``````````````````````````````````````

.. tip:: Display-related properties like **LineOffset** and **LineWidth** are a 0-1 percentage of the scope size to keep them consistent between 2D and 3D. For example, ``0.25`` would be 25%. This information should probably be moved out of this tip, and into the descriptions below.

.. _doc_data_item_asset_sight_distancemarker_distance:

Distance :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Meters between player and target.

----

.. _doc_data_item_asset_sight_distancemarker_lineoffset:

LineOffset :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Distance between center line and start of horizontal line marker.

----

.. _doc_data_item_asset_sight_distancemarker_linewidth:

LineWidth :ref:`float <doc_data_builtin_types>` ``0.05``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Length of horizontal line marker.

----

.. _doc_data_item_asset_sight_distancemarker_side:

Side :ref:`ESide <doc_data_item_asset_sight_eside_enumeration>` ``Right``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Direction the horizontal line and text expand in.

----

.. _doc_data_item_asset_sight_distancemarker_haslabel:

HasLabel :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, a label with ``Distance`` text is shown next to the horizontal line marker.

----

.. _doc_data_item_asset_sight_distancemarker_color:

Color :ref:`color <doc_data_file_format>` ``black``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Horizontal line and text color.