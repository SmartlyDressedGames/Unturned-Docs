.. _doc_data_eobjectchart:

EObjectChart
============

The EObjectChart enumerated type is used to determine the how an asset should appear when generating a map's chart view. Most of the enumerators corresponds to a specific pixel coordinate on either the Height_Strip or Layer_Strip of a map's :ref:`Charts.unity3d file <doc_mapping_charts>`.

Enumerators
```````````

**NONE**: Use the default for this asset.

**GROUND**: Use (20, 0) from the Height_Strip.

**IGNORE**: Skip this asset, and use whatever is underneath.

**HIGHWAY**: Use (0, 0) from the Layer_Strip.

**ROAD**: Use (1, 0) from the Layer_Strip.

**STREET**: Use (2, 0) from the Layer_Strip.

**PATH**: Use (3, 0) from the Layer_Strip.

**LARGE**: Use (15, 0) from the Layer_Strip.

**MEDIUM**: Use (16, 0) from the Layer_Strip.

**WATER**: Use (0, 0) from the Height_Strip.

**CLIFF**: Use (4, 0) from the Layer_Strip.