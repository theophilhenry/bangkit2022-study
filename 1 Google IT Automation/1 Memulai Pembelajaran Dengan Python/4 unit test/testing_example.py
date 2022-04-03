import unittest

def connect_db():
    print('[Connected to DB]')

def disconnect_db(db):
    print('[Disonnected from DB {}]'.format(db))

class User:
    username = ""
    active = False

    def __init__(self, db, username):
        self.username = username

    def set_active(self):
        self.active = True

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = connect_db()
        self.dicoding = User(self.db, 'dicoding')

    def tearDown(self):
        disconnect_db(self.db)

    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.active)

    def test_user_is_active(self):
        self.dicoding.set_active()
        self.assertTrue(self.dicoding.active)

if __name__ == "__main__":
    unittest.main()