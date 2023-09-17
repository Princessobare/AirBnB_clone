#!/usr/bin/python3
"""This Defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): amenity name.
    """

    name = ""
