from obspy import read
from numpy import savetxt
import os
from datetime import datetime
import shutil


today=datetime.now()
if today.hour  <12:
    h="00"
else:
    h="12"



os.mkdir("/home/zoohan/Desktop/cnvrt/"+"Converted_"+today.strftime('%Y%m%d')+h)

#print(type(CONVERTED_DIR))
#os.chdir(os.mkdir("/home/zoohan/Desktop/cnvrt/"+"Converted_"+today.strftime('%Y%m%d')+h))
#Convert .miniseed to txt format 

localdr=os.listdir("21")

#Converted_2021033100


def DataConvert(fileName,data,data2,data3,data4):
    os.chdir("/home/zoohan/Desktop/cnvrt/"+"Converted_"+today.strftime('%Y%m%d')+h)
    fileOut=fileName
    fileOut=open(fileName,'w')
    
    for line in data:
        fileOut.write(str(line))
        fileOut.write('\n')
    fileOut.write("END_CHANNEL")
    fileOut.write('\n')
    for line in data2:
        fileOut.write(str(line))
        fileOut.write('\n')
    for line in data3:
        fileOut.write(str(line))
        fileOut.write('\n')
    fileOut.write("END_CHANNEL")
    fileOut.write('\n')
    for line in data4:
        fileOut.write(str(line))
        fileOut.write('\n')
    fileOut.write("END_CHANNEL")
    fileOut.write('\n')


def dataProcess(workingPath):
    #for lines in localdr:
    print (lines)
    #miniseedData=read("/home/zoohan/Desktop/cnvrt/21/"+lines)
    miniseedData=read(workingPath+'/'+lines)
    channels = miniseedData 
    ch_0=miniseedData[0].data
    ch_1=miniseedData[1].data
    ch_2=miniseedData[2].data
    ch_3=miniseedData[3].data
    DataConvert('CONVERTED_'+lines[24:38],ch_0,ch_1,ch_2,ch_3)

print("Type Working Dir")
path=str(input())

for lines in localdr:
    dataProcess(path)





    










