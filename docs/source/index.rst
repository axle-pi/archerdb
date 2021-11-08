ArcherDB
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

====================================

* :ref:`Overview`
* :ref:`Install`
* :ref:`Database`
* :ref:`Table`
* :ref:`Indexes`
* :ref:`Working with Data`
* :ref:`API`

|

:ref:test


.. Overview:

Overview
==========

|

What is ArcherDB?
+++++++++++++++++

ArcherDB is an in memory key-value database developed in Python. It is intended to
be used to store JSON serializable data with arbitrary structure. A single table can
be used to store various types of records, but new tables can be added to store different
types of data, and limited optional schema validation is planned to be added to enforce
data requirements on a table by table basis.

All operations are performed in memory, and database is periodically written to disk
so state can be maintained if database is shut down or application running it crashes.
Additionally all write operations are logged so any change to database state is
not lost on an unexpected shut down.

The primary classes included in ArcherDB are the :py:class:`~archerdb.database.Database` and :py:class:`~archerdb.table.Table` classes.

The :py:class:`~archerdb.database.Database` class is used to create a new database and add and drop tables.

A new :py:class:`~archerdb.table.Table` can be created for each type of record you want to save. For example, you may want to create a ``customers`` table and an ``inventory`` table if your application stores data on both.


|

.. Install:

Install
==========
ArcherDB can be found on [PyPI](https://pypi.org/project/archerdb/) and the easiest
way to install is using pip:

.. code-block:: python

    pip install archerdb

ArcherDB does not use any packages outside of the standard python library so
nothing else is required to start using!
|

.. Database:

Database
==========
Before adding Tables or records, a :py:class:`~archerdb.database.Database` instance must be created:

.. code-block:: python

    db = Database('./db')

When initializing a Database the path to the database directory (``./db``) in this example) should be provided.
The database directory will be used to put data and log files for the database. If a database has already
been created in the directory, its data will be loaded and the database will be the same as it was previously.

The data for the database will be put in ``${database_directory}/data/``

The transaction logs will be put in ``${database_directory}/log/``

|

.. Table:

Table
==========
A Database instance is used to create and drop tables:

.. code-block:: python

    users = db.addTable('players')
    teams = db.addTable('teams')

    db.show_tables()
    # ['players', 'teams']

    db.drop_table('teams')

    db.show_tables()
    # ['players']

A table name must be unique. If you pass an existing table name to ``db.add_table()`,
the existing table will be returned.

|

.. Indexes:

Indexes
==========

To improve search performance for common search patterns, consider adding one or more
indexes to a table. For example if a frequent access pattern of a `users` `~archerdb.table.Table` is to search
for a user based on id you may consider adding an index as show below. Note, the impact
of the index will be bigger if the table is larger.

.. code-block:: python

    t = db.add_table('users')
    t.add({'username': 'archerdb'})

    # add 10 million users with random usernames
    letters = string.ascii_lowercase
    for i in range(0, 10000000):
        username =  ''.join(random.choice(letters) for i in range(10))
        t.add({'username':username})

    start_time = time.time()
    t.search({'username':'archerdb'})
    # ['2002504a-783c-4643-a12c-ddec5d533987']
    elapsed_time = time.time() - start_time
    # elapsed_time = 5.515

    t.add_index('username')

    start_time = time.time()
    t.search({'username':'archerdb'})
    # ['2002504a-783c-4643-a12c-ddec5d533987']
    elapsed_time = time.time() - start_time
    # elapsed_time = 0.001

|

.. Working with Data:

Working with data
=================

Data records can be added, deleted, or fetched from a Table:

.. code-block:: python

    # Add records to users table
    id1 = users.add({'username' : 'axle', 'type':'admin', 'email': 'axle@archerdb.com'})
    id2 = users.add({'username' : 'sparks', 'type':'admin', 'email': 'sparks@archerdb.com'})
    id3 = users.add({'username' : 'support', 'type':'support', 'email': 'email@archerdb.com'})

    # get user by id
    user = users.get_by_id(id)
    # {'username': 'axle', 'type': 'admin', 'email': 'email@archerdb.com'}

    # search for user based on a field (username) and return ids.
    admin_ids = users.search({'type': 'admin'})
    #['aef9acfc-f93b-4106-949e-d8688b48f5b7', '257bd836-40a7-45cf-965f-dbb2e61fdabf']

    # search for user based on a field (username) and return documents.
    admins = users.search({'type': 'admin'}, True)
    #[{'username': 'axle', 'type': 'admin', 'email': 'email@archerdb.com'}, {'username': 'sparks', 'type': 'admin', 'email': 'sparks@archerdb.com'}]

    # delete a record
    users.delete('id3')


|

.. API:

API
==========

:py:class:`~archerdb.database.Database`

.. automodule:: archerdb.database
    :members:
    :special-members: __init__

|

:py:class:`~archerdb.table.Table`

.. automodule:: archerdb.table
    :members:
    :special-members: __init__
