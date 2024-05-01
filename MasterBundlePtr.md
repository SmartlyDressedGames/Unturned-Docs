**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/data/master-bundle-ptr.html) instead.*

Master Bundle Pointer
=====================

Identifies a Unity asset like a prefab, material or audio clip within a master bundle.

In \*.asset files
-----------------

`MasterBundle`: File name of the asset bundle exported from Unity. Should match the `Asset_Bundle_Name` configured in the `MasterBundle.dat` file.

`AssetPath`: File path of the Unity asset e.g. \*.prefab, \*.mat, \*.png, \*.ogg, etc. Relative to the `Asset_Prefix` path configured in the `MasterBundle.dat` file.

	"MyMasterBundlePtr"
	{
		"MasterBundle" "core.masterbundle"
		"AssetPath" "path/to/file.extension"
	}

If the asset default master bundle should be used then the path can be specified inline:

	"MyMasterBundlePtr" "path/to/file.extension"