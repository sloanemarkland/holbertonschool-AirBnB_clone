"""test_user module"""
import unittest
import models.user
from models.user import User
from models import storage

class TestUser(unittest.TestCase):
    """TestUser class documentation"""
    def setUp(self):
        """ setUp method for User class. user_dict simulates the process
        of serializing the user1 instance into a dictionary. user3 simulates
        deserializing the dictionary back into an instance of User."""
        self.user1 = User()
        self.user2 = User()
        user_dict = self.user1.to_dict()
        self.user3 = User(**user_dict)

    def tearDown(self):
        """ tearDown method that deletes all test instances of User class.
        """
        del self.user1
        del self.user2
        del self.user3
        storage.save()

    def test_init(self):
        """ Test initialization of User class """
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

    def test_user_update(self):
        """ test that user can be updated """
        self.user1.email = "puppyluv3000@hotmail.com"
        self.user2.password = "password123"
        self.user3.first_name = "Benrah"
        self.user1.last_name = "Harpland"
        self.assertEqual(self.user1.email, "puppyluv3000@hotmail.com")
        self.assertEqual(self.user2.password, "password123")
        self.assertEqual(self.user3.first_name, "Benrah")
        self.assertEqual(self.user1.last_name, "Harpland")


if __name__ == '__main__':
    unittest.main()
