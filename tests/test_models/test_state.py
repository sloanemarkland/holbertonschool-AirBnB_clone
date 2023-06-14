"""test_state module"""
import unittest
import models.state
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """TestState class documentation"""
    def setUp(self):
        """ setUp method for State class. state_dict simulates the process
        of serializing the state1 instance into a dictionary. state3 simulates
        deserializing the dictionary back into an instance of State."""
        self.state1 = State()
        self.state2 = State()
        state_dict = self.state1.to_dict()
        self.state3 = State(**state_dict)

    def tearDown(self):
        """ tearDown method that deletes all test instances of State class.
        """
        del self.state1
        del self.state2
        del self.state3
        storage.save()

    def test_init(self):
        """ Test initialization of State class """
        self.assertEqual(self.state1.name, "")
        self.assertEqual(self.state2.name, "")

    def test_state_update(self):
        """ test that state can be updated """
        self.state1.name = "California"
        self.state2.name = "New York"
        self.assertEqual(self.state1.name, "California")
        self.assertEqual(self.state2.name, "New York")

if __name__ == '__main__':
    unittest.main()
