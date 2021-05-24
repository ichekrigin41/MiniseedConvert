from posix import listdir
from weakref import ProxyTypes
from obspy import read
from numpy import savetxt
import numpy as np
import os
from datetime import datetime
import shutil
from pathlib import *
import pymongo
from pymongo import MongoClient
import pathlib
from pymongo import database
from pymongo import cursor
from sshtunnel import SSHTunnelForwarder
import pprint
import json
import re


MONGO_HOST = "192.168.1.34"
MONGO_DB = "Archive"
MONGO_USER = "ubersoft"
MONGO_PASS = "1"

server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=('127.0.0.1', 27017)
)

server.start()

# server.local_bind_port is assigned local port
client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
db = client[MONGO_DB]
DataDB = db["Data"]
AddedFilesDB = db["AddedFiles"]
pprint.pprint(db.collection_names())


'''
client = MongoClient('mongodb://127.0.0.1:27017/')
mydb = client["Archive"]
DataDB = mydb["Data"]
'''


print(db.list_collection_names())

today = datetime.now()
if today.hour < 12:
    h = "00"
else:
    h = "12"

WorkDir = Path.cwd()
dir1 = f"{str(WorkDir)}/getter_2/Downloaded/Converted_{today.strftime('%Y%m%d')}{h}"
if not os.path.isdir(dir1):
    os.mkdir(dir1)


p = '/home/zoohan/Рабочий стол/convert_mongo/MiniseedConvert/tst/'

# Ввод директории ОТКУДА конвертить
print("Ввод директории ОТКУДА вести запись в БД")
# p=str(input())


localdr = os.listdir(p)
elems = []
Files = []

for elems in localdr:
    elems = p+elems
    Files += [elems]

print(Files)


def DB_INSERT(el):
    n = 0
    b = (read(el))
    print(b)

    while n != len(b.traces):
        post = {
            "network": b[n].stats.network,
            "station": b[n].stats.station,
            "location": b[n].stats.location,
            "channel": b[n].stats.channel,
            "starttime": datetime.utcfromtimestamp(b[n].stats.starttime.timestamp),
            "endtime": datetime.utcfromtimestamp(b[n].stats.endtime.timestamp),
            "sampling_rate": b[n].stats.sampling_rate,
            "delta": b[n].stats.delta,
            "npts": b[n].stats.npts,
            "calib": b[n].stats.calib,
            "data": b[n].data.tolist(),
            "file_name": el
        }
        
        DataDB.insert_one(post)
        n = n+1
        


def AddedFiles(FileName):
    post2 = {
        "file_name": FileName,
        "add_time": today
    }
    AddedFilesDB.insert_one(post2)


def DatabaseChecker(datas):
    for datas in Files:
        DB_INSERT(datas)
        AddedFiles(datas)


    # print(list(F))
n = 0


'''
for e in Files:
    #AdFiles = AddedFilesDB.find_one({"file_name"},{e})
    #FileNameInDB = DataDB.find_one({"file_name"},{e})

    #AdFiles = AddedFilesDB.find_one({"file_name":e})
    #FileNameInDB = DataDB.find_one({"file_name":e})

    AdFiles = AddedFilesDB.find({},{"_id":0,"file_name":1})


    #FileNameInDB = DataDB.find_one({"file_name":e})


    print(AdFiles)
    #print(FileNameInDB)
   # print(FileNameInDB)
   # DB_INSERT(e)
   # AddedFiles(e)
  '''
'''
for e in AddedFilesDB.find({}, {"_id": 0, "file_name": 1}):
    #DatabaseChecker(e)
    
    print(type(e))
    res = str(e)
    lenres = len(res)
    convertedstring = (res[13:lenres-1])
    XX = re.sub("'", "", convertedstring)
    XX2 = re.sub("^\s+|\s+$", "", XX, flags=re.UNICODE)
    for e1 in DataDB.find({}, {"_id": 0, "file_name": 1}):
        res2 = str(e1)
        print(res2)

        lenres2 = len(res2)
        convertedstring2 = (res2[13:lenres2-1])
        XXX = re.sub("'", "", convertedstring2)
        XX3 = re.sub("^\s+|\s+$", "", XXX, flags=re.UNICODE)

        if XX2 == XX3:
                print("Equal")
                #break
        elif XX2 != XX3:
                print("NOT Equals")
                #print(str(datas))
                print(XX2)
                print(XX3)
                #DatabaseChecker(e)

        # e+=1
'''

for e in Files:
   # AA=DataDB.find({"/home/zoohan/Рабочий стол/convert_mongo/MiniseedConvert/tst/IV.KRMSH_centaur-6_7618_20210401_210000.miniseed":{"$exists":True}})
    #AA=list(AddedFilesDB.find({"$and":[ {e:{"$exists": True}}, {e:{"$ne": "1"}}]}))
    AA=AddedFilesDB.find()[20:25]
    BB=DataDB.find({"$and":[ {e:{"$exists": True}}, {e:{"$ne": ""}}]})
    print(e)
#collection.find({"cwc":{"$exists":True}})
    for doc in AddedFilesDB.find(({e:{"$exists":True}})):
        print(doc)
            
    
    #print("False")
    
    DB_INSERT(e)
    AddedFiles(e)
  
server.stop()
