Unturned Documentation
======================

This repository exists to document `Unturned <https://store.steampowered.com/app/304930>`_'s modding features going forward. Originally map and asset documentation was created through Steam Guides. The main guide with links to related guides can be found here: `Workshop: Creating, Publishing & Updating <https://steamcommunity.com/sharedfiles/filedetails/?id=460136012>`_.

Video Tutorials
---------------

`How to host a Dedicated Server on Windows <https://www.youtube.com/watch?v=8axVrnSLlx4>`_

Several older tutorial videos are gradually becoming outdated and don't represent the current development direction, but are listed here for completeness:

- `Uploading Skins to the Curated Workshop <https://www.youtube.com/watch?v=rF4YvEuxse8>`_

- `Creating Custom Songs <https://www.youtube.com/watch?v=wXpk7o9Dr4k>`_

- `Quick Overview of First Version of Foliage Upgrade <https://www.youtube.com/watch?v=VVt2bRcAWv4>`_

- `Devkit 101 + Landscapes Overview <https://www.youtube.com/watch?v=fkljCH419ug>`_

- `Spawn Tables <https://www.youtube.com/watch?v=7Aiz7utMx8g>`_

- `Building Models <https://www.youtube.com/watch?v=rAZ9KEGjSUk>`_

Offline Downloads
-----------------

PDF and Epub versions of the documentation can be `downloaded <https://readthedocs.org/projects/unturned/downloads/>`_ for offline use.

Contributing
------------

Anyone can contribute towards the *Unturned* modding documentation! To submit an issue, visit the `GitHub repository <https://github.com/SmartlyDressedGames/Unturned-Docs>`_. See the `README <https://github.com/SmartlyDressedGames/Unturned-Docs#readme>`_ for more details on how to contribute.

.. Below is the table-of-content tree for the website,
	which is hidden from the page but appears in the sidebar.

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: About

	about/command-line
	about/getting-started

.. First section has articles on assets (in general).
	Second section lists asset types, alphabetically.
.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Asset Manual

	assets/asset-bundle-custom-data
	assets/asset-bundles
	assets/asset-definitions
	assets/data-file-format
	assets/asset-validation

	assets/airdrop-asset
	assets/animal-asset
	assets/animation
	assets/character-mesh-replacement
	assets/crafting-blacklist-asset
	assets/currency-asset
	assets/effect-asset
	assets/foliage-asset
	assets/item-asset/index
	assets/item-data
	assets/layers
	assets/level-asset
	assets/mod-hooks
	assets/npc-asset/index
	assets/physics-material-asset
	assets/spawn-asset
	assets/stereo-song-asset
	assets/unity-2018
	assets/unity-2019
	assets/vehicle-physics-profile-asset
	assets/weather-asset
	assets/zombie-difficulty-asset

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Mapping

	mapping/curated-maps
	mapping/editor-asset-redirectors
	mapping/favorite-searches
	mapping/level-batching
	mapping/level-config
	mapping/manual-object-culling

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Servers & Programming
	
	servers/command-io
	servers/dedicated-workshop-update-monitor
	servers/game-server-login-tokens
	servers/glazier
	servers/openmod
	servers/port-forwarding
	servers/rocket
	servers/server-hosting
	servers/server-hosting-rules
	servers/server-update-notifications

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Data types
	
	data/asset-ptr
	data/bitmask
	data/guid
	data/master-bundle-ptr
	data/rich-text
