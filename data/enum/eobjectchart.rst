.. _doc_data_eobjectchart:

EObjectChart
============

The EObjectChart enumerated type is used to determine the how an asset should appear when generating a map's chart view. Most of the enumerators corresponds to a specific pixel coordinate on either the Height_Strip or Layer_Strip of a map's :ref:`Charts.unity3d file <doc_mapping_charts>`.

Enumerators
```````````

.. list-table::
   :widths: 25 75
   :header-rows: 1
   
   * - Named Value
     - Description
   * - ``None``
     - Use the default for this asset.
   * - ``Ground``
     - Use (20, 0) from the Height_Strip.
   * - ``Ignore``
     - Skip this asset, and use whatever is underneath.
   * - ``Highway``
     - Use (0, 0) from the Layer_Strip.
   * - ``Street``
     - Use (1, 0) from the Layer_Strip.
   * - ``Road``
     - Use (2, 0) from the Layer_Strip.
   * - ``Path``
     - Use (3, 0) from the Layer_Strip.
   * - ``Large``
     - Use (15, 0) from the Layer_Strip.
   * - ``Medium``
     - Use (16, 0) from the Layer_Strip.
   * - ``Water``
     - Use (0, 0) from the Height_Strip.
   * - ``Cliff``
     - Use (4, 0) from the Layer_Strip.