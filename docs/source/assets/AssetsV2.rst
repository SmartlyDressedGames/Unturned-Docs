.. _doc_assets_v2:

Assets v2
=========

For the vast majority of older features like items, vehicles, effects, etc refer to :ref:`Assets v1 <doc_assets_v1>`.

The main advantages of the newer assets are:

1. Extensible types. Adding a new asset v1 type (e.g. Gun, Melee, Dialogue) required extending an enum. Eventually this was improved to allow mods to register string-class mappings during startup. Asset v2 files specify the qualified class name, so do not require any registration.

2. Structured file format. Arrays in v1 assets are painful whereas v2 assets do not require element annotation. Theoretically the file can be any format like json or xml. This is the main reason why flat v1 assets cannot be automatically upgraded (yet).

3. Visual editor. There has been work on an inspector in the devkit for creating and editing assets rather than manually modifying files. At the time of writing (early 2020) this is no longer a priority sadly.

File Format
-----------

Any ``.asset`` file is treated as v2. Lines starting with ``//`` are comments. Keys and values are wrapped in quotes. Curly braces ``{ }`` wrap objects and square brackets ``[ ]`` wrap arrays.

.. code-block:: cs
	
	"Key" "Value"
	"Object"
	{
		"Key" "Value"
	}
	"Array"
	[
		{
			"Key" "Value"
		}
		{ "Key" "Value" }
	]

Header
------

Each asset has a ``Metadata`` section for preparing to load.

``GUID`` *string*: Refer to :ref:`GUID <doc_data_guid>` documentation.

``Type`` *string*: Fully qualified name of any class in any module.

.. code-block:: cs
	
	"Metadata"
	{
		"GUID" "7e4b847061b64272b42ea8869fd053c7"
		"Type" "SDG.Unturned.Asset"
	}

Body
----

The ``Asset`` body contains any class properties. Individual asset type documentation elaborates on these.

.. code-block:: cs
	
	"Asset"
	{
		"Key" "Value"
	}
