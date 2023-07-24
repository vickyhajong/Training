#!/bin/sh

addNum()
{
    result=`expr $1 + $2`
    echo "$result"
}
diffNum()
{
    result=`expr $1 - $2`
    echo "$result"
}
mulNum()
{
    result=`expr $1 \* $2`
    echo "$result"
}
divNum()
{
    result=`expr $1 / $2`
    echo "$result"
}

if [ $2 == "+" ];then
    addNum $1 $3
elif [ $2 == "-" ];then
    diffNum $1 $3
elif [ $2 == "x" ];then
    mulNum $1 $3
elif [ $2 == "/" ];then
    divNum $1 $3
else
    echo "Unknown Operator $2"
fi