Unturned Documentation
======================

.. Below is the table-of-content tree for the website,
	which is hidden from the page but appears in the sidebar.
	...
	The toctree is located at the top of this file, so that
	chapters are generated properly for the offline downloads.

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: About

	about/getting-started
	about/launch-options
	about/steam-workshop

.. First section has articles on assets (in general).
	Second section lists asset types, alphabetically.
.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Introduction to Modding

	assets/asset-bundles
	assets/asset-definitions
	assets/data-file-format
	assets/asset-validation
	assets/asset-bundle-custom-data
	assets/curated-items
	assets/animation
	assets/layers
	assets/mod-hooks
	assets/unity-2018
	assets/unity-2019

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Asset Manual

	assets/airdrop-asset
	assets/animal-asset
	assets/character-mesh-replacement
	assets/crafting-blacklist-asset
	assets/currency-asset
	assets/effect-asset
	assets/foliage-asset
	assets/item-asset/index
	assets/level-asset
	assets/material-palette-asset
	assets/npc-asset/index
	assets/object-asset
	assets/outfit-asset
	assets/physics-material-asset
	assets/redirector-asset
	assets/resource-asset
	assets/spawn-asset
	assets/stereo-song-asset
	assets/vehicle-asset
	assets/vehicle-physics-profile-asset
	assets/vehicle-redirector-asset
	assets/weather-asset
	assets/zombie-difficulty-asset

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Mapping

	mapping/charts
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

	servers/bookmark-host
	servers/command-io
	servers/debugging-exceptions
	servers/dedicated-workshop-update-monitor
	servers/fake-ip
	servers/game-server-login-tokens
	servers/glazier
	servers/openmod
	servers/port-forwarding
	servers/rocket
	servers/server-auto-restart
	servers/server-codes
	servers/server-hosting
	servers/server-hosting-rules
	servers/server-update-notifications

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Data Types

	data/built-in-types

	data/asset-ptr
	data/bitmask
	data/color
	data/enum/index
	data/flag
	data/guid
	data/master-bundle-ptr
	data/rich-text
	data/struct/index
	data/vector3

Welcome to the official documentation for `Unturned <https://store.steampowered.com/app/304930>`_'s modding and server hosting features! To navigate, use the table of contents in the sidebar or the search function in the top-left corner.

Upcoming Features
-----------------

You can find modding features under consideration on this Trello board: `Unturned Roadmap <https://trello.com/b/gpe4zlW3/unturned-roadmap>`_. The cards on the board aren't ordered in any particular way. i.e., they do not dictate the order of updates.

Miscellaneous requests and tasks that may pop up take priority over the roadmap, so it may go a while between progress updates. For example, work for curated maps often takes priority. Several high-priority ideas that don't yet have a solid plan, like a crafting revamp, are not listed on the board.

Legacy Tutorials
----------------

Our earliest modding documentation was available through Steam Guides. Although most of these guides have been superseded by our documentation here, some still contain useful information about Unity setup that we have yet to bring over. The useful guides are:

- `Items <https://steamcommunity.com/sharedfiles/filedetails/?id=470771503>`_: Most of the sub-sections about Unity setup are still relevant.
- `Vehicles <https://steamcommunity.com/sharedfiles/filedetails/?id=470772671>`_: Information about Unity setup.
- `Objects <https://steamcommunity.com/sharedfiles/filedetails/?id=470771210>`_: Information about Unity setup.
- `Misc. Assets <https://steamcommunity.com/sharedfiles/filedetails/?id=481212147>`_: Unity setup for animals, effects, and resources.
- `Maps <https://steamcommunity.com/sharedfiles/filedetails/?id=470770384>`_: Explaining various features.
- `Localization <https://steamcommunity.com/sharedfiles/filedetails/?id=470770864>`_
- `Creating 3rd-party Modules <https://steamcommunity.com/sharedfiles/filedetails/?id=790629631>`_: Not to be confused with *mods* or *plugins*.
- `Uploading Mods to the Steam Workshop <https://steamcommunity.com/sharedfiles/filedetails/?id=460136012>`_
- `Upgrading from Unity 5 LTS to Unity 2017 LTS <https://steamcommunity.com/sharedfiles/filedetails/?id=1624005178>`_: Only relevant for *very* old mods, but lists the important changes between those two versions.

There are several official video tutorials available, but many of these have gradually become outdated. They do not accurately represent the current modding features available, or may contain incorrect information, but are listed here for completeness:

- `Hosting a Dedicated Server on Windows <https://www.youtube.com/watch?v=8axVrnSLlx4>`_
- `Uploading Skins to the Curated Workshop <https://www.youtube.com/watch?v=rF4YvEuxse8>`_
- `Creating Custom Songs <https://www.youtube.com/watch?v=wXpk7o9Dr4k>`_
- `Quick Overview of First Version of Foliage Upgrade <https://www.youtube.com/watch?v=VVt2bRcAWv4>`_
- `Devkit 101 + Landscapes Overview <https://www.youtube.com/watch?v=fkljCH419ug>`_
- `Spawn Tables <https://www.youtube.com/watch?v=7Aiz7utMx8g>`_
- `Building Models <https://www.youtube.com/watch?v=rAZ9KEGjSUk>`_

If you refer to a video tutorial (official or otherwise), we recommend double-checking the information with our written documentation when possible.

Offline Downloads
-----------------

PDF and Epub versions of the documentation can be `downloaded <https://readthedocs.org/projects/unturned/downloads/>`_ for offline use.

Contributing
------------

Anyone can contribute towards the *Unturned* modding documentation! To submit an issue, visit the `GitHub repository <https://github.com/SmartlyDressedGames/Unturned-Docs>`_. See the `README <https://github.com/SmartlyDressedGames/Unturned-Docs#readme>`_ for more details on how to contribute.
