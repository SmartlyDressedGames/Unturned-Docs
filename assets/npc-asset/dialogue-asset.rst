.. _doc_npc_asset_dialogue:

Dialogue Assets
===============

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Dialogue``)

**ID** *uint16*: Must be a unique identifier. Values less than 2,000 are reserved for official content.

Messages
--------

Properties pertaining to dialogue performed by the NPC. Dialogue can utilize conditions and rewards. Messages that meet all of their conditions will be shown, and can grant rewards when the message is shown. These are prefixed with ``Message_#_``. For example, ``Message_0_Condition_0_Type Flag_Bool``. For more information, refer to the documentation for :ref:`Conditions <doc_npc_asset_conditions>` and :ref:`Rewards <doc_npc_asset_rewards>` respectively.

**Messages** *int32*: Total number of possible messages.

**Message_#_Pages** *byte*: Total number of pages the message has.

**Message_#_Responses** *byte*: Total number of responses to be shown when this message is shown. If 0, then all messages are automatically a candidate to be shown. Defaults to 0.

**Message_#_Response_#** *byte*: Index of the response to show.

**Message_#_Prev** *uint16* or *GUID*: ID or GUID of dialogue to return to if there are no responses available for this message. Defaults to 0.

**Message_#_FaceOverride** *byte*: Optional index of face image to use when this message is opened. Face is reset to character's default when unspecified or when dialogue is closed.

Responses
---------

Properties pertaining to dialogue available to the player. Dialogue can utilize conditions and rewards. Responses are only visible when conditions are met, and can grant rewards when selected. These are prefixed with `Response_#_`. For example, `Response_0_Reward_0_Type Quest`. For more information, refer to the documentation for :ref:`Conditions <doc_npc_asset_conditions>` and :ref:`Rewards <doc_npc_asset_rewards>` respectively.

**Responses** *byte*: Total number of possible responses.

**Response_#_Messages** *byte*: Total number of messages to only show this response for. If 0, then it is shown for all messages. Defaults to 0.

**Response_#_Message_#** *uint16*: Index of the message to show for.

**Response_#_Dialogue** *uint16* or *GUID*: ID or GUID of the dialogue to open when selected.

**Response_#_Quest** *uint16* or *GUID*: ID or GUID of the quest to preview when selected.

**Response_#_Vendor** *uint16* or *GUID*: ID or GUID of the vendor to open when selected.

Localization
------------

**Message_#_Page_#** :ref:`doc_data_richtext`: Text shown for the corresponding message page.

**Response_#** :ref:`doc_data_richtext`: Text shown for the corresponding response option.
