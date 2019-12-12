Asset Bundles
=============

The game loads textures, audio, meshes, prefabs, etc. from Unity __Asset Bundles__ at runtime. How these are setup and used has evolved over the years from individual *.unity3d bundles to .content bundles to .masterbundle files.

[Master Bundles](#master-bundles) should be used for essentially all new projects.

Tool Setup
----------

Prior to using any of these tools they must be imported into a Unity project

1. Inside Unity open the Assets > Import Package > Custom Package... wizard.
1. Find the Unturned installation directory.
3. Navigate to the Bundles/Sources directory.
4. Import the Project.unitypackage.

Individual Asset Bundles (*.unity3d)
-----------------------------------

Most official files have transitioned to the master bundle system, but some uses still exist like the per-map road textures.

### Tool Usage:

1. Follow _Tool Setup_ instructions.
2. Open the tool from the Window > Unturned > Bundle Tool menu.
3. Select individual assets or directories of assets in the Project window.
4. Click Grab to preview which assets will be exported.
5. Click Bundle to choose a destination for the asset bundle file.

### Motivations:

When beginning development of 3.0, it was key to support runtime loading of custom modded content. At the time files in asset bundles were loaded by name without extension, so each game type looked for specific names like "Item", "Object", "Animal", etc. The .unity3d extension was chosen for web browser compatibility. Obviously this system did not age well.

Content Bundles (*.content)
---------------------------

This format is used by devkit landscapes, material palettes and radio songs, but is unlikely to see any further use in favor of master bundles. Ideally support for these usages will be transitioned to master bundles.

### Tool Usage:

1. Follow _Tool Setup_ instructions.
2. Open the tool from the Window > Unturned > Content Tool menu.
3. Select directories of assets in the Project window.
4. In the Inspector window tag them in an asset bundle ending with ".content".
5. Click ... to choose a destination for the content bundle file.
6. Click Export.

### Motivations:

In late 2016 and early 2017 development was focused on improving the editor experience, and one aspect of that was asset bundling. Content bundles scanned a manifest of contained assets in order to allow browsing individually from the in-game editor, and the idea was to allow each content reference to be configured per-game-property. Unfortunately, this effort was far too broad - from building an interface between the game code / online subsystem code to revising the ID system to use GUIDs. In retrospect it would have been wiser to crack down on individual features which has been the approach since then.

Master Bundles (*.masterbundle)
-------------------------------

Most official files including curated maps have been transitioned to master bundles, and they will be used for the forseeable future.

### File Setup:

Master bundles can be loaded from any directory the game loads *.dat files from. Unless an override is specified, the nearest master bundle in the file hierarchy is used. While loading each directory is checked for a MasterBundle.dat file signalling the presence of a master bundle. For example, refer to the core.masterbundle in the Bundles directory.

MasterBundle.dat can set the following keys:

	// Name of asset bundle file in the same directory as MasterBundle.dat.
	Asset_Bundle_Name core.masterbundle

	// Path to the asset bundle within Unity.
	// Unity subfolders should match 1:1 with dat subfolders.
	Asset_Prefix Assets/CoreMasterBundle

	// Version 3 is Unity 2018.4 LTS. Older versions have shader consolidation enabled for backwards compatibility.
	Asset_Bundle_Version 3

Individual asset *.dats can set the following keys:

	// Name of master bundle to load files from.
	Master_Bundle_Override core.masterbundle

	// If included, look for an individual *.unity3d asset bundle instead.
	Exclude_From_Master_Bundle

	// Path within master bundle to load files from.
	// Used by notes to share a common object prefab.
	Bundle_Override_Path /Objects/Medium/Furniture/Note

### Tool Usage:

1. Follow _Tool Setup_ instructions.
2. Open the tool from the Window > Unturned > Master Bundle Tool menu.
3. Select directories of assets in the Project window.
4. In the Inspector window tag them in any asset bundle.
5. Click the checkbox next to an asset bundle's name in the tool to mark it as a master bundle. This filters the list of asset bundles to show, and tracks an export path associated with it.
6. Click the ... to choose a destination for the bundle file.
7. Click Export.

### Motivations:

When upgrading to Unity 2017.4 LTS it became apparent that all asset bundles would have to be re-exported from Unity due to shader compatibility changes. This would be an incredible amount of files, so it was time to re-approach the *.content issue in a way that could quickly convert all existing content. This was handled by keeping the file hierarchy 1:1 and guessing the file extension for the by-name loading.
