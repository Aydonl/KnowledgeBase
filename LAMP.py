#LAMP 环境搭建
#yum安装httpd,mysql,php
yum install httpd mysql-server php php-mysql php-gd php-mstring -y


--vhost.conf，添加如下配置

NameVirtualHost  *.*.*.16:80
NameVirtualHost  *.*.*.18:80
<VirtualHost  *.*.*.16:80>
    ServerAdmin webmaster@server.zzidc.com
    #DocumentRoot WEBROOT/tmp/
    ServerName  *.*.*.16
    <Location />
       Order Allow,Deny
       Deny from all
    </Location>
</VirtualHost>
<VirtualHost  *.*.*.18:80>
    ServerAdmin webmaster@server.zzidc.com
    DocumentRoot WEBROOT/tmp/
    ServerName  *.*.*.18
    ErrorLog logs/ls.com-error_log
    CustomLog logs/ls.com-access_log common
    <Directory WEBROOT/tmp/>
       Order Deny,Allow
       Deny from all
    </Directory>
</VirtualHost>
<VirtualHost  *.*.*.16:80>
    ServerAdmin webmaster@server.zzidc.com
    DocumentRoot WEBROOT/server.zzidc.com/
    ServerName server.zzidc.com
    php_admin_value openbase_dir "WEBROOT/server.zzidc.com:/tmp"
    ErrorLog logs/server.zzidc.com-error_log
    CustomLog logs/server.zzidc.com-access_log common
</VirtualHost>
<VirtualHost  *.*.*.18:80>
    ServerAdmin webmaster@host.zzidc.com
    DocumentRoot WEBROOT/host.zzidc.com/
    ServerName host.zzidc.com
    ServerAlias domain.zzidc.com
    RewriteEngine on
    RewriteCond %{HTTP_HOST} ^domain.zzidc.com [NC]
    #RewriteRule ^(.*)$ http://host.zzidc.com/$1 [L,R=301]
    RewriteRule ^(.*)$ http://host.zzidc.com$1 [L,R=301]
    php_admin_value openbase_dir "WEBROOT/host.zzidc.com:/tmp"
    ErrorLog logs/host.zzidc.com-error_log
    CustomLog logs/host.zzidc.com-access_log common
</VirtualHost>
<VirtualHost  *.*.*.16:80>
    ServerAdmin webmaster@vps.zzidc.com
    DocumentRoot WEBROOT/vps.zzidc.com/
    ServerName vps.zzidc.com
    php_admin_value openbase_dir "WEBROOT/vps.zzidc.com:/tmp"
    ErrorLog logs/vps.zzidc.com-error_log
    CustomLog logs/vps.zzidc.com-access_log common
    DirectoryIndex index.php index.html
</VirtualHost>
<VirtualHost  *.*.*.18:80>
    ServerAdmin webmaster@zzidc.com.cn
    DocumentRoot WEBROOT/zzidc.cn/
    ServerName zzidc.com.cn
    ServerAlias www.zzidc.com.cn
    RewriteEngine on
    RewriteCond %{HTTP_HOST} ^zzidc.com.cn [NC]
    #RewriteRule ^(.*)$ http://host.zzidc.com/$1 [L,R=301]
    RewriteRule ^(.*)$ http://www.zzidc.com.cn$1 [L,R=301]
    php_admin_value openbase_dir "WEBROOT/zzidc.cn:/tmp"
    ErrorLog logs/zzidc.cn-error_log
    CustomLog logs/zzidc.cn-access_log common
</VirtualHost>