#!/bin/sh
# Script to greet the user according to time of day
hour=`date | cut -c12-13`
now=`date +"%A, %d of %B, %Y (%r)"`
if [ $hour -lt 12 ]
then
  mess="Good Morning $LOGNAME, Have a nice day!"
fi

if [ $hour -gt 12 -a $hour -le 16 ]
then
  mess="Good Afternoon $LOGNAME"
fi

if [ $hour -gt 16 -a $hour -le 18 ]
then
  mess="Good Evening $LOGNAME"
fi
echo -e "$mess\nIt is $now"

