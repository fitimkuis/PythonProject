#!/bin/bash

#foldername="Users-$1-Rampup-$2-Loops-$3-Server-API_$(date +%Y%m%d%H%M)"
filename="process-payment_$(date +%Y%m%d%H%M)".csv

#mkdir $(date +%Y%m%d_%H%M%S)

script=$1
user=$2
ramp=$3
count=$4

if [ -z $4 ]
 then 
    echo "Always use four arguments, first is script name second is number of users, third is ramp up time and las is count of loops. exaple: ./script name 50 50 1 = run script with 50 users with a rampup time 1 seconds and one loop."
  exit 1
fi
echo "count of users" $user
#div=$((ramp / user));
NUM=$(echo "scale=2;$ramp/$user" | bc -l)
echo "ramp up time in sec" $NUM
echo "number of loop count" $count


foldername="$script-Users-$user-RampUpTime-$NUM-Loops-$count-timestamp-$(date +%Y%m%d%H%M)"

rm -rf /var/www/html/dashboards/*.csv
rm -rf /perf/apache-jmeter-3.2/assertions/*.csv

cd /perf/apache-jmeter-3.2/apache-jmeter-3.2/bin
./jmeter -n -t /perf/apache-jmeter-3.2/scripts/$script -Jjmeter.reportgenerator.report_title=$script-Users-$user-RampUpTime-$NUM-Loops-$count -Jusers=$user -Jcount=$count -Jrampup=$ramp -l /perf/apache-jmeter-3.2/logs/$filename -e -o /perf/apache-jmeter-3.2/dashboard/$foldername


#copy latest assertion to the www/html
cd /perf/apache-jmeter-3.2/assertions
latest=$(ls -tr | tail -n 1)
cp -u /perf/apache-jmeter-3.2/assertions/$latest /var/www/html/dashboards/
chmod 0777 /var/www/html/dashboards/*

#copy newest folder to the www/html
#cd /perf/apache-jmeter-3.2/dashboard
#newest=$(ls -td */ | head -n 1)
#echo $newest
#chmod -R 0777 $newest
#cp -R $newest /var/www/html/dashboards/
#chmod -R 0777 /var/www/html/dashboards/*
#chmod -R 0777 /var/www/html/dashboards/$newest/*

file="/perf/apache-jmeter-3.2/assertions/$latest"
if [ -f "$file" ]
then
        mv /perf/apache-jmeter-3.2/dashboard/$foldername /perf/apache-jmeter-3.2/dashboard/$foldername-FAILED
        cp -u /perf/apache-jmeter-3.2/assertions/$latest /var/www/html/dashboards/failed-tests/
        chmod 0777 /var/www/html/dashboards/failed-tests/*
#        cp -R $newest /var/www/html/dashboards/failed-tests/
#        chmod -R 0777 /var/www/html/dashboards/failed-tests/$newest/* 
        echo "$file found."
else
        mv /perf/apache-jmeter-3.2/dashboard/$foldername /perf/apache-jmeter-3.2/dashboard/$foldername-PASS
        echo "$file not found."
fi

#cd /perf/apache-jmeter-3.2/test-scripts
#sh ./copy-folder.sh

#copy newest folder to the www/html
cd /perf/apache-jmeter-3.2/dashboard
newest=$(ls -td */ | head -n 1)
echo $newest
chmod -R 0777 $newest
cp -R $newest /var/www/html/dashboards/
chmod -R 0777 /var/www/html/dashboards/*
chmod -R 0777 /var/www/html/dashboards/$newest/*

newest2=$(ls -td */ | head -n 1)
echo $newest2


file="/perf/apache-jmeter-3.2/assertions/$latest"
if [ -f "$file" ]
then
        cp -R $newest2 /var/www/html/dashboards/failed-tests/
        chmod -R 0777 /var/www/html/dashboards/failed-tests/*
        chmod -R 0777 /var/www/html/dashboards/failed-tests/$newest2/*
        echo "$file found."
fi

#cd /var/www/html/dashboards
#newest=$(ls -td */ | head -n 1)
#echo $newest
#chmod -R 0777 $newest
#x-www-browser $newest/index.html
