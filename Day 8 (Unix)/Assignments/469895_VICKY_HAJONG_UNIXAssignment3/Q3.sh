#!/bin/sh
echo "Enter the value that you want to check whether it can be in fibonacci series or not"
read n
c=0
if [ $n -gt 35000 ];then
    echo "Limit is 35000"
elif [ $n -eq "0" ] | [ $n -eq "1" ];then
    echo "It is fibonacci series term"
    c=`expr $c + 1`
else
    a=0
    b=1
    while [ $b -le $n ]
    do
        sum=`expr $a + $b`
        if [ $sum == $n ];then
            echo "It is a fibonacci series term"
            c=`expr $c + 1`
        fi
        a=$b
        b=$sum
    done
fi
if [ $c -eq 0 ];then
    echo "It is not in fibonacci series"
fi