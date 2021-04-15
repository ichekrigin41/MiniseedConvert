from obspy import read
from numpy import savetxt
import os
from datetime import datetime
import shutil
from pathlib import *




today=datetime.now()
if today.hour  <12:
    h="00"
else:
    h="12"

WorkDir=Path.cwd()
dir1 = f"{str(WorkDir)}/Getter2/getter_2/Downloaded/Converted_{today.strftime('%Y%m%d')}{h}"
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






#Ввод директории ОТКУДА конвертить
print("Type Working Dir")
p=str(input())

localdr=os.listdir(p)



for lines in localdr:
    dataProcess(p)
    





    










