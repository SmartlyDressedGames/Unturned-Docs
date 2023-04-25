.. _doc_data_richtext:

Rich Text
=========

Certain text blocks support **rich text** markup. These are tags which modify the appearance of the text for example bold, italics, colors, etc.

Which tags are supported depends on the :ref:`doc_glazier` mode being used. Most players will be using the default, uGUI.

Extended Tags
-------------

These tags are specific to *Unturned*.

**\<br\>**: New line. Supported in most multi-line text boxes such as dialogue, signs/notes, item descriptions, etc.

**\<name_npc\>**: Insert the NPC character's name. Only supported in NPC dialogue.

**\<name_char\>**: Insert the player character's name. Only supported in NPC dialogue and signs/notes.

**\<pause\>**: Pause dialogue for 0.5 seconds before continuing. Only supported in NPC dialogue.

uGUI - TextMesh Pro (default)
-----------------------------

For the full list of tags please refer to the TextMesh Pro documentation here: https://docs.unity3d.com/Packages/com.unity.textmeshpro@2.2/manual/RichText.html

IMGUI
-----

For the full list of tags please refer to the Unity styled text documentation here: https://docs.unity3d.com/2018.3/Documentation/Manual/StyledText.html
