import pymongo
from pymongo import MongoClient
import datetime


client = MongoClient('mongodb://127.0.0.1:27017/')

mydb = client["Archive"]
year_2020 = mydb["2020"]

testDict = {"name":"Test1"}

x = year_2020.insert_one(testDict)



print(mydb.list_collection_names())
print(x.inserted_id)

'''
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

insertion = db.insert_one(post).inserted_id'''