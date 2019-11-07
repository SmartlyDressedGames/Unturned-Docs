Curated Maps
============

Overview
--------

Community-created updates and maps that are officially linked from the game are considered __Curated Maps__. They help players find high-quality new experiences, and keep the game updated with fresh content. Modders can then earn money from their work on their hobby, and get their creations highlighted.

Quality Assurance
-----------------

The primary focus of this article at the time of posting is to begin laying out standards to help ensure top quality between maps. This will be an iterative process, and is open to collaboration and feedback from the community.

__Map Variety__: New maps should feel noticeably different in order to be a candidate for curation. This is a subjective rule, and is covered by factors like interesting progression, new items, new environments, new architecture styles, new buildings, etc.

__Asset Validation__: Running the game with the [-ValidateAssets](ValidateAssets.md) command-line flag should not produce any warnings or errors.

__English Text__: Having an English-speaking member of the mod team is recommended, and [MoltonMontro](mailto:moltonmontro@smartlydressedgames.com) has offered to help with English-related questions. Most importantly in this regard is proper punctuation and grammar: while native English speakers can easily read incorrect punctuation, it is very helpful for non-native readers. Ironically this paragraph probably has some punctuation errors.

__Project Organization__: To prevent unintended assets from being exported into asset bundles, convention is to separate the project files into Sources and MasterBundle directories. Hawaii is split between a directory called "HawaiiMasterBundle" in the project root, and a Sources directory which contains all of the .blend, .mb, .xcf, .psd, .ai, etc files. When exporting the asset bundle this ensures only game files like .fbx and .prefab are included.

__Asset Duplication__: If multiple objects share identical prefabs, or use vanilla content, asset bundle size can be improved by sharing the same prefabs. For an example of this refer to the vanilla notes using Bundle_Override_Path.

__Water Reflections__: When using water volumes, only one should have planar reflections enabled. These reflections require rendering the world a second time for each enabled volume, and are some of the most performance expensive effects in the game.

__Overlapping Navmeshes__: No bounds should overlap. Otherwise zombies will appear and disappear unexpectedly in multiplayer.

__Visibility Overlay__: The visibility menu in the editor sums the mesh complexity in each region. Ideally there should only be a few red zones.

__Item Icons__: Each item should have a proper icon in the inventory. One way to quickly preview the icon is to attach an orthographic camera in Unity, and tune the orthographic size before setting the size in the .dat file.

Stockpile Preparation
---------------------

Each release is usually accompanied by a few cosmetics and skins in the game's item store. Royalties from the sales are shared with the mod team.

__File Sharing__: Ideally the items have been setup for use as clothes in-game, and then exported into a .unitypackage. This package will then be imported into the vanilla project.

__Curated Workshop Item__: Payment splits are handled by a hidden curated workshop item. Setting this up usually takes a few weeks for new contributors bank and tax information to be processed.

__Bundles__: Two or three collections of sets of four to six items.

__Mystery Boxes__: Fifteen to twenty items that have individual value (not parts of sets like a shirt/pants).


Eligibility for Curation
------------------------

Even if a map is of substantial quality, it may not be eligible for curation. When considering eligibility, it is important that the map fits the vanilla style of the game.

Although not every map should be curated, it is important to recognize the amount of effort that modders have put into their projects. Depending on the direction of the project, non-vanilla assets should either be adjusted to fit the vanilla style, or alternatives to curation should be considered instead.

__Vanilla-style maps__: are eligible for curation. They are also eligible for cosmetic bundles or mystery boxes.

__Non-vanilla maps__: are eligible to be featured. They are also eligible to have cosmetic content on the Stockpile.

It is encouraged to still work on a project even if it is not eligible for curation. Creating a variety of Workshop content creates a valuable portfolio for future curation attempts, and may still benefit from being featured.
