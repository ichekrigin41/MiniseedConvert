import os
import shutil



listNames=["_202101_","_202102_","_202103_","_202104_","_202105_","_202106_",
"_202107_","_202108_","_202109_","_202110","_202111_","_202112_"]

testName1="IV.KRMSH_20210116_070000.miniseed"
testName2="IV.KRMSH_20210216_070000.miniseed"
testName3="IV.KRMSH_20210816_070000.miniseed"

arr=os.listdir('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded')

f=[f'{str(index):0>2.2}' for index in range(1,13)]

#mover2(testName2,f)



def mover(fileName):
    if "_202101" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_01')
        print(fileName)
    if "_202102" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_02')
        print(fileName)
    if "_202103" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_03')
        print(fileName)
    if "_202104" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_04')
        print(fileName)
    if "_202105" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_05')
        print(fileName)
    if "_202106" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_06')
        print(fileName)
    if "_202107" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_07')
        print(fileName)
    if "_202108" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_08')
        print(fileName)
    if "_202109" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_09')
        print(fileName)
    if "_202110" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_10')
        print(fileName)
    if "_202111" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_11')
        print(fileName)
    if "_202112" in fileName:
        shutil.move('/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/'+fileName,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/Downloaded/2021_12')
        print(fileName)
    else: return 0




for line in arr:
    mover(line)


#mover3(arr,listNames)
'''
for line in arr:
    mover3(line,listNames)
'''