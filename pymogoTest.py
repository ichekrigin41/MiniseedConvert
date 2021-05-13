import pymongo
from pymongo import MongoClient
import datetime


client = MongoClient('mongodb://localhost:27017/')

db = client.Archive

test = db.__getitem__("2020")

print(test)

'''
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

insertion = db.insert_one(post).inserted_id'''