"""test_base module"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """TestBase class documentation"""
    def test_init(self):
        """ Test initialization of BaseModel class """
        modelmodel = BaseModel()
        self.assertIsNotNone(modelmodel.id)

    def test_init2(self):
        """idk"""
        modelmodel = BaseModel()
        self.assertIsInstance(modelmodel.created_at, datetime)

    def test_init3(self):
        """updated_at belongs to datetime class"""
        modelmodel = BaseModel()
        self.assertIsInstance(modelmodel.updated_at, datetime)

    def test_init4(self):
        """created and updated"""
        modelmodel = BaseModel()
        self.assertEqual(modelmodel.created_at, modelmodel.updated_at)
    
    def test_save(self):
        """ test the save method of BaseModel class """
        fakemod = BaseModel()
        fakecreate = fakemod.created_at
        fakeupdate = fakemod.updated_at
        fakemod.save()
        self.assertEqual(fakemod.created_at, fakecreate)
        self.assertNotEqual(fakemod.updated_at, fakeupdate)

    def test_to_dict(self):
        """ test to_dict method of BaseModel class """
        gizelle = BaseModel()
        gizelle_dict = gizelle.to_dict()
        self.assertIsInstance(gizelle_dict, dict)
        self.assertIsInstance(gizelle_dict["updated_at"], str)
        self.assertIsInstance(gizelle_dict["created_at"], str)

if __name__ == '__main__':
    unittest.main()
