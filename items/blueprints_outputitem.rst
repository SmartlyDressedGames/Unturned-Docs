.. _doc_item_asset_blueprints_outputitem:

Blueprint Output Items
======================

Configuration for a produced item in a :ref:`blueprint <doc_item_asset_blueprints>`.

Value Format
------------

For straightforward cases, a simple one-liner format is supported:

- {ID}
- {ID} x {Amount}
- this
- this x {Amount}

Examples:

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

	OutputItems
	[
		{
			// First output item properties
		}
		{
			// Second output item properties
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
   * - :ref:`Amount <doc_item_asset_blueprints_outputitem:amount>`
     - :ref:`uint8 <doc_data_builtin_types>`
     - ``1``
   * - :ref:`ID <doc_item_asset_blueprints_outputitem:id>`
     - :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`Item <doc_item_asset_intro>`
     -
   * - :ref:`Origin <doc_item_asset_blueprints_outputitem:origin>`
     - :ref:`doc_data_eitemorigin`
     - ``Craft``

----

.. _doc_item_asset_blueprints_outputitem:amount:

Amount :ref:`uint8 <doc_data_builtin_types>` ``1``
::::::::::::::::::::::::::::::::::::::::::::::::::

Quantity of this item created by the blueprint. Minimum value of one.

----

.. _doc_item_asset_blueprints_outputitem:id:

ID :ref:`Asset Pointer <doc_data_assetptr>` to :ref:`Item Asset <doc_item_asset_intro>`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This property can also be set to a string value of ``this``, which will use the the owning asset's ID. Useful for blueprints creating the owning asset to avoid accidentally writing the wrong ID.

----

.. _doc_item_asset_blueprints_outputitem:origin:

Origin :ref:`doc_data_eitemorigin` ``Craft``
::::::::::::::::::::::::::::::::::::::::::::

A kludge to override certain spawning properties. For example, setting the origin to ``Admin`` will cause items to spawn at full quality.
