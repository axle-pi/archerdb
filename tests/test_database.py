import unittest
import os
import shutil
import json
from archerdb import Database

TEST_DB_DIR = 'testdb'
LOG_LINE_0 = {'class_name': 'Database', 'object_name': 'db', 'method': 'add_table', 'params': ['users']}
LOG_LINE_1 = {'class_name': 'Table', 'object_name': 'users', 'method': 'put', 'params': [{'username': 'test'}]}


class TestDatabase(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_DB_DIR):
            shutil.rmtree(TEST_DB_DIR)

        self.db = Database(TEST_DB_DIR)

    def tearDown(self):
        if os.path.exists(TEST_DB_DIR):
            shutil.rmtree(TEST_DB_DIR)

    def test_db_init(self):
        self.assertTrue(os.path.exists('{}/db'.format(TEST_DB_DIR)))
        self.assertTrue(os.path.exists('{}/log'.format(TEST_DB_DIR)))

    def test_transaction_logged(self):
        users = self.db.add_table('users')
        users.put({'username': 'test'})

        with open('{}/log/log.txt'.format(TEST_DB_DIR)) as f:
            lines = [json.loads(line.rstrip()) for line in f]
        self.assertEqual(2, len(lines))

        self.assertEqual(LOG_LINE_0, lines[0])
        self.assertEqual(LOG_LINE_1, lines[1])

    def test_transaction_replay(self):
        self.db.drop_table('users')
        self.db._replay(LOG_LINE_0)
        self.db._replay(LOG_LINE_1)

        self.assertEqual(['users'], self.db.show_tables())
        users = self.db.add_table('users')
        res = users.search({'username': 'test'})
        self.assertEqual(1, len(res))
        self.assertEqual({'username': 'test'}, users.get(res[0]))

if __name__ == '__main__':
    unittest.main()
