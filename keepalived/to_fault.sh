#!/bin/bash
#
now=`date +%F\ %H:%M:%S`
myname=`hostname`
message='Now I am Fault,'${myname}${now}
echo $message >> /.ha/fault.log

