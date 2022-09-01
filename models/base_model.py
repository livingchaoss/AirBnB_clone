#!/usr/bin/python3
"""Module for Base class
contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        
