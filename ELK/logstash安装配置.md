# logstash安装配置

1. 配置yum源

```shell
vi /etc/yum.repos.d/logstash
[logstash-5.x]
name=Elastic repository for 5.x packages
baseurl=https://artifacts.elastic.co/packages/5.x/yum
gpgcheck=0
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

2. 安装

`yum install logstash -y`

3. 配置

* vi /etc/logstash/startup.options

修改 JAVACMD

* vi /etc/logstash/jvm.options

修改jvm参数

* 将logstash配置文件放入/etc/logstash/conf.d/

示例：
tomcatlog.conf,内容如下

```yaml
input {
	beats {
	port => 5044
	}
}
output {
	mongodb {
	collection => "%{sitename}"
	database => "tomcatlog"
	generateId => false
	isodate => true
	uri	=> "mongodb://loguser:log.123@127.0.0.1:27018/tomcatlog"
	}
}
```

* 生成sysv init脚本

```shell
cd /usr/share/logstash
bin/system-install /etc/logstash/startup.options sysv
```
