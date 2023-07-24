#!/bin/sh

a=0
b=1
read n
echo "Fibonacci series"
if [ $n -eq 1 ];then
    echo -n "$a "
elif [ $n -eq 2 ];then
    echo -n "$a "
    echo -n "$b "
else
    echo -n "$a "
    echo -n "$b "
fi
n=`expr $n - 2`
while [ $n -gt 0 ]
do
    sum=`expr $a + $b`
    echo -n "$sum "
    a=$b
    b=$sum
    n=`expr $n - 1`
done
echo " "