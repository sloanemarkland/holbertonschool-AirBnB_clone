#!/usr/bin/python3
"""
File containing User class for AirBnB - The Console
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""
    def __init__(self):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
