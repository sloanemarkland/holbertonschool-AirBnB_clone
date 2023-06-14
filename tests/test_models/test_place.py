"""test_place module"""
import unittest
import models.place
from models.place import Place
from models import storage

class TestPlace(unittest.TestCase):
    """TestPlace class documentation"""
    def setUp(self):
        """Set up method for Place class"""
        self.place1 = Place()
        self.place2 = Place()
        place_dict = self.place1.to_dict()
        self.place3 = Place(**place_dict)
    
    def tearDown(self):
        """Tear down method for Place class"""
        del self.place1
        del self.place2
        del self.place3
        storage.save()
    
    def test_init(self):
        """Test initialization of Place class"""
        self.assertEqual(self.place1.city_id, "")
        self.assertEqual(self.place1.user_id, "")
        self.assertEqual(self.place1.name, "")
        self.assertEqual(self.place1.description, "")
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertEqual(self.place1.amenity_ids, [])
    
    def test_place_update(self):
        """test that place can be updated"""
        self.place1.city_id = "Tulsa"
        self.place2.user_id = "Benrah"
        self.place3.name = "Harpland"
        self.place1.description = "This is a place"
        self.place2.number_rooms = 1
        self.place3.number_bathrooms = 2
        self.place1.max_guest = 3
        self.assertEqual(self.place1.city_id, "Tulsa")
        self.assertEqual(self.place2.user_id, "Benrah")
        self.assertEqual(self.place3.name, "Harpland")
        self.assertEqual(self.place1.description, "This is a place")
        self.assertEqual(self.place2.number_rooms, 1)
        self.assertEqual(self.place3.number_bathrooms, 2)
        self.assertEqual(self.place1.max_guest, 3)

if __name__ == '__main__':
    unittest.main()
