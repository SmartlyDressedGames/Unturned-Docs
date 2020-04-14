Asset Pointer
=============

When an asset refers to another it does so using an __Asset Pointer__. These identify the target asset by its GUID.

In \*.dat files
---------------

Note that the GUID here is not wrapped in quotes because Unturned \*.dat files are treated as pairs of strings.

	MyAssetPtr ################################

In \*.asset files
-----------------

	"MyAssetPtr" { "GUID" "################################" }

In JSON files
-------------

	"MyAssetPtr": { "GUID": "################################" }
