
#!/bin/sh

files=`ls -d */`
c=0
for arg in "$@"
do
        for i in $files
        do
        if [ "${arg}/" == "$i" ];then
                echo "Directory files and subdirectories in '$arg' are listed below"
                echo "`ls $i`"
                c=`expr $c + 1`
                break
        fi
        done
        if [ $c -eq 0 ];then
        echo "$arg Directory Not found :("
        fi
        shift
done
