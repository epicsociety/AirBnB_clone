#!/usr/bin/python2
"""__init__ module used to initialize a model
   It runs whenever a model is created
 """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
