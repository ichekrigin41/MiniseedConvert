#!/usr/bin/python
from subprocess import Popen

import sys
import time



#filename = "/home/zoohan/Рабочий стол/MiniseedConvert/Miniseed_Converter.py/"
filename = sys.argv[1]

while True:
    print("\nStarting a " + filename)
    p = Popen("python" + filename,shell=True)
    p.wait(256)
    time.sleep(10)