Unturned Documentation
======================

This repository exists to document `Unturned <https://store.steampowered.com/app/304930>`_'s modding features going forward. Originally map and asset documentation was created through Steam Guides. The main guide with links to related guides can be found here: `Workshop: Creating, Publishing & Updating <https://steamcommunity.com/sharedfiles/filedetails/?id=460136012>`_.

Video Tutorials
---------------

`How to host a Dedicated Server on Windows <https://www.youtube.com/watch?v=8axVrnSLlx4>`_

Several older tutorial videos are gradually becoming outdated and don't represent the current development direction, but are listed here for completeness:

* `Uploading Skins to the Curated Workshop <https://www.youtube.com/watch?v=rF4YvEuxse8>`_

* `Creating Custom Songs <https://www.youtube.com/watch?v=wXpk7o9Dr4k>`_

* `Quick Overview of First Version of Foliage Upgrade <https://www.youtube.com/watch?v=VVt2bRcAWv4>`_

* `Devkit 101 + Landscapes Overview <https://www.youtube.com/watch?v=fkljCH419ug>`_

* `Spawn Tables <https://www.youtube.com/watch?v=7Aiz7utMx8g>`_

* `Building Models <https://www.youtube.com/watch?v=rAZ9KEGjSUk>`_

.. Below is the table-of-content tree for the website,
	which is hidden from the page but appears in the sidebar.

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: About
	
	about/Troubleshooting
	about/CommandLine
	about/GettingStarted

.. First section has articles on assets (in general).
	Second section lists asset types, alphabetically.
.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Asset Manual
	
	assets/AssetBundleCustomData
	assets/AssetBundles
	assets/AssetsV1
	assets/AssetsV2
	assets/AssetValidation

	assets/AirdropAsset
	assets/AnimalAsset
	assets/Animation
	assets/CharacterMeshReplacement
	assets/CraftingBlacklistAsset
	assets/Currency
	assets/EffectAsset
	assets/Foliage
	assets/ItemAsset/index
	assets/ItemData
	assets/Layers
	assets/LevelAsset
	assets/ModHooks
	assets/NPCAsset/index
	assets/PhysicsMaterialAsset
	assets/SpawnAsset
	assets/StereoSongAsset
	assets/Unity2018
	assets/Unity2019
	assets/VehiclePhysicsProfile
	assets/WeatherAsset
	assets/ZombieDifficultyAsset

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Mapping
	
	mapping/CuratedMaps
	mapping/EditorAssetRedirectors
	mapping/FavoriteSearches
	mapping/Landscape
	mapping/LevelBatching
	mapping/LevelConfig
	mapping/ManualObjectCulling

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Servers & Programming

	servers/CommandIO
	servers/DedicatedWorkshopUpdateMonitor
	servers/GameServerLoginTokens
	servers/Glazier
	servers/OpenMod
	servers/PortForwarding
	servers/Rocket
	servers/RocketMod
	servers/ServerHosting
	servers/ServerHostingRules
	servers/ServerUpdateNotifications

.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Data types
	
	data/AssetPtr
	data/Bitmask
	data/GUID
	data/MasterBundlePtr
