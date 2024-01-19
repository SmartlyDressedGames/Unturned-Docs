.. _doc_item_asset_sight:

Sight Assets
============

Sight attachments are inventory items that can be attached to ranged weapons.

This inherits the :ref:`CaliberAsset <doc_item_asset_caliber>` class.

Game Data File
--------------

Sight attachments inherit properties from the CaliberAsset class, which in turn inherits properties from the ItemAsset class. Properties that are required to be included are listed in the table below.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1
   
   * - Class
     - Property Name
     - Required Value
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`GUID <doc_item_asset_intro:guid>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`ID <doc_item_asset_intro:id>`
     - 
   * - :ref:`ItemAsset <doc_item_asset_intro>`
     - :ref:`Type <doc_item_asset_intro:type>`
     - ``Sight``

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`DistanceMarkers <doc_item_asset_sight:distancemarkers>`
     - :ref:`list of DistanceMarker <doc_item_asset_sight:distancemarker_dictionary_descriptions>`
     - 
   * - :ref:`Holographic <doc_item_asset_sight:holographic>`
     - :ref:`flag <doc_data_flag>`
     - 
   * - :ref:`Nightvision_Color <doc_item_asset_sight:nightvision_color>`
     - :ref:`color <doc_data_file_format>`
     - See description
   * - :ref:`Nightvision_Fog_Intensity <doc_item_asset_sight:nightvision_fog_intensity>`
     - :ref:`float <doc_data_builtin_types>`
     - See description
   * - :ref:`Offset_Scope_Overlay_By_One_Texel <doc_item_asset_sight:offset_scope_overlay_by_one_texel>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Vision <doc_item_asset_sight:vision>`
     - :ref:`ELightingVision <doc_data_elightingvision>`
     - ``None``
   * - :ref:`Zoom <doc_item_asset_sight:zoom>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1``
   * - :ref:`ThirdPerson_Zoom <doc_item_asset_sight:thirdperson_zoom>`
     - :ref:`float <doc_data_builtin_types>`
     - ``1.25``
   * - :ref:`Zoom_Using_Eyes <doc_item_asset_sight:zoom_using_eyes>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``

.. _doc_item_asset_sight:distancemarker_dictionary:

DistanceMarker Dictionary
`````````````````````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1
   
   * - Property Name
     - Type
     - Default Value
   * - :ref:`Distance <doc_item_asset_sight:distancemarker_distance>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`LineOffset <doc_item_asset_sight:distancemarker_lineoffset>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0``
   * - :ref:`LineWidth <doc_item_asset_sight:distancemarker_linewidth>`
     - :ref:`float <doc_data_builtin_types>`
     - ``0.05``
   * - :ref:`Side <doc_item_asset_sight:distancemarker_side>`
     - :ref:`ESide <doc_item_asset_sight:eside_enumeration>`
     - ``Right``
   * - :ref:`HasLabel <doc_item_asset_sight:distancemarker_haslabel>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`Color <doc_item_asset_sight:distancemarker_color>`
     - :ref:`color <doc_data_file_format>`
     - ``black``

.. _doc_item_asset_sight:eside_enumeration:

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

.. _doc_item_asset_sight:distancemarkers:

DistanceMarkers :ref:`list of DistanceMarker <doc_item_asset_sight:distancemarker_dictionary_descriptions>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property is a list of :ref:`DistanceMarker dictionaries <doc_item_asset_sight:distancemarker_dictionary>`. It can be used to add visible (and accurate) distance markers to the scope that account for the weapon's bullet drop.

----

.. _doc_item_asset_sight:holographic:

Holographic :ref:`flag <doc_data_flag>`
:::::::::::::::::::::::::::::::::::::::

This sight should be holographic.

----

.. _doc_item_asset_sight:nightvision_color:

Nightvision_Color :ref:`color <doc_data_color>`
:::::::::::::::::::::::::::::::::::::::::::::::

Override the default nightvision color. To configure this property, the ``Vision`` property must be set to ``Military``. This property supports using legacy color parsing. When not overridden, the default nightivision color will depend on the value of the :ref:`Vision <doc_item_asset_sight:vision>` property.

----

.. _doc_item_asset_sight:nightvision_fog_intensity:

Nightvision_Fog_Intensity :ref:`float <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Configure the intensity of fog while nightvision is active. When this property has not been configured, the default fog intensity will depend on the value of the :ref:`Vision <doc_item_asset_sight:vision>` property.

----

.. _doc_item_asset_sight:offset_scope_overlay_by_one_texel:

Offset_Scope_Overlay_By_One_Texel :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If ``true``, the 2D scope texture will be scaled up slightly to center the pixel that would otherwise be left of center. For example, when enabled with a 512×512 texture the pixel at 255×255 will be centered on the display.

----

.. _doc_item_asset_sight:vision:

Vision :ref:`ELightingVision <doc_data_elightingvision>` ``None``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Set a unique lighting vision effect to use. The value of this property may effect the default values of other properties. The ``Headlamp`` enumerator is not supported by this property.

----

.. _doc_item_asset_sight:zoom:

Zoom :ref:`float <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::

Multiplicative amount of zoom. This value must be equal to or greater than ``1``.

----

.. _doc_item_asset_sight:thirdperson_zoom:

ThirdPerson_Zoom :ref:`float <doc_data_builtin_types>` ``1.25``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Zoom factor while in the third-person perspective. This value must be equal to or greater than ``1``.

----

.. _doc_item_asset_sight:zoom_using_eyes:

Zoom_Using_Eyes :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Whether the main camera field of view should zoom without a scope overlay.

.. _doc_item_asset_sight:distancemarker_dictionary_descriptions:

DistanceMarker Dictionary Descriptions
``````````````````````````````````````

.. _doc_item_asset_sight:distancemarker_distance:

Distance :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Meters between the player and a hypothethical target.

----

.. _doc_item_asset_sight:distancemarker_lineoffset:

LineOffset :ref:`float <doc_data_builtin_types>` ``0``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

Distance between center line and start of horizontal line marker.

Display-related properties like ``LineOffset`` are a percentage (represented as a decimal value from 0 to 1). For example, ``0.25`` would be 25%.

----

.. _doc_item_asset_sight:distancemarker_linewidth:

LineWidth :ref:`float <doc_data_builtin_types>` ``0.05``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Length of horizontal line marker.

Display-related properties like ``LineWidth`` are a percentage (represented as a decimal value from 0 to 1). For example, ``0.25`` would be 25%.

----

.. _doc_item_asset_sight:distancemarker_side:

Side :ref:`ESide <doc_item_asset_sight:eside_enumeration>` ``Right``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Direction the horizontal line and text expand in.

----

.. _doc_item_asset_sight:distancemarker_haslabel:

HasLabel :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, a label with ``Distance`` text is shown next to the horizontal line marker.

----

.. _doc_item_asset_sight:distancemarker_color:

Color :ref:`color <doc_data_file_format>` ``black``
:::::::::::::::::::::::::::::::::::::::::::::::::::

Override the color of the horizontal line and text.