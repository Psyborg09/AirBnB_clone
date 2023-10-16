#!/usr/bin/python3
"""This module create a class called FileStorage"""
import json
<<<<<<< HEAD
from models.base_model import BaseModel


class FileStorage:
    '''serializes instances to a JSON file and deserializes
       JSON file to instances'''
=======
from datetime import datetime

class FileStorage:
    """ this is a class of filestorage with different methods """
>>>>>>> 6dfca4d70763875bf86e1e3585708da82af77633
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
<<<<<<< HEAD
        '''this module returns the dict __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in `__objects` the `obj` with key `<obj class name>.id`'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''serializes `__objects` to the JSON file'''
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic, json_file)

    def reload(self):
        '''deserializes the JSON file to `__objects`'''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)
                for ob in obj_dict.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
=======
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_data = {}
        for key, value in self.__objects.items():
            serialized_data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
>>>>>>> 6dfca4d70763875bf86e1e3585708da82af77633
        except FileNotFoundError:
            pass
