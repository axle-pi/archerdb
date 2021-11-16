ArcherDB
========



Contents
--------

.. toctree::
   :maxdepth: 1

   install
   quickstart
   data_storage_and_logs
   api

|

What is ArcherDB?
+++++++++++++++++

ArcherDB is an in memory key-value database developed in Python. It is intended to
be used to store JSON serializable data with arbitrary structure. A single table can
be used to store various types of records, but new tables can be added to store different
types of data.

All operations are performed in memory, and database is periodically written to disk
so state can be maintained if database is shut down or application running it crashes.
Additionally all write operations are logged so any change to database state is
not lost on an unexpected shut down.

The primary classes included in ArcherDB are the :py:class:`~archerdb.database.Database` and :py:class:`~archerdb.table.Table` classes.

The :py:class:`~archerdb.database.Database` class is used to create a new database and add and drop tables.

A new :py:class:`~archerdb.table.Table` can be created for each type of record you want to save. For example, you may want to create a ``customers`` table and an ``inventory`` table if your application stores data on both.


|


.. include:: install.rst