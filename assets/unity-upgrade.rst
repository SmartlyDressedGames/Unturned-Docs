.. _doc_unity_upgrade:

Upgrading Unity Version
=======================

From Unity 2017 LTS to 2018 LTS
-------------------------------

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

2017 LTS Availability
`````````````````````

For archival purposes the 2017 LTS version of the game will remain in a "unity-2017" beta branch.

Platforms
`````````

Linux 32-bit and MacOS 32-bit have been removed in favor of the 64-bit versions. Servers that were still using the outdated Linux 32-bit depot should update to the 64-bit Linux dedicated server.

Headless server files have been removed from the player Linux depot, and are instead only in the dedicated server Linux depot. Windows headless mode is now supported in 2018 LTS, and is enabled for the Windows dedicated server depot.

From Unity 2018 LTS to 2019 LTS
-------------------------------

Blender Animations
``````````````````

Unity no longer supports importing multiple animations from a single .blend file. Exporting to an exchange format like .fbx is recommended instead, which is how the base game assets have always been handled. Note that this is recommended for meshes/models as well. `Read more details on the Unity issue tracker here. <https://issuetracker.unity3d.com/issues/using-multiple-animation-clips-in-blender-not-all-animation-clips-are-imported-using-a-blend-file>`_

2018 LTS Availability
`````````````````````

For archival purposes the 2018 LTS version of the game will remain in a "unity-2018" beta branch.
