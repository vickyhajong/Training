#!/bin/sh

read n
i=1
c=1
while [ $c -le $n ]
do
    j=0
    while [ $j -lt $c ]
    do
        echo -n "$i "
        i=`expr $i + 1`
        j=`expr $j + 1`
    done
    echo " "
    c=`expr $c + 1`
done