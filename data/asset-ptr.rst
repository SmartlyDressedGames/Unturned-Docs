.. _doc_data_assetptr:

Asset Pointer
=============

When an asset refers to another it does so using an **Asset Pointer**. These identify the target asset by its :ref:`GUID <doc_data_guid>`.

In \*.dat files
---------------

Note that the GUID here is not wrapped in quotes because Unturned \*.dat files are treated as pairs of strings.

.. code-block:: unturneddat
	
	MyAssetPtr ################################

In \*.asset files
-----------------

Two formats are supported in these files. The inline style was added later so you will see the older style used in many official assets.

.. code-block:: unturnedasset
	
	"MyAssetPtr" "################################"
	"MyAssetPtr" { "GUID" "################################" }

In JSON files
-------------

.. code-block:: json
	
	"MyAssetPtr": { "GUID": "################################" }
