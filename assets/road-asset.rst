.. _doc_assets_road:

Road Assets
===========

This asset allows roads to be shared between levels, and exposes some previously-unavailable properties for configuration.

Properties
----------

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Chart <doc_assets_road:chart>`
     - :ref:`doc_data_eobjectchart`
     - ``None``
   * - :ref:`Depth <doc_assets_road:depth>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`OffsetAlongNormal <doc_assets_road:offsetalongnormal>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`PhysicsMaterial <doc_assets_road:physicsmaterial>`
     - :ref:`string <doc_data_builtin_types>`
     - See description
   * - :ref:`RepeatDistanceScale <doc_assets_road:repeatdistancescale>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``1.0``
   * - :ref:`TexturePath <doc_assets_road:texturepath>`
     - :ref:`string <doc_data_builtin_types>`
     - See description
   * - :ref:`Width <doc_assets_road:width>`
     - :ref:`float32 <doc_data_builtin_types>`
     - ``0.0``
   * - :ref:`VanillaPhysicsMaterial <doc_assets_road:vanillaphysicsmaterial>`
     - :ref:`enum <doc_data_builtin_types>`
     - See description

----

.. _doc_assets_road:chart:

Chart :ref:`doc_data_eobjectchart` ``None``
:::::::::::::::::::::::::::::::::::::::::::

If not ``None``, overrides how road appears in chart generation.

If ``None`` (default) legacy classification is used:

- Concrete roads wider than 16 meters are ``Highway``.
- Other concrete roads are ``Road``.
- Non-concrete roads are ``Path``.

----

.. _doc_assets_road:depth:

Depth :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Total size along the up axis.

.. note:: If converting a legacy road configuration, please note that Depth shown in the legacy editor is actually *half* the total depth.

----

.. _doc_assets_road:offsetalongnormal:

DistanceAlongNormal :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Distance along the terrain surface normal to move each road vertex.

----

.. _doc_assets_road:physicsmaterial:

PhysicsMaterial :ref:`doc_data_masterbundleptr` to ``PhysicMaterial``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Unity ``PhysicMaterial`` to apply to road collider. Not used if :ref:`VanillaPhysicsMaterial <doc_assets_road:vanillaphysicsmaterial>` is assigned.

----

.. _doc_assets_road:repeatdistancescale:

RepeatDistanceScale :ref:`float32 <doc_data_builtin_types>` ``1.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

By default, Texture is uniformly scaled along the road according to its aspect ratio and the road's width. For example, if :ref:`Width <doc_assets_road:width>` is 8 meters and Texture is 256x128 pixels, the texture will repeat every 4 meters.

This property multiplies the distance along the road before the texture repeats.

.. note:: If converting a legacy road configuration, the repeat distance was the texture's height in pixels divided by the Height value. For example: a 64x64 pixel texture with Height of 2 would repeat every 32 meters. To calculate an equivalent RepeatDistanceScale, divide the legacy repeat distance by the road asset's Width.

----

.. _doc_assets_road:texturepath:

TexturePath :ref:`doc_data_masterbundleptr` to ``Texture2D``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If not specified, the game looks for a texture named ``Texture`` in the accompanying asset bundle.

----

.. _doc_assets_road:width:

Width :ref:`float32 <doc_data_builtin_types>` ``0.0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::

Total horizontal size before the road begins tapering off into the terrain.

.. note:: If converting a legacy road configuration, please note that Width shown in the legacy editor is actually *half* the total width.

----

.. _doc_assets_road:vanillaphysicsmaterial:

VanillaPhysicsMaterial :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Optional name of a built-in Unity ``PhysicMaterial`` to apply to road collider. For example, "Concrete_Static" or "Gravel_Static" for the legacy road physics materials.
