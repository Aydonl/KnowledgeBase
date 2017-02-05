#pureftpd安装
##环境
>centos6.8
##安装依赖
`yum install gcc make perl openssl openssl-devel -y`
##编译安装
```
mkdir /opt/.src
cd /opt/.src
tar xf pure-ftpd-1.0.42.tar.bz2 
cd pure-ftpd-1.0.42
./configure --prefix=/kuaiyun/server/ftp --without-inetd --with-altlog --with-puredb --with-throttling --with-peruserlimits --with-tls
make
make install
mkdir /kuaiyun/server/ftp/etc
cd ..
cp pure-config.pl /kuaiyun/server/ftp/sbin/pure-config.pl && \
cp pure-ftpd.conf /kuaiyun/server/ftp/etc/ && \
cp addftpuser.log /kuaiyun/server/ftp/etc/ && \
cp pureftpd /etc/init.d/ && \
ll /etc/init.d/pureftpd  && \
chmod +x /etc/init.d/pureftpd && \
chmod +x /kuaiyun/server/ftp/sbin/pure-config.pl && \
chkconfig --add pureftpd
```