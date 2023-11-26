.. _doc_data_elightingvision:

ELightingVision
===============

The ELightingVision enumerated type is used to determine the lighting conditions when using certain items, such as :ref:`glasses <doc_item_asset_glasses>`. Some assets may only support using specific enumerators.

Enumerators
```````````

.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Named Value
     - Description
   * - ``None``
     - There is no vision effect, and normal lighting is used.
   * - ``Military``
     - "Military" nightvision lighting is used. When supported by the asset, nightvision color is ``#507814``, and nightvision fog intensity is ``0.25``.
   * - ``Civilian``
     - "Civilian" nightvision lighting is used. When supported by the asset, nightvision color is ``#666666``, and nightvision fog intensity is ``0.5``.
   * - ``Headlamp``
     - "Headlamp" lighting is used. When supported by the asset, this will enable a toggleable light source and allow for using :ref:`PlayerSpotLightConfig <doc_data_playerspotlightconfig>` properties.