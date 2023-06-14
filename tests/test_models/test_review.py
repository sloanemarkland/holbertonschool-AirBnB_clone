"""test_review module"""
import unittest
import models.review
from models.review import Review
from models import storage

class TestReview(unittest.TestCase):
    """TestReview class documentation"""
    def setUp(self):
        """Set up method for Review class"""
        self.review1 = Review()
        self.review2 = Review()
        review_dict = self.review1.to_dict()
        self.review3 = Review(**review_dict)
    
    def tearDown(self):
        """Tear down method for Review class"""
        del self.review1
        del self.review2
        del self.review3
        storage.save()
    
    def test_init(self):
        """Test initialization of Review class"""
        self.assertEqual(self.review1.place_id, "")
        self.assertEqual(self.review1.user_id, "")
        self.assertEqual(self.review1.text, "")
    
    def test_review_update(self):
        """Test that review can be updated"""
        self.review1.place_id = "123456"
        self.review2.user_id = "123456"
        self.review3.text = "This is a review"
        self.assertEqual(self.review1.place_id, "123456")
        self.assertEqual(self.review2.user_id, "123456")
        self.assertEqual(self.review3.text, "This is a review")

if __name__ == '__main__':
    unittest.main()
