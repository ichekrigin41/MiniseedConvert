import os
import re
import string
from pathlib import *

import wget
import urllib.request


marks=','

ConstDir = Path.cwd()
#str(ConstDir)+


#fileName = str(ConstDir)+"/Getter2/getter_2/getter_2/scraped.csv"
fileName = str(ConstDir)+"/scraped.csv"
fileOut = open(fileName ,'r')

#ConvertedToMiniseed = str(ConstDir)+'/Getter2/getter_2/miniseed_files.csv'

ConvertedToMiniseed = str(ConstDir)+'/miniseed_files.csv'
fileOut_2 = open(ConvertedToMiniseed,'w')


def miniseedCleaner(InputFile,OutFile):
    for line in InputFile:
        if ".miniseed" in line:
            if "," in line:
                OutFile.write(line.replace(',',""))

def Full_URL_Fixer(InputFile,OutFile):
    URL_Const="http://seismic.p3volc.keenetic.pro"
    for line in InputFile:
        OutFile.write(URL_Const+line)
        


def remover(InputFile,OutFile):
    for line in InputFile:
        if "," in line:
            OutFile.write(line.replace(',',""))
        

def GetterWget(CleanedPath,WorkingDirr):
    for line in CleanedPath:
        print(URL_Const+line)
        wget.download(line)

FixedURLs=str(ConstDir)+'/fixedURLs.csv'
InputFile=open(FixedURLs,'w')

fileOut_3=open(ConvertedToMiniseed,'r')
WorkingDir=str(ConstDir)+'/Downloaded'

miniseedCleaner(fileOut,fileOut_2)
Full_URL_Fixer(fileOut_3,InputFile)

InputFile1=open(FixedURLs,'r')

#os.mkdir('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded')
os.chdir(str(ConstDir)+'/Downloaded')
'''
for line in InputFile1:
    try:
        wget.download(line[:-1])
    except: 
        wget.download(line[:-1])
'''
'''
for line in InputFile1:
    urllib.request.urlretrieve(line[:-1])
'''

