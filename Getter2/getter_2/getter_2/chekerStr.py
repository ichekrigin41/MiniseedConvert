import os
import re
import string

import wget


marks=','
    
fileName='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/test.csv'
fileOut=open(fileName,'r')

ConvertedToMiniseed='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/miniseed_files.csv'
fileOut_2=open(ConvertedToMiniseed,'w')


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

FixedURLs='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/fixedURLs.csv'
InputFile=open(FixedURLs,'w')

fileOut_3=open(ConvertedToMiniseed,'r')
WorkingDir='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded'

miniseedCleaner(fileOut,fileOut_2)
Full_URL_Fixer(fileOut_3,InputFile)

InputFile1=open(FixedURLs,'r')

os.mkdir('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded')
os.chdir('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded')

for line in InputFile1:
    wget.download(line[:-1])



