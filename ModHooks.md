Mod Hooks
=========

Overview
--------

Script Components can be added to Game Objects in Unity and exported in Asset Bundles _IF_ they match a script in the base game code. These intentionally exportable scripts are referred to as __Mod Hooks__. They can be imported into a Unity project from the Project.unitypackage, and added to game objects inside the Unturned components menu. Each script makes several Events available which can drive other component properties like visibility or play an animation.

Originally proposed and coined by VitaxaRusModding in this GitHub issue: [Link](https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/435)

Collision Event Hook
--------------------

Events for player overlaps with a trigger collider. Primarily useful for server-side objects as collisions are not triggered by other players client-side, but this limitation may be resolved in the future.

Vehicle Event Hook
------------------

Events for driver entering and exiting the vehicle. These events are fired on server and client.

Weather Event Hook
------------------

Events for day, night, full moon, and weather. These events are fired on server and client.
