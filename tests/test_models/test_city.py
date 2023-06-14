"""test_city module"""
import unittest
import models.city
from models.city import City
from models import storage

class TestCity(unittest.TestCase):
    """TestCity class documentation"""
    def setUp(self):
        """ setUp method for City class"""
        self.city1 = City()
        self.city2 = City()
        city_dict = self.city1.to_dict()
        self.city3 = City(**city_dict)

    def tearDown(self):
        """ tearDown method that deletes all test instances of City class.
        """
        del self.city1
        del self.city2
        del self.city3
        storage.save()
    
    def test_init(self):
        """ Test initialization of City class """
        self.assertEqual(self.city1.state_id, "")
        self.assertEqual(self.city1.name, "")
    
    def test_city_update(self):
        """ test that city can be updated """
        self.city1.state_id = "123456"
        self.city2.name = "Tulsa"
        self.assertEqual(self.city1.state_id, "123456")
        self.assertEqual(self.city2.name, "Tulsa")

if __name__ == '__main__':
    unittest.main()
