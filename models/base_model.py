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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
            


    def save(self):
        """Saves and updates the date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of BaseModel"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """String representation function"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
