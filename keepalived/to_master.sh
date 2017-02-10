#!/bin/bash
#
now=`date +%F\ %H:%M:%S`
myname=`hostname`
message='Now I am Master,'${myname}${now}
echo $message >> /.ha/master.log
/sbin/route add default gw 122.114.25.66
