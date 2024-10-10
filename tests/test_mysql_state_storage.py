#!/usr/bin/python3

import unittest
import MySQLdb


class TestStateStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = MySQLdb.connect(
            user='hbnb_test',
            password='hbnb_test_pwd',
            host='localhost',
            database='hbnb_test_db'
        )
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.db.close()

    def test_create_state(self):
        # Step 1: Get the current number of records
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Step 2: Execute the console command (simulate creation)
        # This is a placeholder; replace with your actual create command
        self.cursor.execute(
            "INSERT INTO states (name) VALUES ('California')"
        )
        self.db.commit()

        # Step 3: Get the new number of records
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Validate that one record was added
        self.assertEqual(new_count, initial_count + 1)

    # Example of a skipped test for a non-applicable storage type
    @unittest.skipIf(
        not is_mysql_storage(),
        "Skipping test for non-MySQL storage"
    )
    def test_specific_mysql_feature(self):
        # Your test code here
        pass


def is_mysql_storage():
    # Implement logic to check if MySQL storage is being used
    return True  # or False based on your condition


if __name__ == '__main__':
    unittest.main()

