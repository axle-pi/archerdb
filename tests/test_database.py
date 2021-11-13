import unittest
import os
from archerdb import Database

TEST_DB_DIR = 'testdb'


class TestDatabase(unittest.TestCase):

    def test_db_init(self):
        if os.path.exists('{}/db'.format(TEST_DB_DIR)):
            os.remove('{}/db'.format(TEST_DB_DIR))
        if os.path.exists('{}/log'.format(TEST_DB_DIR)):
            os.remove('{}/log'.format(TEST_DB_DIR))

        db = Database(TEST_DB_DIR)
        self.assertTrue(os.path.exists('{}/db'.format(TEST_DB_DIR)))
        self.assertTrue(os.path.exists('{}/log'.format(TEST_DB_DIR)))


if __name__ == '__main__':
    unittest.main()
