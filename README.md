<img align="right" src="https://raw.githubusercontent.com/axle-pi/archerdb/main/docs/_static/logo_only.svg" alt="logo" width="70px"> 


# ArcherDB



- [Documentation](#documentation)
- [Quick start](#quickStart)
- [Install](#install)

<a id="documentation"></a>

# Documentation

See latest [docs](https://archerdb.readthedocs.io/en/latest/)

<a id="quickStart"></a>

# Quick start

```python
>>> from archerdb import Database

# Create db with 1 table
>>> db = Database('./db')
>>> users = db.add_table('users')

# Add document to users table
>>> id_1 = users.put({'username' : 'axle', 'type':'admin', 'email': 'axle@archerdb.com'})
>>> id_2 = users.put({'username' : 'sparks', 'type':'admin', 'email': 'sparks@archerdb.com'})
>>> id_3 = users.put({'username' : 'support', 'type':'support', 'email': 'email@archerdb.com'})

# get user by id
>>> user = users.get(id_1)
# {'username': 'axle', 'type': 'admin', 'email': 'axle@archerdb.com'}

# search for user based on a field (username) and return ids.
>>> admin_ids = users.search({'type': 'admin'})
# ['aef9acfc-f93b-4106-949e-d8688b48f5b7', '257bd836-40a7-45cf-965f-dbb2e61fdabf']

# search for user based on a field (username) and return documents.
>>> admins = users.search({'type': 'admin'}, True)
# [{'username': 'axle', 'type': 'admin', 'email': 'axle@archerdb.com'}, {'username': 'sparks', 'type': 'admin', 'email': 'sparks@archerdb.com'}]
```

<a id="install"></a>

# Install

ArcherDB is available on PyPI

[View on PyPI](https://pypi.org/project/archerdb/)

```
$ pip install archerdb
```

