from datetime import datetime,timedelta,date
import os
import wget


    







#today.strftime('%Y%m%d')
today=datetime.now()



y=(today.strftime('%Y'))
m=(today.strftime('%m'))
d=(today.strftime('%d'))
H=(today.strftime('%H'))




file_URL="http://seismic.p3volc.keenetic.pro/archive/"+y+"/"+m+"/"+"IV.KRMSH_centaur-6_7618_"+y+m+d+"_"+H+"0000.miniseed"
file_NAME="IV.KRMSH_centaur-6_7618_"+y+m+d+"_"+H+"0000.miniseed"

path="/home/zoohan/Desktop/cnvrt/KRMSH"

os.mkdir(path+y+m+d)
os.chdir(path+y+m+d)

start_date=date(2021,3,1)
end_date=date(2021,3,29)

delta=timedelta(days=1)

while start_date <=end_date:
    wget.download(file_URL,path+y+m+d)



#wget.download(file_URL,path+y+m+d)



print(y,m,d,H)
print(file_URL)
print(file_NAME)

