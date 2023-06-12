#!/usr/bin/python3
"""
File containing Base model class for AirBnB - The Console
"""
import uuid
from datetime import datetime


class BaseModel():
    """Base Model Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class"""
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Saves and updates the date"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary representation of BaseModel"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """String representation function"""
        im_string = self.__class__.__name__
        return ("[{}] ({}) {}".format(im_string, self.id, self.__dict__))
