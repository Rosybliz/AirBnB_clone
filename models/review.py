#!/usr/bin/python3
"""
This module contains class review
and inherits from class BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    review class for review instances
    """
    place_id = ""
    user_id = ""
    text = ""
