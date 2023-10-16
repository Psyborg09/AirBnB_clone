#!/usr/bin/python3
<<<<<<< HEAD
"""This is a Module that creates the class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """This defines all common attributes or methods for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """this prints an instance of the object specified"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """this updates the `updated_at` attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
=======
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
>>>>>>> 6dfca4d70763875bf86e1e3585708da82af77633
