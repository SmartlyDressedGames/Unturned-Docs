.. _doc_data_flag:

Flag
====

Placeholder text about flags. Flag properties don't require specifying a value. Instead, simply including the property name will include it.

.. attention::

    The :ref:`doc_data_file_format` page includes several data types currently (flag, color, vector3). Maybe those should be moved out of that doc, into their own things?

Some older asset types look for the presence of a particular key, not its value. These are referred to as flags. Their value can be left empty.

For example: item assets check for the ``Pro`` flag marking them is a Steam economy item.

.. code-block:: text

	Flag1
	Flag2