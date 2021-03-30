from obspy import read
from numpy import savetxt
import os


#Convert .miniseed to txt format 

localdr=os.listdir("21")


def DataConvert(fileName,data,data2,data3,data4):
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



for lines in localdr:
    print (lines)
    miniseedData=read("/home/zoohan/Desktop/test/21/"+lines)
    channels = miniseedData 
    ch_0=miniseedData[0].data
    ch_1=miniseedData[1].data
    ch_2=miniseedData[2].data
    ch_3=miniseedData[3].data

    DataConvert('CONVERTED_'+lines[24:38],ch_0,ch_1,ch_2,ch_3)







