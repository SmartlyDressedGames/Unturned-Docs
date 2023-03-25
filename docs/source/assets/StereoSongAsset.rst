.. _doc_assets_stereosong:

Stereo Song Asset
=================

Defines a music track that can be played on the in-game stereo item. (Or any custom music player item for that matter.) For an example refer to ``Unturned_Theme.asset`` in the Songs folder.

This is an :ref:`Asset v2 <doc_assets_v2>` class.

Asset Properties Reference
--------------------------

``Title`` string: display text to show in the music player menu. If a localization .dat file is present the ``Name`` key will be used, or a translation reference can be used. Examples:

.. code-block:: cs
	
	"Title" "My song"

OR

``Name`` in {Language}.dat file

OR

.. code-block:: cs
	
	"Title"
	{
		"Namespace" "SDG"
		"Token" "Stereo_Songs.Unturned_Theme.Title"
	}

``Song`` :ref:`Asset Pointer <doc_data_masterbundleptr>`: audio clip to play. Can either be a newer master bundle pointer or an older content pointer. Examples:

.. code-block:: cs
	
	"Song"
	{
		"MasterBundle" "core.masterbundle"
		"AssetPath" "Effects/Ambience/Cave_0/Cave_0.ogg"
	}

OR

.. code-block:: cs
	
	"Song"
	{
		"Name" "core.content"
		"Path" "assets/resources/bundles/songs/unturned_theme.mp3"
	}

``Link_URL`` string: optional URL to open in web browser when external link button is clicked.

``Is_Loop`` *bool*: whether audio source should loop. Recommend **NOT** using .mp3 format for looping music.
