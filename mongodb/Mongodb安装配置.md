# Mongodb安装配置

1. 下载

wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel62-3.0.6.tgz

2. 安装

tar xf mongodb-linux-x86_64-rhel62-3.0.6.tgz -C /usr/local/
ln -sv /usr/local/mongodb-linux-x86_64-rhel62-3.0.6 /usr/local/mogodb
cd /usr/local/mogodb
mdkir etc
mkdir /mongo_data

3. 配置

```shell
vi /usr/local/mogodb/etc/mongo.conf
#内容如下
fork = true
quiet = true
port = 27018
auth = true
pidfilepath = /mongo_data/mongopid
dbpath = /mongo_data
logpath = /mongo_data/logs/server.log
logappend = true
journal = true
#rest = true
directoryperdb = true
httpinterface = false
storageEngine = wiredTiger
```

4. 启动

`/usr/local/mongodb/bin/mongod -f /usr/local/mongodb/etc/mongo.conf`