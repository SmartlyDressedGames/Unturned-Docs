.. _doc_data_masterbundleptr:

Master Bundle Pointer
=====================

Identifies a Unity asset like a prefab, material or audio clip within a master bundle.

In \*.asset files
-----------------

``MasterBundle``: File name of the asset bundle exported from Unity. Should match the ``Asset_Bundle_Name`` configured in the ``MasterBundle.dat`` file.

``AssetPath``: File path of the Unity asset e.g. \*.prefab,
\*.mat,
\*.png,
\*.ogg, etc. Relative to the ``Asset_Prefix`` path configured in the ``MasterBundle.dat`` file.

.. code-block:: cs
	
	"MyMasterBundlePtr"
	{
		"MasterBundle" "core.masterbundle"
		"AssetPath" "path/to/file.extension"
	}

If the asset default master bundle should be used then the path can be specified inline:

.. code-block:: cs
	
	"MyMasterBundlePtr" "path/to/file.extension"
