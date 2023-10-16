#!/usr/bin/python3
import json
from datetime import datetime

class FileStorage:
    """ this is a class of filestorage with different methods """
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
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
        except FileNotFoundError:
            pass
