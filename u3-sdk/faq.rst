.. _doc_sdk_faq:

FAQ
===

Unturned's project files are available in a `GitHub repository <https://github.com/SmartlyDressedGames/U3-SDK>`_.

General
-------

**Q: Why make the game's source code available?**

**A:** Unturned's greatest strength is our passionate community. Releasing the source files allows you and other players to further expand upon the game as you see fit, building a lasting legacy for the game regardless of the changes we make or how many years pass from now.

**Q: How will this affect cheat development? (Will cheating be easier?)**

**A:** The source code doesn't add much new information for cheat developers. High quality decompilations of Unturned already exist (reverse engineering the code), and we've previously shared the code's documentation. BattlEye's Unturned-specific anti-cheat code is still private (even we don't have access to it), and they will continue monitoring for any new cheats.

**Q: Can I publish my derivate works on Steam?**

**A:** We intend to support this if possible. For more information about mods on Steam, please refer to: https://store.steampowered.com/about/communitymods/

**Q: Will the Steam version continue receiving updates?**

**A:** Yes, we plan to continue maintaining the official Steam version.

**Q: Will the project files be kept up-to-date with the version used by the official game?**

**A:** Yes, we plan to keep the source code in sync with the latest official releases.

**Q: Is the game "Open Source" now?**

**A:** *Open Source* refers to the `Open Source Initiative <https://opensource.org/>`_'s `definition <https://opensource.org/osd>`_, which the current non-commercial license doesn't meet. Ideally, once we finish another game and are hopefully able to re-acquire certain rights, we'd like to re-license the U3 SDK under the `MIT License <https://opensource.org/license/mit>`_.

**Q: Do I need a paid Unity license?**

**A:** At the time of writing (2026-07-02), individuals and hobbyists earning less than $200,000 USD/year from their use of Unity are elligible for a free Unity Personal license. That being said, you should review `Unity's terms <https://unity.com/products>`_.

**Q: Will one-off custom forks cause fragmentation?**

**A:** Our hope is to see like-minded devs join together around a shared fork, collaborating on enhancements that benefit all of their projects. (*The whole is greater than the sum of its parts!*)

----

Technical
---------

**Q: Why is the SDK ignoring my settings?**

**A:** The SDK stores most save data (including certain settings) separately from the base game's save data. After you apply the same settings within the SDK they will be persisted.

**Q: How do I export a development build?**

**A:** The "development" build has additional logging, visualizations, and debug tools (e.g., the profiler) enabled. Within Unity open **Window > Unturned > Build Tool**. Select **Build Test** and once it completes run ``Builds/Test/Unturned.exe``.

**Q: How do I export release builds?**

**A:** The Windows, macOS, and Linux builds are intended for distribution through Steam as a standalone mod. Within Unity open **Window > Unturned > Build Tool** and select **Build Standalone Platforms**.

**Q: Can I host servers?**

**A:** Yes: servers for your mod are filtered according to the ``Name`` configured in ``Builds/Shared/ModInfo.json``. Development builds can run as either client or server, and the Unity editor can run a game server by enabling **Playing in Unity > Dedicated Server In Editor**.

**Q: Will my workshop mods work?**

**A:** By default, any regular Unturned workshop file should be compatible and automatically load. Note that upgrading your mod's Unity engine version may affect compatibility.

**Q: Will my plugins work?**

**A:** By default, most plugins for Unturned servers should be compatible. Custom code changes to your mod may affect compatibility. For example, renaming or removing code that plugins depend on will break compatibility with those plugins.

----

Contributing
------------

**Q: How can I contribute?**

**A:** Two of the best ways you can get involved are helping out with a community fork (or starting one!), or participating in `Discussions <https://github.com/SmartlyDressedGames/U3-SDK/discussions>`_ (especially answering questions!).

**Q: How can I report an issue?**

**A:** If it's related to the U3-SDK (as opposed to the vanilla game or a mod), please create an issue on the `GitHub Issue Tracker <https://github.com/SmartlyDressedGames/U3-SDK/issues>`_!

**Q: How can I report a security vulnerability?**

**A:** If you've found an exploit affecting the vanilla game, please don't create a publicly visible issue. Instead, send an email to info@smartlydressedgames.com.

**Q: Where can I get discuss development and ask questions?**

**A:** Many developers frequent the `GitHub Discussions <https://github.com/SmartlyDressedGames/U3-SDK/discussions>`_. It's a great place to meet fellow modders, and if you're polite someone might be kind enough to help you out!

**Q: Will you accept pull requests?**

**A:** Our current goal is simply allowing players to create their own spin on the game. From minor balance changes and item additions, to total conversions with new gameplay elements. If there is significant community interest behind a mod we may reach out to collaborate in some form or another.

----

Dependencies
------------

**Q: Has any code been removed from this release?**

**A:** Yes, certain code we can't redistribute has been removed. For example, third-party pathfinding and anti-cheat libraries. If you have an appropriate license to use those libraries you may use the integration from the base game in your project if you wish.

**Q: Why do zombies walk into walls?**

**A:** Smarter zombie navigation depends on the `A* Pathfinding Project <https://arongranberg.com/astar/>`_. If you have a license for this library, please feel free to use the integration from the base game.

**Q: Why do interaction and selection tint the entire model?**

**A:** Edge highlighting depends on a `Highlighting System Plugin <https://deepdreamgames.com/highlightingsystem.html>`_. If you have a license for this plugin, please feel free to use the integration from the base game.

**Q: Why does the water look so simple?**

**A:** Better water shaders and planar reflections depend on `Unity 4 Pro Standard Assets <https://docs.unity3d.com/462/Documentation/Manual/HOWTO-Water.html>`_. If you have a license for these assets, please feel free to use the integration from the base game.

**Q: Why are missing component warnings logged in some levels?**

**A:** Certain prefabs include `NavmeshCut Components <https://arongranberg.com/astar/documentation/stable/navmeshcut.html>`_ which can't be loaded without the pathfinding library.

----

Assets
------

**Q: Can I modify the core assets?**

**A:** We're comfortable with our *own* in-house assets being modified, however the core asset bundle has been intentionally excluded from the SDK. It contains some third-party licensed content (examples: community-submitted skins, audio files). Unfortunately, we don't have an easy and definitive list we can share of which assets are third-party versus created in-house. Thus we're unable to provide blanket permission for redistributing the entire set of core assets, or to advise on which specific assets could be relicensed or replaced.

**Q: How can large assets be included in source control?**

**A:** Internally, we use `Git LFS <https://git-lfs.com/>`_. The SDK's ``.gitattributes`` file is prepared for Git LFS, with a comment on the first line describing the setup.

**Q: Can I use Git LFS without enabling it on my public fork?**

**A:** One option is two use two repositories: a public repository containing your fork's source code, and a private downstream repository containing your asset files.

----

Restrictions
------------

**Q: Can I commercialize/monetize my mod?**

**A:** No, sorry, it must be strictly non-commercial. Please refer to the full license text for more details.

**Q: What is considered non-commercial?**

**A:** Players must be able to play and access all features and content of your mod for free. Taking payments (whether inside or outside the game) in return for in-game content or services is considered commercial use.

**Q: Can my mod accept donations?**

**A:** Accepting voluntary donations is fine. Providing in-game items, upgrades, benefits, etc for "donations" is considered commercial use.

**Q: Can I offer out-of-game benefits to Patrons?**

**A:** Yes, for example, special Discord roles for your donors is fine.

**Q: Can I enable ads and sponsorships on YouTube videos about my mod?**

**A:** Yes, this is not considered commercial use of the SDK.

**Q: Are there any restrictions on mod naming?**

**A:** Your mod must not imply it was created or endorsed by SDG. For example, you cannot title your mod "Unturned 2". Please refer to the full license text for more details.

**Q: What platforms can I develop my mod for?**

**A:** The SDK can target the same PC platforms as the Steam version of Unturned: Windows, macOS, and Linux (including Steam Deck). Please refer to the full license text for more details.

**Q: Do I need to publish the source code for my mod?**

**A:** No, you can keep your mod's code private if you wish.

**Q: How are custom forks' servers affected by moderation?**

Our server hosting guidelines only apply to servers that are accessible through Unturned's public server list. By default, servers hosted on forked projects are not visible in our public server list, although it is technically possible to make them appear there. Regardless of which version of the game a server is running, if it is listed in our public server list, it should comply with our server hosting guidelines.

That said, maintainers of forked projects are free to establish and enforce their own server hosting guidelines. If you host a server for a forked project, you would need to follow any rules they set, or you may be subject to moderation by that project's maintainers.
