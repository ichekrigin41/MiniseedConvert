import os
import re
import string


marks=','
    
fileName='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/test.csv'
fileOut=open(fileName,'r')

ConvertedToMiniseed='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/miniseed_files.csv'
fileOut_2=open(ConvertedToMiniseed,'w')



def miniseedCleaner(InputFile,OutFile):
    for line in InputFile:
        if ".miniseed" in line:
            OutFile.write(line)
            OutFile.write('\n')
        

Cleaned='/home/zoohan/Desktop/cnvrt/Getter2/getter_2/cleanedPath.csv'
CleanedFile=open(Cleaned,'w')
fileOut_3=open(ConvertedToMiniseed,'r')


def remover(InputFile,OutFile):
    for line in InputFile:
        if "," in line:
            OutFile.write(line.replace(',',""))
            OutFile.write('\n')



miniseedCleaner(fileOut,fileOut_2)
remover(fileOut_3,CleanedFile)

