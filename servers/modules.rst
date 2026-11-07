.. _doc_servers_modules:

Modules
=======

Modules are assembly files that the game loads at startup.  Each module has a ``.module`` configuration file, and the game invokes methods in any class in its assemblies that implement the ``SDG.Framework.Modules.IModuleNexus`` interface. Plugin frameworks such as :ref:`OpenMod <doc_servers_openmod>` and :ref:`Rocket <doc_servers_rocket>` utilize this system. While traditionally used only by the server, modules can also be installed on player clients.

.. warning:: Players and server hosts should maintain caution when installing modules from untrusted sources. Distributions on the workshop are never officially verified.

Installing a Module
-------------------

Place the module's folder inside of the ``Modules`` directory of your Unturned installation, then restart the game or server. The game searches this folder and its subfolder for ``.module`` files. You may keep each module within its own folder.

.. code-block:: text

	Unturned/
	└── Modules/
	    └── MyModule/
	        ├── MyModule.module
	        └── MyModule.dll

The ``-ModulesPath`` :ref:`launch option <doc_launch_options>` can be used to define the search to another directory instead.

Configuration File
------------------

``.module`` files are formatted in JSON. Field names are case-sensitive.

.. code-block:: json

	{
		"IsEnabled": true,
		"Name": "ExampleModule",
		"Version": "1.0.0.0",
		"Dependencies":
		[
			{
				"Name": "OtherModule",
				"Version": "1.0.0.0"
			}
		],
		"Assemblies":
		[
			{
				"Path": "/ExampleModule.dll",
				"Role": "Both_Optional"
			}
		]
	}

**IsEnabled** *bool*: If false, the module will not be loaded. Defaults to ``true``.

**Name** *string*: Name of module.

**Version** *string*: Version of the module.

**Dependencies** *array of objects*: Modules that must be loaded before this module. If the dependency is missing or its version is lower than specified, the module is not loaded.

		**Name** *string*: Name of the required module.

		**Version** *string*: Minimum version of the required modules.

**Assemblies** *array of objects*: Assemblies that belong to the module.

		**Path** *string*: Path to the ``.dll`` file. This is relative to the folder containing the ``.module`` file.

		**Role** *EModuleRole*: Specifies if the module should be loaded on the server, client, or both. Options include: ``Client``, ``Server``, ``Both_Optional``, and ``Both_Required``.

		**Load_As_Byte_Array** *bool*: If true, the entire assembly is read into memory before being loaded rather than loaded directly from the file. Prevents the file from being locked during runtime. Defaults to ``false``.