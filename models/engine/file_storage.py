#!/usr/bin/python3
"""storing dictionary 
    manages serialiation and deserialization
"""


import json


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionarry '__objects'.
        Args:
            self (object): <class '__main__.FileStorage'> instances

        Returns:
            __objects
        """

        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            self (object): <class '__main__.FileStorage'> instance
            obj (obj): instance of class 'obj.__class__'.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        return None

    def save(self):
        """serialies __objects to the JSON file (path:__file_path)
        Args:
            self (object): <class '__main__.FileStorage'> instance
        """

        serialize_my_dict = {}
        for key in self.__objects.keys():
            serialize_my_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialize_my_dict, file)
        return None

    def reload(self):
        """deserializes the JSON file to __objects
        Args:
            self (object): <class '__main__.FileStorage'> instance
        """

        from models.base_model import BaseModel

        classes_dict = {
                "BaseModel": BaseModel,
                }

        try:
            with open(self.__file_path, "r") as file:
                deserialie_my_dict = json.load(file)
            for k, v in deserialie_my_dict.items():
                self.__objects[k] = classes_dict[v["__class__"]](**v)
        except Exception:
            pass
