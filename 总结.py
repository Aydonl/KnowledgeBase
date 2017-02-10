#!/bin/python

#1月份总结 
def Jan():
  '''
  01/10   存储故障
  01/15   10.82.0.250 硬盘故障 影响ssp/api/jf/vps/server/host 监控系统
  01/18   www.zzidc.com 受攻击
  01/22   整合主站相关网站 cs、jiexi、mobile、idc、jf、support、ssp、www、mc、gl
  01/22   备案服务器10.82.171.12 硬盘故障，通过备份数据，转移服务器，确保了备案网站可以正常访问
  '''

#2月份总结
def Feb():
  '''
  测试keepalived 高可用的可用性
      1.监控脚本能否正常运行，监控到异常后主能否切换； √
      2.虚拟ip 掩码如何配置；√
      3.解决网卡子接口，配上ip后不通的问题 √
  完成前端nginx 高可用配置 √

  备案服务器
      1.原物理服务器 重装系统 √
      2.重启mysql服务  √ 
      3.搭建高可用环境

  监控  
      监控后端服务器每个节点状况（www,cs） √


  迁移原平台上的服务器 
  '''

#3月份总结
def Mar():
  '''

  工作

  文件服务器
  nfs+drbd

  迁移认证中心至nginx+tomcat架构的平台上
  ssl

  www.zzidc.com
  ac.zzdic.com
  mc.zzidc.com  
  ssp.zzidc.com 0401
  support.zzidc.com 0402
                                  
  访问日志分析 

  awstat
  keepalive 改进
  ---------------
  故障
  3/26  网络故障
  19:15-19:30
  影响：
  gl.zzidc.com
  ssp.zzidc.com
  support.zzidc.com
  www.zzidc.com
  idc.zzidc.com
  mc.zzidc.com
  jf.zzidc.com
  www.csgainet.com
  '''
#4月份总结
def Apr():
  '''
  搭建邮件服务器postfix+extmail，解决了网站上找回密码等通知邮件客户无法收到的问题
  关于备份：
  知识库
  OSA
  增加数据安全性

  结合开发部测试主站投诉与呼叫系统投诉相结合的功能
  搭建长沙备案系统环境
  搭建运营平台的测试环境，测试云主机
  增加网站防cc攻击功能

  计划 ：
     nginx 防cc
     tomcat 优化
     tomcat 日志问题
     tomcat内存回收问题
  故障：
      DDOS
      04-11-2014 11:15:48 -- 04-11-2014 11:22:24
      DDOS
      04-14-2014 20:05:33 -- 04-14-2014 20:24:48
      keepalived
      04-24-2014 14:45:03 -- 04-24-2014 14:58:06 

  }
  '''
#5月份总结
def May():
  '''
  5月份 {
  故障：
    网络故障
    mysql数据库负载高 05-28-2014
    CDN方案
    数据库读写分离        
  }
  '''

#6月份总结
def Jun():
  '''
  备案：文件转移到文件服务器
  support；程序上传图片转移到文件服务器
  ssp：程序上传图片转移到文件服务器
  '''
#7月份总结
def July():
  '''
  备案：数据（30G+）转移到文件服务器
  
  防cc，

  '''


网页缓存层
  无

负载均衡层
  Nginx+keepalived
WEB层
  Tomcat

文件服务器层
  无
  计划：NFS+DRBD
数据库层
  无
---------------------
文件服务器



tomcat 日志问题


tomcat内存回收问题

fail2ban
portsentry


站点重启脚本

--------------------
ac gl mobile support www  cs jf luoyang mc idc jiexi ssp


JAVA_HOME=/usr/local/jdk


gl luoyang jf support jiexi idc mc mobile www ssp cs


rpm -Uvh http://www.elrepo.org/elrepo-release-6-6.el6.elrepo.noarch.rpm




