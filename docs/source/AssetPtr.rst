Asset Pointer
=============

When an asset refers to another it does so using an **Asset Pointer**. These identify the target asset by its GUID.

In \*.dat files
---------------

Note that the GUID here is not wrapped in quotes because Unturned \*.dat files are treated as pairs of strings.

.. code-block::
	
	MyAssetPtr ################################

In \*.asset files
-----------------

Two formats are supported in these files. The inline style was added later so you will see the older style used in many official assets.

.. code-block:: cs
	
	"MyAssetPtr" "################################"
	"MyAssetPtr" { "GUID" "################################" }

In JSON files
-------------

.. code-block:: json
	
	"MyAssetPtr": { "GUID": "################################" }
