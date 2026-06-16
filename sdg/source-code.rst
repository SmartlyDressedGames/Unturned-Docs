.. _doc_source_code:

Source Code
===========

Unturned's project files are available in a `GitHub repository <https://github.com/SmartlyDressedGames/U3-SDK>`_.

FAQ
---

**Q: Why make the game's source code available?**

**A:** Unturned's greatest strength is our passionate community. Releasing the source files allows you and other players to further build upon the game as you see fit. Building a lasting legacy for the game regardless of the changes we make or how many years pass from now.

**Q: Can I publish my derivate works on Steam?**

**A:** We intend to support this if possible. For more information about mods on Steam, please refer to: https://store.steampowered.com/about/communitymods/

**Q: Will the Steam version continue receiving updates?**

**A:** Yes, we plan to continue maintaining the official Steam version.

**Q: Will you accept pull requests?**

**A:** Our current goal is simply allowing players to create their own spin on the game. From minor balance changes and item additions, to total conversions with new gameplay elements. If there is significant community interest behind a mod we may reach out to collaborate in some form or another.

**Q: Will the project files be kept up-to-date with the version used by the official game?**

**A:** Yes, we plan to keep the source code in sync with the latest official releases.

**Q: Has any code been removed from this release?**

**A:** Yes, certain code we can't redistribute has been removed. For example, third-party pathfinding and anti-cheat libraries. If you have an appropriate license to use those libraries you may use the integration from the base game in your project if you wish.

**Q: Can I commercialize my mod?**

**A:** No, sorry, it must be strictly non-commercial. Please refer to the full license text for more details.

**Q: Are there any restrictions on mod naming?**

**A:** Your mod must not imply it was created or endorsed by SDG. For example, you cannot title your mod "Unturned 2". Please refer to the full license text for more details.

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

**Q: How can I report an issue?**

**A:** If it's related to the U3-SDK (as opposed to the vanilla game or a mod), please create an issue on the `GitHub Issue Tracker <https://github.com/SmartlyDressedGames/U3-SDK/issues>`_!

**Q: How can I report a security vulnerability?**

**A:** If you've found an exploit affecting the vanilla game, please don't create a publicly visible issue. Instead, send an email to info@smartlydressedgames.com.

**Q: Where can I get discuss development and ask questions?**

**A:** Many developers frequent the `GitHub Discussions <https://github.com/SmartlyDressedGames/U3-SDK/discussions>`_. It's a great place to meet fellow modders, and if you're polite someone might be kind enough to help you out!

**Q: How can I contribute?**

**A:** Two of the best ways you can get involved are helping out with a community fork (or starting one!), or participating in `Discussions <https://github.com/SmartlyDressedGames/U3-SDK/discussions>`_ (especially answering questions!).
