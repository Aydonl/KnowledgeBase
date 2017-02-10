#!/bin/python
#nginx+waf安装配置
#安装依赖软件,创建所需目录,创建用户
def software_dir_user():
	'''
	yum install pcre pcre-devel openssl-devel gcc make -y
	mkdir -pv /var/tmp/nginx/proxy/ && \
	useradd -r -M -s /sbin/nologin nginx
	'''

#安装Lua库,下载地址：http://luajit.org/download/LuaJIT-2.0.2.tar.gz
def install_lua():
	'''
	下载后解压，
	make && make install
	ln -sv /usr/local/lib/libluajit-5.1.so.2.0.2 /lib64/libluajit-5.1.so.2
	'''

#编译安装Nginx，安装ngx_lua,ngx_devel_kit
def install_nginx():
	'''
	源码修改定制-版本信息欺骗
修改 src/core/nginx.h文件，进行版本欺骗，例如
 
#define NGINX_VERSION "1.0.14"
#define NGINX_VER "Nginx/"NGINX_VERSION
改为
#define NGINX_VERSION "2.2.14"
#define NGINX_VER "Apache/"NGINX_VERSION
 
去掉Debug编译选项
Nginx默认配置和编译是带-g选项的，这样会使可执行文件变大，去掉-g就很小了，运行效率也会提高。修改auto/cc/gcc文件，将CFLAGS=”$CFLAGS -g”这一行注释掉，大约是倒数第8行，即改为：
# debug
#CFLAGS="$CFLAGS -g"

	wget https://github.com/simpl/ngx_devel_kit/archive/v0.2.19.tar.gz
	wget https://github.com/chaoslawful/lua-nginx-module/archive/v0.9.0.tar.gz
	tar xf v0.2.19.tar.gz
	tar xf v0.9.0.tar.gz
	export LUAJIT_LIB=/usr/local/lib
	export LUAJIT_INC=/usr/local/include/luajit-2.0
	./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-pcre --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock --user=nginx --group=nginx --with-http_ssl_module --with-http_flv_module --with-http_gzip_static_module --http-proxy-temp-path=/var/tmp/nginx/proxy/ --add-module=/root/ngx_lua/ngx_devel_kit-0.2.19 --add-module=/root/ngx_lua/lua-nginx-module-0.9.12 --with-openssl=/root/ngx_lua/openssl-1.0.1g --with-ipv6
	make && make install
	'''

#安装ngx_lua_waf	
def install_ngx_lua_waf():
	'''
	#wget https://github.com/loveshell/ngx_lua_waf/archive/master.zip
	wget http://10.81.0.30:8098/fwqpz/waf1.1.tbz
	mv master /etc/nginx/waf
	编辑init.lua配置部分
		logpath='/var/log/nginx/hack/'
		rulepath='/etc/nginx/wafconf/'

	mkdir -pv /var/log/nginx/hack/
	chown -R nginx /var/log/nginx/hack
	在nginx.conf的http段添加
    lua_package_path "/etc/nginx/waf/?.lua";
    lua_shared_dict guard_dict 100m;
    lua_shared_dict dict_captcha 70m;
    lua_shared_dict limit 100m;
    init_by_lua_file  /etc/nginx/waf/init.lua;
    access_by_lua_file /etc/nginx/waf/runtime.lua;
    lua_max_running_timers 1;

	'''

#启动nginx
def final():
	'''
	启动nginx
		nginx
	测试WAF
		curl http://127.0.0.1/index.html?id=../../etc/passwd
	'''


def youhua():
'''
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.default.accept_source_route = 0
kernel.sysrq = 0
kernel.core_uses_pid = 1
net.ipv4.tcp_syncookies = 1
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.shmmax = 68719476736
kernel.shmall = 4294967296
net.ipv4.tcp_max_tw_buckets = 6000
net.ipv4.tcp_sack = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_rmem = 4096        87380   4194304
net.ipv4.tcp_wmem = 4096        16384   4194304
net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.netdev_max_backlog = 262144
net.core.somaxconn = 262144
net.ipv4.tcp_max_orphans = 3276800
net.ipv4.tcp_max_syn_backlog = 262144
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_synack_retries = 1
net.ipv4.tcp_syn_retries = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_mem = 94500000 915000000 927000000
net.ipv4.tcp_fin_timeout = 1
net.ipv4.tcp_keepalive_time = 30
net.ipv4.ip_local_port_range = 1024    65000
参考：http://blog.sina.com.cn/s/blog_561159790101dd6g.html


ulimit

'''