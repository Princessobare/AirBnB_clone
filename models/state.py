#!/usr/bin/python3
"""This Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The state name.
    """

    name = ""
