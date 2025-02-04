.. _doc_test_steam_items:

Testing Steam Items
===================

.. note:: Only applicable in development builds and the Unity editor.

A temporary test inventory can be loaded from a file named ``TestInventory.dat`` in the game folder.

It contains an ``Items`` list of dictionaries, each with the following properties:

DefinitionId :ref:`int32 <doc_data_builtin_types>`
::::::::::::::::::::::::::::::::::::::::::::::::::

Steam item definition ID. The item can exist locally, i.e., not in the Inventory Service.

----

Quantity :ref:`int32 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::::

Number of items in stack. Optional.

----

InstanceId :ref:`uint64 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

By default, a relatively stable instance ID is automatically created for each test item. Can optionally be overridden using this property if necessary.

----

Tags :ref:`string <doc_data_builtin_types>`
:::::::::::::::::::::::::::::::::::::::::::

Dynamic per-item tags. Optional. (e.g., manually specifying ragdoll effect, crafted mythical, and/or kill counter)

----

RagdollEffect *enum*
::::::::::::::::::::

Optional. Any of the ragdoll effect names.

----

ParticleEffect :ref:`uint16 <doc_data_builtin_types>` ``0``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Optional legacy ID of a mythical effect. Works as if the item were crafted with this mythical effect. Useful for testing mythical effects, however cosmetic items only work on the main menu. (Unboxed mythicals unfortunately use an older, less flexible system.)

----

KillCounter *enum*
::::::::::::::::::

Optional. Can be set to ``Player`` or ``Total``.
