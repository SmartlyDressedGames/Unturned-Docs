.. _doc_mapping_curated:

Curated Maps
============

.. warning:: This program is still evolving. Some of this information could change, especially once we begin to accept the first maps under this new program!

Community-created maps that are officially linked from in-game are considered **Curated Maps**. Players can experience more high-quality content, and modders can earn money from their work while getting their creations highlighted.

We have introduced a new Curation Program for 2025 and beyond. Creating maps is intended to be a fun and rewarding hobby, and our new program should be more accessible to creators.

How does a map get accepted?
````````````````````````````

Our streamlined program starts with you simply publishing a map to the Steam Workshop. It looks something like this:

#. | You publish a cool map on the Steam Workshop.
#. | We reach out to authors of cool maps on the Steam Workshop.
#. | Legal agreements (e.g. establishing revenue share between co-authors).
#. | You make any changes necessary (if any).
#. | We commission artists (or you create) the contents of store bundles released alongside the map.
#. | Your curated map is added to the game.

While creating your map, we recommend gathering feedback from other players! Maps can be accepted at any time after being published, so authors can create and revise content without much worry.

Eligibility / Guidelines
------------------------

Several factors may influence our decisions when accepting new maps. First and foremost – curated maps should meet our guidelines (detailed further below).

.. tip:: We encourage working on projects even if they would not ineligible for curation. Creating a variety of Workshop content creates a valuable portfolio for future curation attempts, and may still benefit from being featured.

	Although not every map should be curated, we often feature non-curated maps in blogposts. Some particularly high-quality maps have received revenue share from Stockpile bundles.

Following these guidelines will significantly improve your eligibility:

Include Custom Content
``````````````````````

Maps should feel new and exciting to players. Although we may accept maps that primarily use vanilla assets, we strongly believe including some amount of custom content on new maps is important.

This helps make each map feel unique. Consider creating new items, having a unique architecture style for your towns, incorporating our modding features in innovative ways, and exploring game mechanics in different ways.

No Third-Party Content
``````````````````````

All content on the map must be an official asset from the base game, or be a custom asset that was created by you. We cannot accept maps that use assets from other people's mods (including other curated maps). Our modding documentation can help you get started!

Art Style
`````````

Curated experiences should still look and feel like *Unturned*. Any custom content on the map should generally match the base game's art style (similar to preexisting curated maps).

Human-like drawings such as faces and skulls should be blocky, similar to the in-game characters. This is a common source of revision requests from us.

Quality Assurance
`````````````````

* | **Asset Validation**: Running the game with the :ref:`-ValidateAssets <doc_asset_validation>` command-line flag should not produce any warnings or errors.

* | **English Text**: Having an English-speaking member of the mod team is recommended, and `MoltonMontro <mailto:moltonmontro@smartlydressedgames.com>`_ has offered to help with English-related questions. Most importantly in this regard is proper punctuation and grammar: while native English speakers can easily read incorrect punctuation, it is very helpful for non-native readers. Ironically this paragraph probably has some punctuation errors.

* | **Project Organization**: To prevent unintended assets from being exported into asset bundles, convention is to separate the project files into Sources and MasterBundle directories. Hawaii is split between a directory called "HawaiiMasterBundle" in the project root, and a Sources directory which contains all of the .blend, .mb, .xcf, .psd, .ai, etc files. When exporting the asset bundle this ensures only game files like .fbx and .prefab are included.

* | **Asset Duplication**: If multiple objects share identical prefabs, or use vanilla content, asset bundle size can be improved by sharing the same prefabs. For an example of this refer to the vanilla notes using Bundle_Override_Path.

* | **Water Reflections**: When using water volumes, only one should have planar reflections enabled. These reflections require rendering the world a second time for each enabled volume, and are some of the most performance expensive effects in the game.

* | **Overlapping Navmeshes**: No bounds should overlap. Otherwise zombies will appear and disappear unexpectedly in multiplayer.

* | **Visibility Overlay**: The visibility menu in the editor sums the mesh complexity in each region. Ideally there should only be a few red zones.

* | **Item Icons**: Each item should have a proper icon in the inventory. One way to quickly preview the icon is to attach an orthographic camera in Unity.

Content Appropriacy
````````````````````

Content should be what is typically considered "family-friendly". For example:

- | Text should be devoid of harsh profanity (anything considered heavy or mild cursing, slurs, or strongly implied). Some alternatives to traditional profanity include nonsense words (such as *gosh*, *darn*, *dang*, *drats*, and *heck*), cut-off text, or redactions (e.g., *\[REDACTED]* or *\[UNINTELLIGIBLE]*).

- | Explicit depictions of drugs, alcohol, and other substances is not allowed. Similar ideas with a looser association, such as berry mixes instead of alcohol; or things like vineyards, bottles, kegs, or distilleries; is allowed. Cigarettes, vaping, smoking, and tobacco are not allowed.

- | Text should be gender-neutral. For example, "Firefighter" instead of "Fireman."

- | Do not link to out-of-game content (for example, websites and phone numbers). We typically request phone numbers be changed to 555: https://en.wikipedia.org/wiki/555_(telephone_number)

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

Stockpile Preparation
---------------------

Each curated map release is usually accompanied by a few cosmetics and skins in the game's item store. Royalties from the sales are shared with the map author(s).

**File Sharing**: Ideally, the items have been setup for use as clothes in-game, and then exported into a .unitypackage. This package will then be imported into the vanilla project.

**Curated Workshop Item**: Payment splits are handled by a hidden curated workshop item. Setting this up usually takes a few weeks for new contributors' bank and tax information to be processed.

**Bundles**: Two or three collections of sets with four to six items each. Bundles can either be a collection of loosely-related items, or a complete outfit. Outfit bundles should avoid having multiple items that take up the same cosmetic slot.

**Mystery Boxes**: Fifteen to twenty items of rare, epic, or legendary rarity. The box can be themed, but all of the items should be usable individually – avoiding things like a set of matching shirts and pants that cannot be easily mixed with other cosmetic pieces.

**Craftable Items**: Ten to twenty items of uncommon rarity. Unlike mystery box contents, it is far more appropriate for craftable items to have matching sets and simple recolors.

FAQ
---

**Q. Are any maps planned to release under the previous program?**

Yes. There's several maps which predate this new program. We believe many of these will be released throughout 2025.

**Q. When's the earliest we could see maps release under this new program?**

Since there's already several curated maps releasing throughout this year, and some changes aren't ready for the new program yet, earliest would probably be end-of-year or sometime in 2026.

**Q. Are there any upcoming changes to this program?**

We're looking to revise the single-player map selection menu, and are considering additional ways players could support their favorite maps (e.g., a cosmetic that adds a small badge next to the player's name when they're playing on a specific map). This is all – to some extent – still subject to change.

**Q. Do curated maps receive updates?**

We may suggest some fixes or other adjustments necessary for the map to meet our expectations. However, additional content is largely left to the discretion of the map author(s).

**Q. What game modes can maps be accepted for?**

Maps designed for officially-supported modes (Survival, Arena) are the most likely to be accepted. We may occasionally consider some maps designed for popular custom game modes.

**Q. Can multiple maps be released together?**

If/when considering maps to release together, we'd like to ensure it makes sense to do so. For example, an arena map and a PvE-focused survival map. This is something we're still exploring.
