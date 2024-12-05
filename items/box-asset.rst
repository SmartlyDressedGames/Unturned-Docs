.. _doc_item_asset_box:

Box Assets
==========

Boxes are intended to be used as a part of the Steam Economy, rather than as in-game content. As such, none of its unique properties can be properly utilized by modders.

This inherits the :ref:`ItemAsset <doc_item_asset_intro>` class.

Item Asset Properties
---------------------

**GUID** *32-digit hexadecimal*: Refer to :ref:`GUID <doc_data_guid>` documentation.

**Type** *enum* (``Box``)

**ID** *uint16*: Must be a unique identifier.

Box Asset Properties
--------------------

**Generate** *int32*: The itemdefid granted by opening this box, which is used to display the correct UI element after an unbox.

**Destroy** *int32*: The itemdefid removed by opening this box, which is used to display the correct UI element after an unbox.

**Drops** *int32*: Corresponds to the total number of items in the box, so that the correct number of UI elements are displayed when showing box contents.

**Drop\_#** *int32*: The itemdefid of an item in the box, which is visually displayed as a UI element when showing box contents.

**Item_Origin** *enum* (``Unbox``, ``Unwrap``): The localization key to use for for the unbox/unwrap menu button.

**Probability_Model** *enum* (``Equalized``, ``Original``): UI elements regarding unbox probability chances are added depending on the specified enumerator.

**Contains_Bonus_Items** *bool*: When true, adds a UI element regarding bonus items.
