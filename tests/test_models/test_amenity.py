"""test_amenity module"""
import unittest
import models.amenity
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """TestAmenity class documentation"""
    def setUp(self):
        """ setUp method for Amenity class"""
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        amenity_dict = self.amenity1.to_dict()
        self.amenity3 = Amenity(**amenity_dict)

    def tearDown(self):
        """ tearDown method that deletes all test instances of Amenity class.
        """
        del self.amenity1
        del self.amenity2
        del self.amenity3
        storage.save()
    
    def test_init(self):
        """ test initialization for Amenity class """
        self.assertEqual(self.amenity1.name, "")
        self.assertEqual(self.amenity2.name, "")
    
    def test_amenity_update(self):
        """ test that amenity can be updated """
        self.amenity1.name = "Hot Tub"
        self.amenity2.name = "Pool"
        self.assertEqual(self.amenity1.name, "Hot Tub")
        self.assertEqual(self.amenity2.name, "Pool")

if __name__ == '__main__':
    unittest.main()
