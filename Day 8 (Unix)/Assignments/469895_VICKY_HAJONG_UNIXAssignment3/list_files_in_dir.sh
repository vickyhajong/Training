#!/bin/sh

files=`ls -d */`
c=0
for i in $files
do
    if [ "${1}/" == "$i" ];then
        echo "Directory files and subdirectories are isted below"
        echo "`ls $i`"
        c=`expr $c + 1`
        break
    fi
done
if [ $c -eq 0 ];then
    echo "Directory Not found :("
fi