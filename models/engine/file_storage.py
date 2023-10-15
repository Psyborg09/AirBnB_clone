#!/usr/bin/python3
import json



class FileStorage:
    __file_path = "file.json" #path to JSON file. Creates a database
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{self.__class__.__name__}.{self.id}"
        self.__objects[key] = obj
#sets in __objects the obj with key <obj class name>.id

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as json_file
            json.dump(self.__objects, json_file)
