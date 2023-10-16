#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    Base class for modeling with common attributes and methods.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The timestamp when the instance is created.
        updated_at (datetime): The timestamp when the instance is last updated.

    Methods:
        __init__(): Initializes a new instance of the class.
        __str__(): Returns a string representation of the instance.
        save(): Updates the `updated_at` timestamp to the current time.
        to_dict(): Returns a dictionary representation of the instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.

        - Generates a unique ID for the instance.
        - Sets the `created_at` and `updated_at` timestamps to the current time.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string with class name, ID, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        """
        save the current instance to the JSON file.
        """
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary with instance attributes and timestamps in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict
