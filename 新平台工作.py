#!/bin/python
#端口信息
def duankouxinxi():
  '''
  www 8081 8006
  support 8082 8007
  idc 8083 8008
  ac  8084 8009
  cs  8085 8010
  mc  8086 8011
  gl  8087 8012
  luoyang 8088 8013
  mobile  8089 8014
  jiexi 8090 8015
  ssp 8091 8016
  jf  8092 8017
  cloud 8095 8019
  python_vnc 8093 N/A
  beian 8096 8020
  saas 8097 8021
  beian_jieko 8098 8022
  jk 8099 8023
  gainet_cn 8100 8024
  '''
#修改端口
def xiugaiduankou():
  '''
  if [ $i = 'support' ];then
    sed -i 's/Connector port="8080"/Connector port="8082"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8007"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'www' ];then
    sed -i 's/Connector port="8080"/Connector port="8081"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8006"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'idc' ];then
    sed -i 's/Connector port="8080"/Connector port="8083"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8008"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'ac' ];then
    sed -i 's/Connector port="8080"/Connector port="8084"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8009"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'cs' ];then
    sed -i 's/Connector port="8080"/Connector port="8085"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8010"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'mc' ];then
    sed -i 's/Connector port="8080"/Connector port="8086"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8011"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'gl' ];then
    sed -i 's/Connector port="8080"/Connector port="8087"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8012"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'luoyang' ];then
    sed -i 's/Connector port="8080"/Connector port="8088"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8013"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'mobile' ];then
    sed -i 's/Connector port="8080"/Connector port="8089"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8014"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'jiexi' ];then
    sed -i 's/Connector port="8080"/Connector port="8090"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8015"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'ssp' ];then
    sed -i 's/Connector port="8080"/Connector port="8091"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8016"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'jf' ];then
    sed -i 's/Connector port="8080"/Connector port="8092"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8017"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  if [ $i = 'cloud' ];then
    sed -i 's/Connector port="8080"/Connector port="8095"/' /usr/local/$i\_apache/conf/server.xml
    sed -i 's/Server port="8005"/Server port="8019"/' /usr/local/$i\_apache/conf/server.xml
    continue   
  fi
  '''
#站点配置文件
def peizhiwenjian():
  '''
  glht:
  WEB-INF/conf/applicationContext.xml
  WEB-INF/web.xml 
  WEB-INF/classes/config_zzht.properties 

  hyzx:
  WEB-INF/classes/config.properties 
  WEB-INF/web.xml 
  WEB-INF/conf/applicationContext.xml
  WEB-INF/classes/log4j.properties

  zzproduct:
  WEB-INF/conf/applicationContext.xml
  WEB-INF/web.xml 
  WEB-INF/classes/config.properties

  csproduct:
  WEB-INF/conf/applicationContext.xml
  WEB-INF/web.xml 
  WEB-INF/classes/config.properties

  cas:
  WEB-INF/cas.properties

  support.zzidc.com/
  WEB-INF/classes/support.properties
  WEB-INF/web.xml  

  idc:
  WEB-INF/classes/jdbc.properties 
  WEB-INF/web.xml 

  mobile
  WEB-INF/classes/config.properties

  dmp
  WEB-INF/web.xml

  ssp
  WEB-INF/conf/spring_RMI.xml'''

#站点所需的文件夹
def wenjianjia():
  '''
  /opt/webapplication/{luoyang,glht,csproduct,mobile,dmp,idc/ROOT,zzproduct,hyzx,support.zzidc.com,jf,ssp,cloud}
  /opt/{photo,pic,file,scrawl,share,share/{upload,photos,image,file,scrawl,softwares,softwares/upload,softwares/images},support_upload,jf_upload}
  '''
#备案系统
def beian():
  '''
  yum install php-soap php php-mysql
  <VirtualHost 116.255.177.19:8090>
       ServerName test.beian.zzidc.com
       DocumentRoot /opt/test/www
       DirectoryIndex index.php index.html
       ErrorLog "logs/test.beian-error_log"
       CustomLog "|/usr/local/Zend/apache2/bin/rotatelogs  /usr/local/Zend/apache2/logs/test.beian-%Y%m%d-access.log 86400" common
       ErrorDocument 500 http://beian.zzidc.com/
       ErrorDocument 403 /missing.html
       <Directory /opt/test/www>
          Options -Indexes
          AllowOverride NONE
          Order Allow,Deny
          Allow from all
       </Directory>
       php_admin_value openbase_dir "/opt/test/www:/tmp"
       <Location /beian/admin>
          Order Allow,Deny
          Allow from 203.171.224.45
          Allow from 219.141.169.253
          Allow from 116.255.132.0/255.255.255.0
       </Location>
  </VirtualHost>
  http://116.255.177.19:8090/IspDomainStatus/check.php?dns=zzidc.com
  http://hcaisp.miibeian.gov.cn/BeianStatusWebService/queryBeianStatus?wsdl
  http://xcaisp.miitbeian.gov.cn/ISPWebService/upDownLoad?wsdl
  http://116.255.177.19:8098/ScanDomainCS?dns     长沙
  http://116.255.177.19:8098/ScanDomainZZ?dns     郑州
  http://116.255.177.19:8098/ScanDomainCS2ZZ?dns  长沙异常时转郑州接口
  http://116.255.177.19:8098/ScanDomainZZ2CS?dns  郑州异常时转长沙接口
  '''

#站点配置文件
def zhandianpeizhi():
  '''
  #luoyang
    <Host name="www.lyjingan.com"  appBase="webapps"
                unpackWARs="true" autoDeploy="true"
                xmlValidation="false" xmlNamespaceAware="false">
            <Alias>lyjingan.com</Alias>
            <Context path="" docBase="/opt/webapplication/luoyang/" crossContext="true" privileged="true" reloadable="true" ></Context>
            <Context path="/photo" docBase="/opt/photo"></Context> 
            <Context path="/jsp/pic" docBase="/opt/pic"></Context>
            <Context path="/jsp/file" docBase="/opt/file"></Context>
            <Context path="/jsp/scrawl" docBase="/opt/scrawl"></Context>
    </Host>
  ###gl
      <Host name="gl.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/glht/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
        <Context path="/upload" docBase="/opt/share/upload"> </Context>
        <Context path="/images/evaluation/photo" docBase="/opt/share/photos"> </Context>
        <Context path="/upload/image" docBase="/opt/share/image"> </Context>
        <Context path="/jsp/file" docBase="/opt/share/file"> </Context>
        <Context path="/jsp/scrawl" docBase="/opt/share/scrawl"> </Context>
        <Context path="/softwares/upload" docBase="/opt/share/softwares/upload"></Context>
        <Context path="/softwares/images" docBase="/opt/share/softwares/images"></Context>
        <Context path="/excel" docBase="/opt/share/glht"></Context>
      </Host>
  ####cs
      <Host name="www.csgainet.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Alias>csgainet.com</Alias>
        <Alias>1758.csgainet.com</Alias>
        <Context path="" docBase="/opt/webapplication/csproduct/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
        <Context path="/upload" docBase="/opt/share/upload"> </Context>
        <Context path="/images/evaluation/photo" docBase="/opt/share/photos"> </Context>
        <Context path="/upload/image" docBase="/opt/share/image"> </Context>
        <Context path="/softwares/upload" docBase="/opt/share/softwares/upload"></Context>
        <Context path="/softwares/images" docBase="/opt/share/softwares/images"></Context>
      </Host>
  ###mobile
 <Host name="m.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/mobile/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
 </Host>
  ###jiexi
      <Host name="jiexi.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/dmp/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
      </Host>
  ##idc
    <Host name="idc.zzidc.com"  appBase="webapps"
                unpackWARs="true" autoDeploy="true"
                xmlValidation="false" xmlNamespaceAware="false">
            <Context path="" docBase="/opt/webapplication/idc/ROOT/" crossContext="true" privileged="true" reloadable="true" ></Context>
    </Host>
  ##www
      <Host name="www.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Alias>zzidc.com</Alias>
        <Alias>www.zzidc.net</Alias>
        <Alias>v.zzidc.com</Alias>
        <Alias>mars.zzidc.com</Alias>
        <Context path="" docBase="/opt/webapplication/zzproduct/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
        <Context path="/upload" docBase="/opt/share/upload"> </Context>
        <Context path="/images/evaluation/photo" docBase="/opt/share/photos"> </Context>
        <Context path="/upload/image" docBase="/opt/share/image"> </Context>
        <Context path="/jsp/file" docBase="/opt/share/file"> </Context>
        <Context path="/jsp/scrawl" docBase="/opt/share/scrawl"> </Context>
        <Context path="/softwares/upload" docBase="/opt/share/softwares/upload"></Context>
        <Context path="/softwares/images" docBase="/opt/share/softwares/images"></Context>
      </Host>
  ##mc
      <Host name="mc.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/hyzx/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
        <Context path="/excel" docBase="/opt/share/excel"></Context>
      </Host>
  ##support
       <Host name="support"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Alias>support.zzidc.com</Alias>
        <Context path="" docBase="/opt/webapplication/support.zzidc.com" crossContext="true" privileged="true" reloadable="true" />
        <Context path="/upload" docBase="/opt/support_upload" />
      </Host>
  #jf
      <Host name="jf.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/jf/" crossContext="true" privileged="true" reloadable="true" > </Context>
      <Context path="/jf" docBase="/opt/jf_upload"> </Context>
      </Host>
  #ssp 
       <Host name="ssp.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/ssp/" crossContext="true" privileged="true" reloadable="true" > </Context>
      </Host> 
  #cloud
      <Host name="cloud.zzidc.com"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="" docBase="/opt/webapplication/cloud/" crossContext="true" privileged="true" reloadable="true" >
        </Context>
      </Host>
  #ac
      <Host name="ac.zzidc.com"  appBase="/opt/webapplication/ac"
            unpackWARs="true" autoDeploy="true"
            xmlValidation="false" xmlNamespaceAware="false">
        <Context path="/" docBase="/opt/webapplication/ac" >
        </Context>
        <Context path="/cas" docBase="/opt/webapplication/ac/cas" crossContext="true" privileged="true" reloadable="true" >
        </Context>
      </Host>
  #beian
      
  '''

#同步tomcat配置
def tongbupeizhi():
  #/root/exclude.list
  '''
  .backup
  logs
  temp
  work
  support_upload
  '''
  '''
  for i in `ls -d /usr/local/*apache`;do rsync -avz --progress --rsh="ssh -p10222" --exclude-from=/root/exclude.list $i/ 10.82.175.9:$i/;done
  '''

#添加用户
def useradd():
  '''
  for i in `cat /root/site.log`;do useradd -r -M -s /bin/bash -g www $i;id $i;done
  '''

#iptables配置
def iptables():
  '''
  :bad_packets - [0:0]
  -A INPUT -j bad_packets
  -A bad_packets -m state --state INVALID -j DROP
  -A bad_packets -p tcp -m tcp ! --tcp-flags FIN,SYN,RST,ACK SYN -m state --state NEW -j DROP
  -A bad_packets -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP
  -A bad_packets -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,SYN,RST,PSH,ACK,URG -j DROP
  -A bad_packets -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,PSH,URG -j DROP
  -A bad_packets -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,SYN,RST,ACK,URG -j DROP
  -A bad_packets -p tcp -m tcp --tcp-flags SYN,RST SYN,RST -j DROP
  -A bad_packets -p tcp -m tcp --tcp-flags FIN,SYN FIN,SYN -j DROP
  -A bad_packets -p tcp -j RETURN
  '''


#创建一个站点
def create_site():
  '''
  useradd -r -M -s /bin/bash -g www ac
  cp /root/init-tomcat /etc/init.d/ac
  cp -a /usr/local/apache /usr/local/ac\_apache
  sed -i "s@myroot=/usr/local/apache@myroot=/usr/local/ac\_apache@" /etc/init.d/ac;ls -l /etc/init.d/ac
  sed -i "s@nginx@ac@" /etc/init.d/ac;ls -l /etc/init.d/ac
  chown -R ac:www /usr/local/ac\_apache
  '''

#Nginx节点网络配置
def ifconfig():
  '''
  /sbin/ifconfig em1 116.255.177.2/27
  /sbin/ifconfig em1:1 116.255.177.3/27
  /sbin/ifconfig em1:2 116.255.177.4/27
  /sbin/ifconfig em1:3 116.255.177.6/27
  /sbin/ifconfig em1:4 116.255.177.10/27
  /sbin/ifconfig em1:5 116.255.177.22/27
  /sbin/ifconfig em1:6 116.255.177.26/27
  /sbin/ifconfig em1:7 116.255.177.27/27
  /sbin/ifconfig em1:8 116.255.177.28/27
  /sbin/route add default gw 116.255.177.1
  '''

#修改数据库连接

def shujuku():
  '''
  sed -i -e 's/new_zzidc_db/test/' -e 's/1qazxsw2!@#$%/mnQEUSX2MOArx/' -e 's/10.82.100.101/192.168.100.207/' /opt/webapplication/zzproduct/WEB-INF/conf/applicationContext.xml
  '''


def ceshihuanji():
  '''
  sed -i -e 's/new_zzidc_db/test/' -e 's/1qazxsw2!@#$%/mnQEUSX2MOArx/' /opt/webapplication/zzproduct/WEB-INF/conf/applicationContext.xml
  sed -i -e 's/new_zzidc_db/test/' -e 's/1qazxsw2!@#$%/mnQEUSX2MOArx/' -e 's/10.82.100.101/192.168.100.207/' /opt/webapplication/zzproduct/WEB-INF/conf/applicationContext.xml
  sed -i -e 's/new_zzidc_db/test/' -e 's/1qazxsw2!@#$%/mnQEUSX2MOArx/' -e 's/10.82.100.101/192.168.100.207/' /opt/webapplication/glht/WEB-INF/conf/applicationContext.xml 
  sed -i -e 's/new_zzidc_db/test/' -e 's/1qazxsw2!@#$%/mnQEUSX2MOArx/' -e 's/10.82.100.101/192.168.100.207/' /opt/webapplication/hyzx/WEB-INF/conf/applicationContext.xml 
  sed -i -e 's/new_zzidc_db/test/' -e 's/1qazxsw2!@#$%/mnQEUSX2MOArx/' -e 's/10.82.100.101/192.168.100.207/' /opt/webapplication/ac/cas/WEB-INF/cas.properties
  '''
def tomcat_threads():
  '''
      <Executor name="tomcatThreadPool" namePrefix="catalina-exec-"
        maxThreads="6000"
        minSpareThreads="20"
        maxSpareThreads="200"
        acceptCount="500"
        maxIdletime="3000"
        />


    <!-- A "Connector" represents an endpoint by which requests are received
         and responses are returned. Documentation at :
         Java HTTP Connector: /docs/config/http.html (blocking & non-blocking)
         Java AJP  Connector: /docs/config/ajp.html
         APR (HTTP/AJP) Connector: /docs/apr.html
         Define a non-SSL HTTP/1.1 Connector on port 8080
    -->
    <Connector port="8081" protocol="HTTP/1.1"
               connectionTimeout="20000"
               URIEncoding="UTF-8"
               enableLookups="false"
               executor="tomcatThreadPool"
               compression="on"
               compressionMinSize="2048"
               noCompressionUserAgents="gozilla,traviata"
               compressableMimeType="text/html,text/xml,text/javascript,text/css,text/plain"
               redirectPort="8443" />
    java_opts:
    JAVA_OPTS='-server -Xms1024m -Xmx1024m -XX:PermSize=512M -XX:NewSize=256M -XX:MaxNewSize=256M -XX:MaxPermSize=512m -Djava.awt.headless=true'
  '''