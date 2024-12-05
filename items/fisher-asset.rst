.. _doc_item_asset_fisher:

Fisher Assets
=============

Fishers (localized as "fishing poles") are useables that allow for catching fish.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Fisher``)

**Useable** *enum* (``Fisher``)

**ID** *uint16*: Must be a unique identifier.

Fisher Asset Properties
-----------------------

**Reward_Experience_Min** *int32*: Minimum amount (inclusive) of experience to grant upon successfully catching something. Defaults to 3.

**Reward_Experience_Max** *int32*: Maximum amount (inclusive) of experience to grant upon successfully catching something. Defaults to 3.

**Reward_ID** *uint16*: Legacy ID of the spawn table a reward should be generated from upon successfully catching something with the fishing pole.

Fishing poles can use quest rewards. Refer to :ref:`Rewards <doc_npc_asset_rewards>` documentation for additional documentation. These rewards are prefixed with ``Quest_``. For example, ``Quest_Rewards 1``.

