#!/bin/bash
# Загрузка файлов с карымшинского сейсмического регистратора 

y=$(date -u +%Y -d "2 hour ago")
m=$(date -u +%m -d "2 hour ago")
d=$(date -u +%d -d "2 hour ago")
H=$(date -u +%H -d "2 hour ago")
file_URL="http://seismic.p3volc.keenetic.pro/archive/$y/$m/IV.KRMSH_centaur-6_7618_$y$m$d"_""$H"0000.miniseed"
filename="IV.KRMSH_centaur-6_7618_$y$m$d"_""$H"0000.miniseed"
path="/mnt/Data/KVERT/AVH_seismo/KRMSH"
mkdir -p $path/$y/$m/$d/
wget -c -t 0 -o krmsh_log $file_URL -O "$path/$y/$m/$d/$filename"
if [[ ! -s "$path/$y/$m/$d/$filename" ]]; then sh /home/kvert/scripts/krmsh_dnld.sh; else echo "$filename" >> /home/kvert/krmsh_conn.log; fi
