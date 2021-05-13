import os
import shutil
import glob
from pathlib import *

listNames=["_202101","_202102","_202103","_202104","_202105","_202106",
"_202107","_202108","_202109","_202110","_202111","_202112"]



BASEDIR = os.path.abspath(os.path.dirname(__file__))

#arr=os.listdir('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded')



f=[f'{str(index):0>2.2}' for index in range(1,13)]

DownloadedDir=Path.cwd()

FixedDownloadDir=str(DownloadedDir)+"/getter_2/Downloaded/"
FixedDownloadDir2=str(DownloadedDir)+"/getter_2/Downloaded"



arr=os.listdir(FixedDownloadDir2)



def mover(fileName):
    if str(listNames[0]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_01")
        print(fileName)
    if str(listNames[1]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_02")
        print(fileName)
    if str(listNames[2]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_03")
        print(fileName)
    if str(listNames[3]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_04")
        print(fileName)
    if str(listNames[4]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_05")
        print(fileName)
    if str(listNames[5]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_06")
        print(fileName)
    if str(listNames[6]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_07")
        print(fileName)
    if str(listNames[7]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_08")
        print(fileName)
    if str(listNames[8]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_09")
        print(fileName)
    if str(listNames[9]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_10")
        print(fileName)
    if str(listNames[10]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_11")
        print(fileName)
    if str(listNames[11]) in fileName:
        shutil.move(FixedDownloadDir+fileName,FixedDownloadDir+"/2021_12")
        print(fileName)
    else: return 0



for line in arr:
    mover(line)


