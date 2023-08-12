#!/usr/bin/python3
# Graham S. Paul & Pearl Chimelumeze (review.py)
"""
Module Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Derived from BaseModel
    General class attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""