#!/usr/bin/python3
"""
Class that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os


class FileStorage():
    """serializes instance to JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing. If the
            file doesn’t exist, no exception should be raised)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                
            for key, obj_dict in serialized_objects.items():
                class_name = key.split('.')[0]
                class_ = globals()[class_name]
                obj = class_(**obj_dict)
                self.__objects[key] = obj
