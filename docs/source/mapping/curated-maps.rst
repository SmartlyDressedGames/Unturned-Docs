.. _doc_mapping_curated:

Curated Maps
============

Community-created maps that are officially linked from the game are considered **Curated Maps**. They help players find high-quality new experiences, and keep the game updated with fresh content. Modders can then earn money from their work on their hobby, and get their creations highlighted.

Eligibility for Curation
------------------------

Even if a map is of substantial quality, it may not be eligible for curation. When considering eligibility, it is important that the map fits the vanilla style of the game.

Although not every map should be curated, it is important to recognize the amount of effort that modders have put into their projects. Depending on the direction of the project, non-vanilla assets should either be adjusted to fit the vanilla style, or alternatives to curation should be considered instead.

Vanilla-style maps are eligible for curation, whereas non-vanilla maps are eligible to be featured. To help support the creators, both are eligible for revenue sharing cosmetic content in the game's item store e.g. the Candyland map.

It is encouraged to still work on a project even if it is not eligible for curation. Creating a variety of Workshop content creates a valuable portfolio for future curation attempts, and may still benefit from being featured.

Menu Visibility
---------------

One key component of sharing a curated map, trending popular workshop item, or specifically featured map is spotlighting it on the main menu. In any of these cases an article is placed above the recent news and announcements showcasing the preview image, and an expandable description.

In-game the description supports the following BBCode tags:

* ``[b]``
* ``[i]``
* ``[list]``
* ``[*]``
* ``[h1]``
* ``[img]``
* ``[url]``

Ideally descriptions are kept succinct, so separate discussion topics might be a better place for long sections like ID lists.

By default popular items are surfaced, but workshop items can be specifically featured to help bring attention to projects with a lot of effort put into them, and curated maps. This can be done for new releases or major updates. Updates can link to a separate URL for the release notes.

Additionally, curated maps are linked from the singleplayer curated maps list, and will inherit the main menu "new" or "updated" label.

Quality Assurance
-----------------

The primary focus of this article at the time of posting is to begin laying out standards to help ensure top quality between maps. This will be an iterative process, and is open to collaboration and feedback from the community.

**Map Variety**: New maps should feel noticeably different in order to be a candidate for curation. This is a subjective rule, and is covered by factors like interesting progression, new items, new environments, new architecture styles, new buildings, etc.

**Asset Validation**: Running the game with the :ref:`-ValidateAssets <doc_asset_validation>` command-line flag should not produce any warnings or errors.

**English Text**: Having an English-speaking member of the mod team is recommended, and `MoltonMontro <mailto:moltonmontro@smartlydressedgames.com>`_ has offered to help with English-related questions. Most importantly in this regard is proper punctuation and grammar: while native English speakers can easily read incorrect punctuation, it is very helpful for non-native readers. Ironically this paragraph probably has some punctuation errors.

**Project Organization**: To prevent unintended assets from being exported into asset bundles, convention is to separate the project files into Sources and MasterBundle directories. Hawaii is split between a directory called "HawaiiMasterBundle" in the project root, and a Sources directory which contains all of the .blend, .mb, .xcf, .psd, .ai, etc files. When exporting the asset bundle this ensures only game files like .fbx and .prefab are included.

**Asset Duplication**: If multiple objects share identical prefabs, or use vanilla content, asset bundle size can be improved by sharing the same prefabs. For an example of this refer to the vanilla notes using Bundle_Override_Path.

**Water Reflections**: When using water volumes, only one should have planar reflections enabled. These reflections require rendering the world a second time for each enabled volume, and are some of the most performance expensive effects in the game.

**Overlapping Navmeshes**: No bounds should overlap. Otherwise zombies will appear and disappear unexpectedly in multiplayer.

**Visibility Overlay**: The visibility menu in the editor sums the mesh complexity in each region. Ideally there should only be a few red zones.

**Item Icons**: Each item should have a proper icon in the inventory. One way to quickly preview the icon is to attach an orthographic camera in Unity, and tune the orthographic size before setting the size in the .dat file.

Age Appropriacy
---------------

All official and curated game content should be what is typically considered family-friendly. As such, there are various restrictions on the type of content that maps seeking curation are allowed implement.

Profanity
`````````

Curated maps should not contain profanity. Objects, story notes, NPC dialogue, quest descriptions, and other such text should be devoid of any profanity. Profanity is anything considered heavy or mild cursing, slurs, or strongly implied.

Occasionally, there may be situations where an alternative to traditional profanity is useful. Nonsense words such as *gosh*, *darn*, *dang*, *drats*, and *heck* are fine to be used. Soft implications—such as a cut-off at the end of dialogue or a lore note—can also be utilized, so long as they are carefully worded to be open to interpretation.

In some situations, it may be better to replace large swaths of text on content such as lore notes with *\[REDACTED]* or *\[UNINTELLIGIBLE]*. Such redactions should be open to interpretation as to what may have been intended, and make sense within the context of the source material. Redactions should not be treated as a method of censoring individual words.

Drugs, alcohol, and other substances
````````````````````````````````````

Explicit depictions of drugs, alcohol, and other substances is not allowed. Although, maps may implement more family-friendly content that is similar in idea, such as berry mixes instead of alcohol. Maps may also choose to implement content that merely has looser, more distant association. Such as vineyards, bottles, kegs, or distilleries.

Inappropriate content
`````````````````````

The depicition of sexual content, or explicit references regarding sexual content, are prohibited in all forms.

Stockpile Preparation
---------------------

Each curated map release is usually accompanied by a few cosmetics and skins in the game's item store. Royalties from the sales are shared with the mod team. Even if a project is not eligible for curation, it may be appropriate to have some support-the-creator items in the Stockpile. For example, the `Stockpile bundles <https://store.steampowered.com/itemstore/304930/browse/?searchtext=%22Rootbeer+Ranger+Bundle%22+%22Cottontail+Ops+Bundle%22>`_ created for the `Candyland map <https://steamcommunity.com/sharedfiles/filedetails/?id=1776871385>`_.

**File Sharing**: Ideally the items have been setup for use as clothes in-game, and then exported into a .unitypackage. This package will then be imported into the vanilla project.

**Curated Workshop Item**: Payment splits are handled by a hidden curated workshop item. Setting this up usually takes a few weeks for new contributors' bank and tax information to be processed.

**Bundles**: Two or three collections of sets with four to six items each. Bundles can either be a collection of loosely-related items, or a complete outfit. Outfit bundles should avoid having multiple items that take up the same cosmetic slot.

**Mystery Boxes**: Fifteen to twenty items of rare, epic, or legendary rarity. The box can be themed, but all of the items should be usable individually – avoiding things like a set of matching shirts and pants that cannot be easily mixed with other cosmetic pieces.

**Playtime Drops**: Ten to twenty items of uncommon rarity. Unlike mystery box contents, it is far more appropriate for playtime drops to have matching sets and simple recolors.
