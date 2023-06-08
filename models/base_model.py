#!/usr/bin/python3
"""
File containing Base model class for AirBnB - The Console
"""
import uuid
from datetime import datetime


class BaseModel():
    """Base Model Class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
