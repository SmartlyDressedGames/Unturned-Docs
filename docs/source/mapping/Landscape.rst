.. _doc_mapping_landscape:

Landscape
=========

Considerations
--------------

Upgrading terrain from the legacy editor to the devkit editor is not necessarily recommended.

**Pros:**

* Height sculpting and material painting tools are better.
* Each 1km x 1km tile has its own set of 8 materials rather than 8 for the entire level.

**Cons:**

* Devkit is not user-friendly, and improvements to it have been voted low priority.
* Not all legacy editor features were ported (yet?), so the landscape has to be edited separately from roads, lighting, etc.

Upgrade Legacy Terrain to Landscape
-----------------------------------

1. Level should have only one Landscape instance spawned from the Type Browser.
2. Open the Ground Upgrade Wizard.
3. Assign materials in the same order as in the original map editor. For example, if dirt is top of the list in the legacy editor then assign dirt to material slot #0.
4. Click upgrade and wait for the data to transfer. This may take a while.
5. Save the level.
6. Change ``Use_Legacy_Ground`` to false in the `Level Config <LevelConfig.md>`_ file.
