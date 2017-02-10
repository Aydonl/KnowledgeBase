#!/bin/bash
#
now=`date +%F\ %H:%M:%S`
myname=`hostname`
message='Now I am Backup,'${myname}${now}
echo $message >> /.ha/backup.log

