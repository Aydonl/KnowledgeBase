#!/bin/bash
src='/share'

dst='10.8.7.35'
port='8605'
now=`/bin/date +%F\ %H:%M:%S`

echo 30000000 > /proc/sys/fs/inotify/max_user_watches

/usr/local/bin/inotifywait -mrq --timefmt '%y/%d/%m %H:%M' --format '%T %w%f%e' -e close_write,delete,create,attrib $src \
| while read files;do
  rsync -vzrtopg --progress --password-file=/etc/tongbu.pass --port=${port} /share/ tongbu@${dst}::share
  echo $now
done
