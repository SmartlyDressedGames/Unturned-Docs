.. _doc_source_code:

Source Code
===========

We are hoping to release Unturned's source code in 2025. This would allow anyone to create their own spin on the game. From minor balance changes and item additions, to total conversions with new gameplay elements.

.. warning:: **This information is subject to change.** Details and timelines regarding the release could be different. There's a lot of moving parts we need to consider as we work towards this goal!

There are some major obstacles that need to be addressed before we can achieve this. Some of these include:

1. | Seeking legal advice. We need to review any existing license agreements, determine any intellectual property we should retain (e.g., the "Unturned" trademark for future games), and more advice about open sourcing the project.

2. | Replacing third-party code and assets that cannot be open sourced. Most of the game's code should already be open sourceable. Certain third-party assets likely cannot be included, and some code will need to be replaced from scratch. As examples: edge highlighting should be converted to Unity's post-processing stack, water—currently a Unity 4 asset—will need a fallback, and zombie pathfinding may be able to use Unity's newer navmesh system.

Tackling these issues – and others – is necessary before the game is made open source.

FAQ
---

**Q. Will the official Steam version continue receiving updates?**

Yes—we plan to continue maintaining the official Steam version with new content updates and bug fixes.

**Q. Why do you want to make the game open source?**

Unturned's greatest strength is our passionate community. Releasing the source files allows you and other players to further build upon the game as you see fit. Building a lasting legacy for the game regardless of the changes we make or how many years pass from now.

**Q. Will you accept pull requests?**

Our current goal is to simply allow players to create their own derivatives of the game. However – we haven't completely ruled this out, and we're sure there's interest in seeing community-contributed code accepted into the game.

**Q. Will the open source project be kept up-to-date with the version used by the official game?**

This is our current intention.

**Q. Is there anything I can't do/use?**

This is an example of something that requires further legal review before we're comfortable giving an answer.

**Q. Is there anything that WON'T be available?**

Yes. Some content will be intentionally stripped from the open source version of the project. For example, support for the BattlEye anti-cheat. This is something that requires further review before we're comfortable giving an exhaustive list.

**Q. Could I publish my derivative work on Steam?**

This requires more legal review (and consulting with Steam)! Ideally, something like that would be permissible. Possibly similar to how some games' mods (e.g., for Portal 2 and Team Fortress 2) have dedicated Store pages. https://store.steampowered.com/about/communitymods/

**Q. Will there be documentation?**

We are not focused on creating documentation specifically for this purpose. However, some preexisting documentation may be helpful, along with any comments included in the source code. Community-contributed documentation on this topic may be accepted.

**Q. Will other versions of Unturned (1.x, 2.x) become open-source?**

We may explore this idea in the future, but this is not a priority for us at this time.
