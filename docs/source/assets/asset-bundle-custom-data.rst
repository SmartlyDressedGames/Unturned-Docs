.. _doc_asset_bundle_custom_data:

Asset Bundle Custom Data
========================

Unity ``ScriptableObject`` which can optionally be created in a :ref:`Master Bundle's <doc_asset_bundles>` root for Unturned-specific asset bundle metadata.

``Owner Workshop File Id`` *uint64*: ID of a file published to the Steam Workshop. If Unturned is loading this asset bundle from a Steam workshop file but the file ID does not match then loading will be canceled. Prevents the asset bundle from being easily copied/stolen.

How to Set Owner Workshop File
------------------------------

1. Within the Unity project window find your master bundle's root folder. This is the same as the Asset_Prefix specified in your MasterBundle.dat file. For example Hawaii's root folder is Assets/HawaiiMasterBundle.

2. Create the ``AssetBundleCustomData`` object by Right Clicking > Create > Unturned > Asset Bundle Custom Data

3. Find your workshop file's ID. This is the number after ``https://steamcommunity.com/sharedfiles/filedetails/?id=`` in the URL of your workshop file's page.

4. Set ``Owner Workshop File Id`` to match your workshop file's ID.

5. (optional) Check that Unturned is finding the custom data by looking for "Loaded (your asset bundle name) custom data from (path)" in the log file, or "Tried loading (your asset bundle name) optional custom data from (path)" in the case it is not found.
