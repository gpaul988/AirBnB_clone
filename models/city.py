#!/usr/bin/python3
# Graham S. Paul & Pearl Chimelumeze (city.py)
"""
Module City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Derived from BaseModel
    General class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
