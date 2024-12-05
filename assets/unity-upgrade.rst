.. _doc_unity_upgrade:

Upgrading Unity Version
=======================

This page covers the various engine upgrades that *Unturned* has undergone, and the important changes from them. While much of the older information is unlikely to still be relevant, it may provide some insight on the off chance that you are updating a particularly old mod, or referencing a tutorial created for a previous Unity version.

From Unity 5 LTS to 2017 LTS
----------------------------

The upgrade from Unity 5.5 to 2017.4 was a large change, and any mods created in Unity 5 are no longer compatible with the game. For archival purposes, the Unity 5.5 LTS version of the game remains available from the "unity-5.5" beta branch.

There were two key reasons for going through an engine upgrade. First, Unity 2017 marked the start of Unity's annual releases as they focused on stability, and performance could be improved by removing workarounds for some now-resolved Unity bugs. Second, Apple deprecated their OpenGL support, so supporting 2017.4's Metal graphics API would be important for macOS players.

Master bundles were introduced to make updating mods easier.

Master Bundles
``````````````

Rather than exporting each bundle as individual .unity3d files, you can now export multiple bundles into a combined **.masterbundle**. Master bundles are not required, but they are more efficient when it comes to time and performance. However, they are not *required*, and you may find it easier to quickly iterate on a .unity3d bundle.

If the game detects a master bundle file, it will load bundles from sub-directories using their relative folder path.

For example, ``MyModBundles/Items/Guns/MyGunItem.dat`` could be the path to an item's .dat file. If ``MyModBundles`` contains a master bundle, it will try to load all Unity files using the relative path ``/Items/Guns``. It is important for .dat folders and Unity folders to line up, 1:1.

Installing the Tools
````````````````````

Copy all of the files from ``Unturned/Bundles/Sources/Tools`` into the ``.../Assets/Editor`` directory of your Unity project. The **MasterBundleTool** will now be available from **Window > Unturned**. To use this tool, first assign your folder to an AssetBundle, and then export your bundles to a location that contains a corresponding MasterBundle.dat file.

Shaders can be imported from the ``All_Shaders.unitypackage`` (also located in a subdirectory of ``Sources``). We recommend using official shaders to improve compatibility with base game content.

Exporting from Unity
````````````````````

.. attention::

	This section of the documentation is admittedly rather old, and it should eventually be moved to a better spot. Fortunately—these steps are still accurate, and the information below has been revised recently. *[2024 November]*

Exporting requires some initial setup within Unity and the target location for your exported master bundle.

In Unity, select the folder within the Project Browser that contains your bundles. Assign it to an AssetBundle from the Inspector. If you haven't created one yet, this is the time to do so. For example, vanilla/official bundles are in an AssetBundle named "core.masterbundle", while the curated Hawaii map's bundles are in "hawaii.masterbundle".

Open the Master Bundle Tool. Select your AssetBundle from the dropdown. If your mod should be fully compatible with MacOS and Linux devices, you will need to check the "Multi-platform" option before exporting.

.. tip::

	When you're still working on your mod, you don't need to enable multi-platform support! This option can be toggled at any time. By only enabling this for release candidates, you can cut down on build time while you're still iterating.

Clicking the "..." button will let you select a target location to export the master bundle into. Before you can proceed, you will need a MasterBundle.dat file in that location.

Navigate to your target location. Any folder that would contain a master bundle needs a **MasterBundle.dat** file. When the game traverses the file hierarchy, it will check for this file, and if present it will assume all sub-folders should be redirected into that master bundle.

Create this file at your target location. You should configure the following options in your MasterBundle.dat file:

- | **Asset_Bundle_Name**: Filename of the Windows master bundle exported from Unity. For example, ``hawaii.masterbundle``.

- | **Asset_Prefix**: Filepath to the folder you selected as an AssetBundle in Unity. For example, your path could be ``Assets/MyModBundles``. In which case, the game could look for an item in ``Assets/MyModBundles/Items/Guns``.

.. note::

	Bundled assets have a few optional properties they can use. The **Exclude_From_Master_Bundle** flag will cause that .dat file to ignore any parent MasterBundles in the folder hierarchy, and instead look for an individual .unity3d file. The **Master_Bundle_Override** property lets you specify the name of a master bundle to redirect to. **Bundle_Override_Path** can be used to have multiple items share the same setup in Unity (such as how the vanilla note objects share the same model), or combined with the previous property to use models from other master bundles (e.g., if you wanted to use the Eaglefire's model but give it custom stats).

Back in Unity, you can now export your master bundle.

Troubleshooting
```````````````

Colors too light or dark in-game
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most likely the Color Space setting in your Unity project needs adjusting. Navigate to Edit > Project Settings > Player. Under the Other Settings section change Color Space to Linear.

If that doesn't work, double-check that sRGB is enabled on your textures.

Devkit Foliage
~~~~~~~~~~~~~~

Materials default to instancing disabled now, so enable the Instancing flag in the Unity material inspector and rebuild the asset bundle.

From Unity 2017 LTS to 2018 LTS
-------------------------------

For archival purposes, the Unity 2017.4 LTS version of the game remains available from the "unity-2017.4" beta branch.

Asset Bundles
`````````````

Older .unity3d/.content/.masterbundle files should work properly without needing any update unless they use custom shaders. The game automatically tries to consolidate their shaders with the latest versions during loading. Once re-exported, Asset_Bundle_Version can be set to 3 in MasterBundle.dat or individual .dat files to disable this shader consolidation step.

Some of the slower asset checks like finding missing meshes have been made optional. Running the game with the "-ValidateAssets" command-line option enables them, and is recommended while working on new content.

Unity Packages
``````````````

All example content has been updated for 2018 LTS, and now has a consistent export process to ensure the contents are kept valid. What were once individual packages (e.g. All_Shaders.unitypackage) have been merged into a single ExampleAssets.unitypackage in the Extras/Sources/Examples directory.

Logging / Server Console
````````````````````````

Usage of Unity's built-in Debug.Log has been replaced with logging to the Client.log or Server_XYZ.log files in the Logs folder. This works around conflict with standard output on the Linux server, so -logfile redirect workarounds should no longer be necessary. -ThreadedConsole implementation has been made the default, but can be disabled by -LegacyConsole.

Workshop
````````

Uploads from 2018 LTS are incompatible with past versions of the game, and a warning message is shown when loading newer content in the 2017 LTS version.

Platforms
`````````

Linux 32-bit and MacOS 32-bit have been removed in favor of the 64-bit versions. Servers that were still using the outdated Linux 32-bit depot should update to the 64-bit Linux dedicated server.

Headless server files have been removed from the player Linux depot, and are instead only in the dedicated server Linux depot. Windows headless mode is now supported in 2018 LTS, and is enabled for the Windows dedicated server depot.





From Unity 2018 LTS to 2019 LTS
-------------------------------

There are very few notable changes from this upgrade. For archival purposes, the Unity 2018 LTS version of the game remains available from the "unity-2018" beta branch.

By default, Unity no longer supports importing multiple animations from a single .blend file. Exporting to an exchange format like .fbx is recommended.

.. tip::

	This is recommended for meshes/models as well! The base game has always handled its own assets like this, as well.

You can find more details in `case #1186253 <https://issuetracker.unity3d.com/issues/using-multiple-animation-clips-in-blender-not-all-animation-clips-are-imported-using-a-blend-file>`_ on the Unity issue tracker.
