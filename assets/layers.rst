.. _doc_assets_layers:

Layers
======

Upfront: obviously Unturned makes poor use of Unity's Layers. This document exists as much for my personal reference as yours. My only defense is that these layers are entrenched from the earliest versions back in 2013, when I was 15 or 16.

Overview
--------

Built-in Layers

- **0 Default**
- **1 TransparentFX**
- **2 Ignore Raycast**
- **4 Water**: ocean and water tiles.
- **5 UI**: menus with :ref:`uGUI glazier <doc_glazier>` as well as plugin custom menus.

User Layers

- **8 Logic**: Clickable overlays like the position, rotation and scale handles. Editor debug visuals that can be seen through walls are on this layer.
- **9 Player**: Character capsule (not body hitboxes). Exists for all players server-side, but only the local player client-side.
- **10 Enemy**: Player body hitboxes.
- **11 Viewmodel**: Local first-person arms and weapon.
- **12 Debris**: Typically small simulated objects like ragdolls, grenades, falling tree trunks, destroyed structures, and fragmented objects.
- **13 Item**: Dropped interactable items.
- **14 Resource**: Trees and boulders. Barricades attached to vehicles are moved to this layer.
- **15 Large**: Large props placed in the level editor.
- **16 Medium**: Medium props placed in the level editor.
- **17 Small**: Small props without collision placed in the level editor.
- **18 Sky**: Distant effects without collision like the clouds and stars.
- **19 Environment**: Roads, grass and pebbles.
- **20 Ground**: Landscape / terrain.
- **21 Clip**: Invisible collision.
- **22 Navmesh**: Invisible zombie-only collision. Navmesh graphs are generated from this collision, but the collision is also loaded on the server to help push zombies around.
- **23 Entity**: Zombie and animal body hitboxes.
- **24 Agent**: Zombie and animal character capsules (not body hitboxes).
- **25 Ladder**: Invisible climbable trigger.
- **26 Vehicle**: All vehicle colliders.
- **27 Barricade**: Barricade item placed in the world. Barricades attached to vehicles are moved to the Resource layer.
- **28 Structure**: Structure item placed in the world.
- **29 Tire**: Wheel colliders. Allows wheels to mask what they collide with.
- **30 Trap**: Typically trigger colliders including rocket launcher projectiles and kill volumes.
- **31 Ground2**: No longer used after old maps were converted to terrain tiles. Previously this was for out-of-bounds terrain. Reserved for future use.

Layer Collision Matrix
----------------------

Note that these comments do **NOT** apply to collision queries like raycasts, spherecasts, etc.

No physics collision:

- **Default**
- **TransparentFX**
- **Ignore Raycast**
- **Water**
- **UI**
- **Logic**
- **Enemy**
- **Viewmodel**
- **Small**
- **Sky**
- **Environment**
- **Ground**
- **Entity**
- **Ladder**
- **Ground2**

Has physics collision:

- **Player**: Character controller layer is used by Unity as the underlying query mask.
- **Debris**
- **Item**
- **Resource**
- **Large**
- **Medium**
- **Environment**
- **Ground**
- **Clip**: Collides with Player and Vehicle for its original purpose. Makeshift vehicles have invisible colliders on this layer to expand their simulation size without affecting barricade placement, so Clip also collides with some of the same layers as Vehicle.
- **Navmesh**
- **Agent**: Character controller layer is used by Unity as the underlying query mask.
- **Vehicle**
- **Barricade**
- **Structure**
- **Tire**: Wheel collider layer is used by Unity as the underlying query mask.
- **Trap**
