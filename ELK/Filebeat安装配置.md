# Filebeat安装

1. 下载rpm包

`wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.2.1-x86_64.rpm`

2. 安装
`rpm -ivh filebeat-5.2.1-x86_64.rpm`


3. 配置
```yaml
filebeat.prospectors:
- input_type: log
  paths:
    - /usr/local/ac_apache/logs/catalina.out
  fields:
    sitename: ac
  fields_under_root: true
  tail_files: true
- input_type: log
  paths:
    - /usr/local/www_apache/logs/catalina.out
  fields:
    sitename: www
  fields_under_root: true
  tail_files: true
name: test209
output.logstash:
  hosts: ["192.168.100.168:5044"]
# 输出到console
output.console:
  pretty: true
```

**详细配置见 /etc/filebeat/filebeat.full.yml**