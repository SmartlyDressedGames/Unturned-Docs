.. _doc_asset_bundles:

Asset Bundles
=============

The game loads textures, audio, meshes, prefabs, etc. from **Unity Asset Bundles** at runtime. How these are setup and used has evolved over the years from individual
\*.unity3d bundles to
\*.content bundles to
\*.masterbundle files.

:ref:`Master bundles <doc_asset_bundles:master_bundles>` should be used for essentially all new projects.

Tool Setup
----------

Prior to using any of these tools they must be imported into a Unity project

#. Inside Unity open the Assets > Import Package > Custom Package... wizard.
#. Find the Unturned installation directory.
#. Navigate to the Extras/Sources directory.
#. Import the Project.unitypackage.

.. _doc_asset_bundles:master_bundles:

Master Bundles
--------------

Master bundles are the most efficient way for your assets to be packaged and distributed. They should be used for essentially any project that you plan to share with other players.

There are only a few asset types that are unsupported by master bundles.

File Setup
``````````

Master bundles can be loaded from any directory the game loads \*.dat files from. Unless an override is specified, the nearest master bundle in the file hierarchy is used. While loading each directory is checked for a MasterBundle.dat file signalling the presence of a master bundle. For example, refer to the core.masterbundle in the Bundles directory.

MasterBundle.dat can set the following keys:

.. code-block:: unturneddat

	// Name of asset bundle file in the same directory as MasterBundle.dat.
	Asset_Bundle_Name core.masterbundle

	// Path to the asset bundle within Unity.
	// Unity subfolders should match 1:1 with dat subfolders.
	Asset_Prefix Assets/CoreMasterBundle

	// Version 3 is Unity 2018.4 LTS. Older versions have shader consolidation enabled for backwards compatibility.
	Asset_Bundle_Version 3

Individual asset \*.dats can set the following keys:

.. code-block:: unturneddat

	// Name of master bundle to load files from.
	Master_Bundle_Override core.masterbundle

	// If included, look for an individual *.unity3d asset bundle instead.
	Exclude_From_Master_Bundle

	// Path within master bundle to load files from.
	// Used by notes to share a common object prefab.
	Bundle_Override_Path /Objects/Medium/Furniture/Note

	// If true, path within master bundle appends asset file name as subdirectory.
	// For example:
	// Guns/Eaglefire.asset → Guns/Eaglefire/Item.prefab
	Bundle_Path_Include_Filename true

Tool Usage
``````````

1. Follow *Tool Setup* instructions.
2. Open the tool from the Window > Unturned > Master Bundle Tool menu.
3. Select directories of assets in the Project window.
4. In the Inspector window tag them in any asset bundle.
5. Click the checkbox next to an asset bundle's name in the tool to mark it as a master bundle. This filters the list of asset bundles to show, and tracks an export path associated with it.
6. Click the ... to choose a destination for the bundle file.
7. Click Export.
8. **(optional)** When redistributing the asset bundle the "multiplatform" toggle should be enabled. This ensures platform-specific shaders are included, and exports a ".hash" file so the server can validate client asset bundle integrity.

Generated Files
```````````````

After exporting a master bundle, the following files are generated in the export directory:

***_linux.masterbundle** and ***_mac.masterbundle** – These contain platform-specific shaders for Linux and macOS, respectively. These are only generated when "multiplatform" is enabled.

***.masterbundle.hash** – A hash file used by the server to verify asset bundle integrity for other platforms. For example, a server running Windows uses it to verify macOS and Linux asset bundle integrity.

.. warning:: Deleting the .hash file means cheaters can modify the asset bundle. For example, to make certain materials glow in the dark or to see through certain objects. Mods should always include the .hash file when redistributing asset bundles.

***.masterbundle.manifest** – A manifest file listing all assets in the bundle, their paths, and their hashes. When multiplatform is enabled, a manifest file is generated for each platform. Coincidentally, the manifest file is useful when debugging mods bundles. As it contains filepaths of all bundled assets, it can help confirm that assets were bundled as expected, and can also be useful when using master bundle pointers.

Individual Asset Bundles
------------------------

Most official files have transitioned to the master bundle system, but some use individual asset bundles (\*.unity3d). For example:

- Per-map road textures.
- Colors used by charts.
- Level ambience.

Tool Usage
``````````

1. Follow *Tool Setup* instructions.
2. Open the tool from the Window > Unturned > Bundle Tool menu.
3. Select individual assets or directories of assets in the Project window.
4. Click Grab to preview which assets will be exported.
5. Click Bundle to choose a destination for the asset bundle file.

Motivations
```````````

When beginning development of 3.0, it was key to support runtime loading of custom modded content. At the time files in asset bundles were loaded by name without extension, so each game type looked for specific names like "Item", "Object", "Animal", etc. The .unity3d extension was chosen for web browser compatibility. Obviously this system did not age well.

Content Bundles (\*.content)
----------------------------

.. deprecated:: 3.22.4.0

Content bundles were originally used by terrain, material palettes, and radio songs. Support for content bundles has been removed since February 25, 2022 and should be replaced by master bundles.

Although it is preferable to properly migrate older assets into master bundles, preexisting content bundles can be easily reused as a master bundle. Rename the
\*.content file to be a
\*.masterbundle file instead. Then, add a corresponding MasterBundle.dat file as described in the file setup for master bundles.
