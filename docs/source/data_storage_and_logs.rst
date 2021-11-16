Data storage and Logs
=====================

Database in memory
------------------

ArcherDB saves tables, indexes and records in memory. This makes writing and
reading data very fast.

The Database stores all this data in a Python dictionary, with table names as keys
and Table object as values:

.. code-block:: python

    >>> db = Database('./db')
    >>> db.add_table('users')
    >>> db.add_table('games)
    >>> db.db
    {'users': <archerdb.table.Table object at ...>, 'games': <archerdb.table.Table object at ...>}

Rather than directly manipulating the `db.db` field, it is recommended to use the APIs
exposed on `Table` object: `t = db.get_table('users')`.

|

Database on disk
----------------

To provide durability, the database contents are periodically saved to disk in
a json file. The database is saved in `<db directory>/db` directory. When database
is restarted, this file is used to rebuild the database to the state it was in
previously. You can also create a new database by putting a `data.json` file in this
path before creating a database. To do this, `data.json` should be formatted like below,
with each table name as a key with table data as its value.

.. code-block:: javascript

    {
      "users":
        {
          "record-001": {<record data>},
          "record-002": {<record data>},
          "record-004": {<record data>},
          ...
        }
    }

|

Logs
----

Write operations on the database or a table are also written to a log file. The
log file is located at `<db directory>/log`. The log files are used to return the
database to the correct state if recreated after an unexpected shutdown.