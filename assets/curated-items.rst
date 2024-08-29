.. _doc_curated_items:

Curated Items
=============

Community-created cosmetic items can be submitted for inclusion in the game through the `"Stockpile Submissions" section of the Steam Workshop <https://steamcommunity.com/workshop/browse/?appid=304930&section=mtxitems>`_.

Accepted items are sold in the `item store <https://store.steampowered.com/itemstore/304930/>`_. The default revenue share is 25%, but for items associated with maps (e.g. the `Elver Map Bundle <https://store.steampowered.com/itemstore/304930/detail/1103/>`_) the revenue share is 50%.

Requirements
------------

Some additional preparation is needed compared with regular gameplay items:

#. Following the style rules
#. Organizing your Unity project
#. Exporting a Unity package
#. Specifying Mythical effect placement

Style Rules
-----------

.. |ico1| image:: img/1e1e1e.png
	:width: 15px

.. |ico2| image:: img/f0f0f0.png
	:width: 15px

There are several rules for cosmetic items to help promote consistency with the Unturned's art style, seeing as they will be integrated directly into the game:

#. Please avoid super high-contrast colors. They can be painful to look at, especially when used in harsh lighting. Most official content has medium-intensity colors.
#. Following this, please do not go darker than |ico1| #1e1e1e or brighter than |ico2| #f0f0f0. Both extremes of brightness will not play nicely with the game's lighting.
#. Flat forest/snow/desert/urban camouflages are reserved for in-game items like the ghillie suit. You are, however, allowed to incorporate patterned camouflage into your cosmetics.
#. Corners of models should not be beveled. Most models should have sharp edges (e.g., ninety degrees). There is not a limit on vertex/triangle/polygon count because anything matching the art style will naturally have a reasonable number.
#. Edges of clothing should have a slightly darker border one pixel wide. This can be easily seen on official clothing items, along the cuffs and bottom hem of shirts.
#. Only use copyrighted content, trademarks, and other intellectual property that belongs to you.

Unity Project Organization
--------------------------

Organizing your project into an export folder for your asset-bundled files (e.g. ``Item.prefab``) and a sources folder for the imported files is greatly appreciated.

This makes it much easier to ensure only the necessary assets are included in the game. As an example, if a source ``.blend`` file were in the asset-bundled folder any unused/intermidiary meshes would accidentally get exported as well.

All of the base game's exported assets are in the ``Assets/CoreMasterBundle`` folder, and all of the source files are in the ``Assets/Game/Sources`` folder.

Cosmetic organization:

- Map-related cosmetics are in per-map folders and prefixed with the map name. For example, Arid's Arrowhead item export files are located in ``Assets/CoreMasterBundle/Items/Arid/Arid_Arrowhead`` and the source files are in ``Assets/Game/Sources/Items/Arid``.
- Sets of items are in a per-outfit folder and prefixed with the outfit name. For example, the Cultist bundle's mask item export files are located in ``Assets/CoreMasterBundle/Items/Outfits/Cultist/Cultist_Mask`` and the source files are in ``Assets/Game/Sources/Items/Outfits/Cultist``.
- Miscellaneous items are in the folder matching their type. For example, the Turtle Backpack exported files are located in ``Assets/CoreMasterBundle/Items/Backpacks/Turtle_Backpack`` and the source files are in ``Assets/Game/Sources/Items/Backpacks/Turtle_Backpack``.

Exporting Unity Package
-----------------------

Since the assets for accepted cosmetics are included in the core asset bundle, a ``.unitypackage`` file is needed along with the regular ``.dat`` files. To export the package:

#. Select the folders containing your ``Item.prefab`` files. For example, if submitting the vanilla fedora you would select the ``Assets/CoreMasterBundle/Items/Hats/Fedora`` folder.
#. Right-click in the **Project** window
#. Click **Export Package...**
#. Ensure **Include dependencies** is checked to include the files that aren't directly placed in the asset bundles (meshes, materials, textures, etc).

.. note::

	The Unity package is in *addition* to the regular asset ``.dat`` and ``English.dat`` files. Including the ``.dat`` files from your setup is useful for keeping the accepted version consistent. While not strictly necessary, including a name and description in the English text file is appreciated and will probably be used.

Mythical Effect Placement
-------------------------

If the item will have mythical effects the Item.prefab needs an "Effect" child transform. The orientation is rather unfortunate: +Z is the mythical's up direction and +Y is the mythical's forward direction.

.. figure:: img/EffectTransform.png

	Example "Effect" transform positioning and orientation.
