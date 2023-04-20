.. _doc_data_file_format:

Data File Format
================

This article describes the syntax of Unturned's ``.dat`` and ``.asset`` files.

Each line is a key-value pair separated by a space. The key and/or value can optionally be in quotes. For example:

.. code-block:: text

	Key1 First value
	"Key2 in quotes" Second value
	Key3 "Third value"

Will be parsed as:

.. code-block:: text

	"Key1" = "First value"
	"Key2 in quotes" = "Second value"
	"Key3" = "Third value"

The only reason to quote a value is to enable comments on the same line. Quotation marks within a quoted key/value can be escaped with a ``\`` backslash. For example ``"a \"b\" c"`` is parsed with quotation marks around ``b``. Keys support quotes in case a space is required, but no keys in the vanilla game use spaces.

.. note::

	Keys are case-insensitive. i.e., ``Use_Cool_Option true`` and ``UsE_cOoL_oPtIoN true`` are identical. Keys should be unique within their dictionary.

Flags
-----

Some older asset types look for the presence of a particular key, not its value. These are referred to as flags. Their value can be left empty.

For example: item assets check for the ``Pro`` flag marking them is a Steam economy item.

.. code-block:: text

	Flag1
	Flag2

Objects / Dictionaries
----------------------

Each series of key-value pairs is a dictionary (sometimes called an object). The top level of the file is treated as a dictionary, and child dictionaries can be added with ``{ }`` curly braces. Adding ``{`` on the line after a key opens a dictionary, and the matching ``}`` closes it.

In this example ``object1`` is a child dictionary in the root dictionary, and ``object2`` is a grand-child:

.. code-block:: text

	object1
	{
		object2
		{
			key value
		}
	}

Arrays / Lists
--------------

Lists (sometimes called an array) can be added with ``[ ]`` square brackets. Adding ``[`` on the line after a key opens a list, and the matching ``]`` closes it.

In this example ``values`` is a list of strings:

.. code-block:: text

	values
	[
		first value
		second value
		third value
	]

Lists can also contain dictionaries as seen in this example:

.. code-block:: text

	List_Of_Objects
	[
		{
			x 1
			y 2
		}
		{
			x 3
			y 4
		}
	]

.. note::

	Many older asset properties predate the addition of lists. In these cases arrays/lists are typically handled by a key specifying the number of items, and then appending the index number to each element's key. For example:

	.. code-block:: text

		// Total number of elements in old-style list
		Elements 2

		// First element has an index of 0
		Element_0 A

		// Second element has an index of 1
		Element_1 B

Comments
--------

Lines starting with ``//`` are comments. (excluded from parsing) Comments can also be added to the end of a line if the value is quoted.

For example these comments are valid:

.. code-block:: text

	// a comment
	key1 value1
	key2 "value2" // in-line comment

Whereas this comment will not be excluded from the value:

.. code-block:: text

	key value // this is not treated as a comment because the value is not in quotes

Vector3
-------

3D vectors can be parsed as a single value from 3 floats optionally surrounded by parenthesis, or from a dictionary with X, Y, and Z keys.

For example these are all valid 3D vectors:

.. code-block:: text

	Position 1, 2, 3
	Offset (4, 5, 6)
	Scale
	{
		X 7
		Y 8
		Z 9
	}

Certain older properties support the newer format while also supporting separate _X, _Y, and _Z keys, namely: ``LOD_Center``, ``LOD_Size``, ``Explosion_Min_Force``, ``Explosion_Max_Force``, and ``Center_Of_Mass``.

Color
-----

Colors can be parsed as a single hexidecimal value with optional "#" in front, or from a dictionary with R, G, and B keys.

For example these are all valid colors:

.. code-block:: text
	
	SkyColor 0000ff
	GroundColor #00ff00
	FogColor
	{
		R 255
		G 0
		B 0
	}

Certain older properties support the newer format while also supporting separate ``_R``, ``_G``, and ``_B`` keys, namely: ``Laser_Color``, and ``Nightvision_Color``.

For example, this would be also be valid for any older property that supports the legacy format:

.. code-block:: text
	
	Laser_Color_R 0.5
	Laser_Color_G 1
	Laser_Color_B 0

History
-------

Prior to the 3.23.6.0 update there were two sets of custom Unturned syntax: "v1" for ``.dat`` files and "v2" for ``.asset`` files. v1 only supported key-value pairs, whereas v2 introduced dictionaries, lists, and required keys/values to be quoted. This is why ``{`` and ``[`` must be on a new line. (Existing v1 assets may have ``{`` or ``[`` as the first character of a value.)
