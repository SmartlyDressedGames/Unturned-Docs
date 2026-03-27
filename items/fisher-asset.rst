.. _doc_item_asset_fisher:

Fisher Assets
=============

Fishers (or "fishing poles") are created from the ItemFisherAsset class. They are useables that allow for catching fish.

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

**Fish_Bite_Interval_Multiplier** *float*: Multiplier for interval before a fish takes the bait. Defaults to 1.

**FishingRewardMode** *enum*: ``Rod`` or ``WaterVolumes``. Defaults to ``Rod`` for backwards compatibility.

``Rod``: Fishing rod itself defines rewards. Ignore per-volume rewards.

``WaterVolumes``: Use per-volume (or per-level if volume unspecified) rewards. If level doesn't support volume rewards, fallback to ``Rod`` rewards.

.. seealso:: :ref:`Level Asset fishing properties <doc_assets_level:supports_fishing_volumes>`.

**CatchChallenge_Enabled** *bool*: If true, player must complete a challenge when fish takes the bait before catching. Defaults to false for backwards compatibility.

**CatchChallenge_CursorSize** *float*: Size of window item must be within to catch. Defaults to 0.2.

**CatchChallenge_Gravity** *float*: Downward acceleration while input is not held. Defaults to 1.

**CatchChallenge_Acceleration** *float*: Upward acceleration while input is held. Defaults to 1.

**CatchChallenge_UpperRestitution** *float*: How much velocity to preserve when bouncing off the top. Defaults to 0.5 (50%).

**CatchChallenge_LowerRestitution** *float*: How much velocity to preserve when bouncing off the bottom. Defaults to 0.5 (50%).

**CatchChallenge_CaptureSpeed** *float*: Multiplier for how quickly item is caught while within cursor. Defaults to 1 (100%).

**CatchChallenge_EscapeSpeed** *float*: Multiplier for how quickly the player loses while item is outside the cursor. Defaults to 1 (100%).
