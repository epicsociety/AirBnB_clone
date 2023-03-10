#!/usr/bin/python3
"""a class Basemodel
The base class fo the AirBnB clone console
"""


from copy import deepcopy
from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    """The base class that defines attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instanceArgs
        Args:
            self (object): <class '__main__.BaseMode'> type object
		    - *args: list of arguments
		    - **kwargs: dict of key-values arguments
		"""

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, timeformat))

                    else:
                        setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = deepcopy(self.created_at)
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance

        Args:
            self (object): <class '__main__.BaseModel'> type object

        Return: string representation of the object that called it
        """

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of an instance
        Args:
            self (object): <class '__main__.BaseModel'> type object

        Return:
            Dictionary representation of all attributed of object

        """

        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def save(self):
        """Updates 'updated_at' attribute with 
        the current time 
        Args:
            self.(object): <class '__main__.BaseModel'> type object
        """

        self.update_at = datetime.now()
        storage.new(self)
        storage.save()
        return None

