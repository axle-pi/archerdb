import unittest
from archerdb import Table, constants

TEST_DB_DIR = 'testdb'
TEST_RECORD = {'username': 'tester', 'email': 'tester@archerdb.com',
               'type': 'admin'}
TEST_RECORD_2 = {'username': 'tester2', 'email': 'tester3@archerdb.com',
                 'type': 'limited'}
TEST_RECORD_3 = {'username': 'tester3', 'email': 'tester3@archerdb.com',
                 'type': 'limited'}


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        constants.initialize_constants('./testDb', False)

    def test_table_init(self):
        table = Table('test', {})
        self.assertEqual(table.name, 'test')
        self.assertEqual(table.records, {})
        self.assertEqual(table.index, {})

    def test_put_record(self):
        table = Table('test', {})
        rec_id = table.put(TEST_RECORD)
        record = table.get(rec_id)
        self.assertEqual(record, TEST_RECORD)

    def test_delete_record(self):
        table = Table('test', {})
        rec_id = table.put(TEST_RECORD)
        table.delete(rec_id)
        record = table.get(rec_id)
        self.assertEqual(record, False)

    def test_search_record(self):
        table = Table('test', {})
        rec_id = table.put(TEST_RECORD)
        rec_id2 = table.put(TEST_RECORD_2)
        rec_id3 = table.put(TEST_RECORD_3)

        res = table.search({'type': 'admin'})
        self.assertEqual(res, [rec_id])
        res = table.search({'type': 'admin'}, True)
        self.assertEqual(res, [TEST_RECORD])

        res = table.search({'type': 'limited'})
        self.assertEqual(res, [rec_id2, rec_id3])
        res = table.search({'type': 'limited'}, True)
        self.assertEqual(res, [TEST_RECORD_2, TEST_RECORD_3])

    def test_add_and_remove_index(self):
        table = Table('test', {})
        table.add_index('username')
        self.assertEqual(len(table.index), 1)
        self.assertTrue('username' in table.index)

        table.add_index('email')
        self.assertEqual(len(table.index), 2)
        self.assertEqual(list(table.index.keys()), ['username', 'email'])

        table.remove_index('username')
        self.assertEqual(len(table.index), 1)
        self.assertTrue('email' in table.index)

if __name__ == '__main__':
    unittest.main()
