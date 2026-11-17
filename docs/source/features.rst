Features
========

Connect to the Database
-----------------------
1. Import the :data:`~sqlitables.connection` module.
2. Use the :func:`~sqlitables.connection.connect` function to receive the connection.

.. code-block::

    from sqlitables import connection
    connection = connection.connect("~/foo/example.db")