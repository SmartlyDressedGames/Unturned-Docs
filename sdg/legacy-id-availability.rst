.. _doc_legacy_id_availability:

Legacy ID Availability
======================

Ideally, new content should use GUIDs when possible.

Certain asset types—such as items—still rely heavily on legacy IDs. That said, they can be referenced by GUID in many cases. For example, NPC clothing and item spawn tables can reference items by GUID.

To find available legacy IDs:

#. Press ``F1`` in the main menu **Workshop** sub-menu.
#. Click **Export Asset IDs**.
#. Open ``Extras/AssetIDs/All Assets/Grouped by Legacy Category``.
#. Each legacy asset category (e.g., Items) has a corresponding ``Legacy ID Availability.csv`` file listing IDs and whether they are reserved for vanilla content.
