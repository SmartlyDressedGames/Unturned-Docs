.. _doc_data_flag:

Flag
====

Some asset types have properties that only look for the presence of a particular key, rather than a key-value pair. These are referred to as flags. Their value can be left empty, since flags do not have a value paired to them.

For example, item assets check for the ``Pro`` flag. An item asset that included this flag is marked as a Steam economy item.

.. code-block:: text

	Flag1
	Flag2
	Flag3