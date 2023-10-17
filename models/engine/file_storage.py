#!/usr/bin/python3
"""This module create a class called FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    '''serializes instances to a JSON file and deserializes
       JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''this module returns the dict __objects
        '''
        return self.__objects

    def new(self, obj):
        '''sets in `__objects` the `obj` with key `<obj class name>.id`
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''serializes `__objects` to the JSON file
        '''
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            dict_repre = {k : v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_repre, json_file)

    def reload(self):
        '''deserializes the JSON file to `__objects`
        '''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)
                for ob in obj_dict.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
        except FileNotFoundError:
            pass
