.. _doc_data_vector3:

Vector3
=======

**Vector3** (or "3D vectors") can either be parsed as a single value containing three :ref:`floats <doc_data_builtin_types>` (optionally surrounded by parenthesis), or from a dictionary with ``X``, ``Y``, and ``Z`` keys.

For example, all three of these would be valid 3D vectors:

.. code-block:: text
	
	Position 1, 2, 3
	Offset (4, 5, 6)
	Scale
	{
		X 7
		Y 8
		Z 9
	}

Legacy Parsing
--------------

Some older properties have support for the vector3 data type, but can alternatively be written using the legacy method of three separate :ref:`float32 <doc_data_builtin_types>` properties. Namely,  the ``LOD_Center``, ``LOD_Size``, ``Explosion_Min_Force``, ``Explosion_Max_Force``, and ``Center_Of_Mass`` properties have support for both.

For example, this would be valid for an older property that supports the legacy format:

.. code-block:: text
	
	LOD_Size_X 0
	LOD_Size_Y -12
	LOD_Size_Z -1