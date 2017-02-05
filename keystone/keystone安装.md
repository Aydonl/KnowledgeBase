#keystone安装

##环境
> centos7.2

###下载软件包

~~wget https://launchpad.net/keystone/icehouse/2014.1.3/+download/keystone-2014.1.3.tar.gz~~

`wget https://github.com/openstack/keystone/archive/10.0.0.tar.gz`

###依赖：
`yum -y  install build-essential git python-devel python-setuptools python-pip libxml2-devel libxslt-devel mariadb-server mariadb MySQL-python gcc make openssl-devel`
###启动mysql
`systemctl start mariadb`



##安装keystone
```
tar xf 10.0.0.tar.gz
cd keystone-10.0.0
pip install -r requirements.txt
python setup.py build
python setup.py install
```
