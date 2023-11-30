.. _doc_data_color:

Color
=====

**Colors** can either be parsed as a single hexadecimal value (optionally prefixed with ``#``), or from a dictionary with ``R``, ``G``, and ``B`` keys with :ref:`uint8 <doc_data_builtin_types>` values.

For example, all three of these would be valid colors:

.. code-block:: text
	
	SkyColor 0000ff
	GroundColor #00ff00
	FogColor
	{
		R 255
		G 0
		B 0
	}

Legacy Parsing
--------------

Some older properties have support for the color data type, but can alternatively be written using the legacy method of three separate :ref:`float32 <doc_data_builtin_types>` properties. Namely,  the ``Laser_Color`` and ``Nightvision_Color`` properties have support for both.

For example, this would be valid for an older property that supports the legacy format:

.. code-block:: text
	
	Laser_Color_R 0.5
	Laser_Color_G 1
	Laser_Color_B 0