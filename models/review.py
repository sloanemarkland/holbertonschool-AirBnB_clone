#!/usr/bin/python3
"""
File containing Review class for AirBnB - The Console
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
