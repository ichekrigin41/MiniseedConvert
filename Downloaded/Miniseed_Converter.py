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


def DataConvert(fileName, channels):
    os.chdir(dir1)
    fileOut=fileName
    fileOut=open(fileName,'w')
    
    for channel in channels:
        for line in channel.data:
            fileOut.write(f'{str(line)}\n')
        fileOut.write("END_CHANNEL\n")


def dataProcess(workingPath):
    print (lines)
    miniseedData = read(workingPath + lines)
    channels = miniseedData
    DataConvert('CONVERTED_' + lines.replace('.miniseed', ''), miniseedData)


def dataProcessToDB(workingPath):
    print (lines)
    miniseedData = read(workingPath + lines)
    channels = miniseedData
    DataConvertToDB('CONVERTED_' + lines.replace('.miniseed', ''), miniseedData)


def DataConvertToDB(fileName, channels):
    os.chdir(dir1)
    fileOut=fileName
    fileOut=open(fileName,'w')
    
    for channel in channels:
        for line in channel.data:
            x = year_2021.insert_one(f'{str(line)}\n')
            #fileOut.write(f'{str(line)}\n')
       # fileOut.write("END_CHANNEL\n")

def TestWrite(fileName):
    os.chdir(dir1)
    tempFile = fileName
    tempFile = open(fileName,"r")
    data=[]
    for line in tempFile:
        x = DataDB.insert_one(f'{str(line)}\n')




'''
#Ввод директории ОТКУДА конвертить
print("Type Working Dir")
p=str(input())

localdr=os.listdir(p)
'''

p = '/home/zoohan/Рабочий стол/convert_mongo/MiniseedConvert/Downloaded/'
localdr = os.listdir(p)
elems=[]
Files = []

fileExt = r"*.miniseed"

if str(Files) in fileExt:
    for elems in localdr:
        Files = read(p+elems)

#pathlib.Path().absolute()

'''
for lines in localdr:
    dataProcessToDB(p)
   '''





def DB_INSERT(el):
    n=0  
    b=len(el.traces)
    print (b)
    
    while n!=len(el.traces):
        post = {
        "network":el[n].stats.network,
        "station":el[n].stats.station,
        "location":el[n].stats.location,
        "channel":el[n].stats.channel,
        "starttime":datetime.utcfromtimestamp(el[n].stats.starttime.timestamp),
        "endtime":datetime.utcfromtimestamp(el[n].stats.endtime.timestamp),
        "sampling_rate":el[n].stats.sampling_rate,
        "delta":el[n].stats.delta,
        "npts":el[n].stats.npts,
        "calib":el[n].stats.calib,
        "data":el[n].data.tolist(), 
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


for lines in Files:
    DB_INSERT(Files)
