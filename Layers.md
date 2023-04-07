**NOTICE:** *You are not reading the most up-to-date documentation. This file is old, and may not reflect the current modding or server capabilities. The latest documentation can be found at [Unturned Documentation](https://docs.smartlydressedgames.com/).*

*This file may be removed in the future. Refer to its more [up-to-date equivalent](https://docs.smartlydressedgames.com/en/stable/assets/layers.html) instead.*

Layers
======

Upfront: obviously Unturned makes poor use of Unity's Layers. This document exists as much for my personal reference as yours. My only defense is that these layers are entrenched from the earliest versions back in 2013, when I was 15 or 16.

Overview
--------

Built-in Layers
- 0 Default
- 1 TransparentFX
- 2 Ignore Raycast
- 4 Water: ocean and water tiles.
- 5 UI: menus with [uGUI glazier](Glazier.md) as well as plugin custom menus.

User Layers
- 8 Logic: clickable overlays like the position, rotation and scale handles. Editor debug visuals that can be seen through walls are on this layer.
- 9 Player: character capsule (not body hitboxes). Exists for all players server-side, but only the local player client-side.
- 10 Enemy: player body hitboxes.
- 11 Viewmodel: local first-person arms and weapon.
- 12 Debris: typically small simulated objects like ragdolls, grenades, falling tree trunks, destroyed structures, and fragmented objects.
- 13 Item: dropped interactable items.
- 14 Resource: trees and boulders. Barricades attached to vehicles are moved to this layer.
- 15 Large: large props placed in the level editor.
- 16 Medium: medium props placed in the level editor.
- 17 Small: small props without collision placed in the level editor.
- 18 Sky: distant effects without collision like the clouds and stars.
- 19 Environment: roads, grass and pebbles.
- 20 Ground: landscape / terrain.
- 21 Clip: invisible collision.
- 22 Navmesh: invisible zombie-only collision. Navmesh graphs are generated from this collision, but the collision is also loaded on the server to help push zombies around.
- 23 Entity: zombie and animal body hitboxes.
- 24 Agent: zombie and animal character capsules (not body hitboxes).
- 25 Ladder: invisible climbable trigger.
- 26 Vehicle: all vehicle colliders.
- 27 Barricade: barricade item placed in the world. Barricades attached to vehicles are moved to the Resource layer.
- 28 Structure: structure item placed in the world.
- 29 Tire: wheel colliders. Allows wheels to mask what they collide with.
- 30 Trap: typically trigger colliders including rocket launcher projectiles and kill volumes.
- 31 Ground2: no longer used after old maps were converted to terrain tiles. Previously this was for out-of-bounds terrain. Reserved for future use.

Layer Collision Matrix
----------------------

Note that these comments do **NOT** apply to collision queries like raycasts, spherecasts, etc.

No physics collision:
- Default
- TransparentFX
- Ignore Raycast
- Water
- UI
- Logic
- Enemy
- Viewmodel
- Small
- Sky
- Environment
- Ground
- Entity
- Ladder
- Ground2

Has physics collision:
- Player: character controller layer is used by Unity as the underlying query mask.
- Debris
- Item
- Resource
- Large
- Medium
- Environment
- Ground
- Clip: collides with Player and Vehicle for its original purpose. Makeshift vehicles have invisible colliders on this layer to expand their simulation size without affecting barricade placement, so Clip also collides with some of the same layers as Vehicle.
- Navmesh
- Agent: character controller layer is used by Unity as the underlying query mask.
- Vehicle
- Barricade
- Structure
- Tire: wheel collider layer is used by Unity as the underlying query mask.
- Trap
