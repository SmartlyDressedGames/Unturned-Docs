.. _doc_item_asset_blueprints_inputitem:

Blueprint Input Items
=====================

Configuration for a required ingredient item in a :ref:`blueprint <doc_item_asset_blueprints>`.

Value Format
------------

For straightforward cases, a simple one-liner format is supported:

- {ID}
- {ID} x {Amount}
- this
- this x {Amount}

For examples:

.. code-block:: unturneddat

	// Canned Beans:
	78fefdd23def4ab6ac8301adfcc3b2d4

	// Or, using Canned Beans' legacy ID:
	13

	// Two cans of beans:
	13 x 2

	// Owning asset:
	this

	// Two of owning asset:
	this x 2

Dictionary Format
-----------------

Unlike the shorter format above, using these properties requires the ``{ }`` :ref:`dictionary <doc_data_file_format>` format. For example:

.. code-block:: unturneddat

	InputItems
	[
		{
			// First input item properties
		}
		{
			// Second input item properties
		}
	]

Properties
``````````

.. list-table::
   :widths: 40 40 20
   :header-rows: 1

   * - Property Name
     - Type
     - Default Value
   * - :ref:`Amount <doc_item_asset_blueprints_inputitem:amount>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`AllowEmpty <doc_item_asset_blueprints_inputitem:allowempty>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`AllowFull <doc_item_asset_blueprints_inputitem:allowfull>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`AllowMaxQuality <doc_item_asset_blueprints_inputitem:allowmaxquality>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`CountEmptyAsOne <doc_item_asset_blueprints_inputitem:countemptyasone>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`CountingMethod <doc_item_asset_blueprints_inputitem:countingmethod>`
     - :ref:`ECraftingInputCountingMethod <doc_item_asset_blueprints_inputitem:ecraftinginputcountingmethod_enumeration>`
     - See description
   * - :ref:`Critical <doc_item_asset_blueprints_inputitem:critical>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``false``
   * - :ref:`Delete <doc_item_asset_blueprints_inputitem:delete>`
     - :ref:`bool <doc_data_builtin_types>`
     - ``true``
   * - :ref:`ID <doc_item_asset_blueprints_inputitem:id>`
     - :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`Item <doc_item_asset_intro>`
     -
   * - :ref:`Prioritization <doc_item_asset_blueprints_inputitem:prioritization>`
     - :ref:`ECraftingInputPrioritization <doc_item_asset_blueprints_inputitem:ecraftinginputprioritization_enumeration>`
     - See description

.. _doc_item_asset_blueprints_inputitem:ecraftinginputprioritization_enumeration:

ECraftingInputPrioritization Enumeration
````````````````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``LowestAmount``
     - Sort items with lowest "amount" to front of list.
   * - ``HighestAmount``
     - Sort items with highest "amount" to front of list.
   * - ``LowestQuality``
     - Sort items with lowest quality% to front of list.
   * - ``HighestQuality``
     - Sort items with highest quality% to front of list.

.. _doc_item_asset_blueprints_inputitem:ecraftinginputcountingmethod_enumeration:

ECraftingInputCountingMethod Enumeration
````````````````````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
   * - ``TotalItems``
     - Sum up number of items found, ignoring amount.
   * - ``TotalAmount``
     - Sum up "amount" of each item. Optionally counting zero as one.

----

.. _doc_item_asset_blueprints_inputitem:amount:

Amount :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Quantity of this item needed to craft the blueprint. Minimum value of one.

----

.. _doc_item_asset_blueprints_inputitem:allowempty:

AllowEmpty :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, items with an "amount" of zero are included in eligible supplies. Otherwise, they are ignored (default).

Defaults to ``true`` if ``CountEmptyAsOne`` is true.

This option exists primarily for the ``FillTargetItem`` operation's internal use.

----

.. _doc_item_asset_blueprints_inputitem:allowfull:

AllowFull :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, items with an "amount" greather than or equal to their maximum amount are ignored. Otherwise, they are eligible (default).

This option exists primarily for the ``FillTargetItem`` operation's internal use.

----

.. _doc_item_asset_blueprints_inputitem:allowmaxquality:

AllowMaxQuality :ref:`bool <doc_data_builtin_types>` ``true``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, items with quality of 100% are eligible (default). Otherwise, they are ignored.

This option exists primarily for the ``RepairTargetItem`` operation's internal use.

----

.. _doc_item_asset_blueprints_inputitem:countemptyasone:

CountEmptyAsOne :ref:`bool <doc_data_builtin_types>` ``false``
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, items with an "amount" of zero are included in eligible supplies as amount 1.

This option is used in vanilla for salvaging empty magazines.

----

.. _doc_item_asset_blueprints_inputitem:countingmethod:

CountingMethod :ref:`ECraftingInputCountingMethod <doc_item_asset_blueprints_inputitem:ecraftinginputcountingmethod_enumeration>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Determines how available amount of this input is calculated.

Defaults to ``TotalItems`` unless ``Operation`` is ``FillTargetItem`` in which case ``TotalAmount`` is used.

----

.. _doc_item_asset_blueprints_inputitem:critical:

Critical :ref:`bool <doc_data_builtin_types>` ``false``
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, the blueprint is hidden from the crafting menu if this input item is missing.

Useful for blueprints that aren't relevant to the player without a specific item. For example, the first input item of a ``FillTargetItem`` blueprint is often marked ``Critical``.

----

.. _doc_item_asset_blueprints_inputitem:delete:

Delete :ref:`bool <doc_data_builtin_types>` ``true``
::::::::::::::::::::::::::::::::::::::::::::::::::::

If true, this item is consumed when crafting the blueprint.

If false, this item is marked as a "Tool" in the crafting menu. (For example, a Saw item required to cut wood.)

----

.. _doc_item_asset_blueprints_inputitem:id:

ID :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`Item Asset <doc_item_asset_intro>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property can also be set to a string value of ``this``, which will use the the owning asset's ID. Useful for Salvage blueprints to avoid accidentally writing the wrong ID.

----

.. _doc_item_asset_blueprints_inputitem:prioritization:

Prioritization :ref:`ECraftingInputPrioritization <doc_item_asset_blueprints_inputitem:ecraftinginputprioritization_enumeration>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Controls which items are used first. For example, whether to use the lowest quality items first.

Defaults to ``LowestQuality`` unless ``Operation`` is ``FillTargetItem`` in which case ``LowestAmount`` is used.
