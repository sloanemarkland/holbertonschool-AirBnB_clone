#!/usr/bin/python3
"""
File containing City class for AirBnB - The Console
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel"""
    state_id = ""
    name = ""
