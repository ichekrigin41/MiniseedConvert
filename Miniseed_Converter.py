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

client = MongoClient('mongodb://127.0.0.1:27017/')
mydb = client["Archive"]
DataDB = mydb["Data"]

print(mydb.list_collection_names())

today=datetime.now()
if today.hour  <12:
    h="00"
else:
    h="12"

WorkDir=Path.cwd()
dir1 = f"{str(WorkDir)}/getter_2/Downloaded/Converted_{today.strftime('%Y%m%d')}{h}"
if not os.path.isdir(dir1):
    os.mkdir(dir1)


'''
#Ввод директории ОТКУДА конвертить
print("Type Working Dir")
p=str(input())

localdr=os.listdir(p)
'''

p = '/home/zoohan/Рабочий стол/convert_mongo/MiniseedConvert/tst/'
localdr = os.listdir(p)
elems=[]
Files = []

for elems in localdr:
    elems=p+elems
    Files+= [elems]

print(Files)




def DB_INSERT(el):
    n=0
    b=(read(el))
    print (b)
    
    while n!=len(b.traces):
        post = {
        "network":b[n].stats.network,
        "station":b[n].stats.station,
        "location":b[n].stats.location,
        "channel":b[n].stats.channel,
        "starttime":datetime.utcfromtimestamp(b[n].stats.starttime.timestamp),
        "endtime":datetime.utcfromtimestamp(b[n].stats.endtime.timestamp),
        "sampling_rate":b[n].stats.sampling_rate,
        "delta":b[n].stats.delta,
        "npts":b[n].stats.npts,
        "calib":b[n].stats.calib,
        "data":b[n].data.tolist(), 
        }
        insertion = DataDB.insert_one(post)
        n=n+1

'''
for e in listDB:
    #print (e.traces)
    DB_INSERT(e)
    '''
'''fileExt = r"*.miniseed"
pp=list(pathlib.Path(p).glob(fileExt))
listDB=[pp]
print(listDB[0])'''
#print(pp)


for e in Files:
    DB_INSERT(e)


