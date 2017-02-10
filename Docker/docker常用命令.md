#docker常用命令

##创建veth设备
`ip link add veth0 type veth peer name veth1`
##将veth1 移入 netns router1中
`ip link set veth1 netns router1`

---
```
docker pull hub.c.163.com/public/centos:7.0
docker pull hub.c.163.com/library/registry:2.3.1
docker run --net=none --privileged=true -it hub.c.163.com/public/centos:6.7 bash

ovs-docker add-port br0 eth0 2bf --ipaddress=192.168.66.227/24 --gateway=192.168.66.1
```
---
##在/etc/default/docker添加一行：

DOCKER_OPTS="--insecure-registry 192.168.163.133:5000"这样就能顺利的从本地镜像库中下载镜像了。

或者是在/etc/sysconfig/docker文件中添加

OPTIONS='--selinux-enabled --insecure-registry 192.168.163.133:5000'

------

```
 vi /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
TYPE=OVSPort
DEVICETYPE=ovs
OVS_BRIDGE=br-ex
ONBOOT=yes
```
Configure the virtual bridge with the IP address details that were previously allocated to eth0:
```
 vi /etc/sysconfig/network-scripts/ifcfg-br-ex
DEVICE=br-ex
DEVICETYPE=ovs
TYPE=OVSBridge
BOOTPROTO=static
IPADDR=192.168.120.10
NETMASK=255.255.255.0
GATEWAY=192.168.120.1
DNS1=192.168.120.1
ONBOOT=yes
```
## 启动一个容器
```
docker run -d \
--net=none \
-l ip=192.168.66.240 \
-l netmask=255.255.254.0 \
-l gateway=192.168.66.178 \
redis:2.8.4

#获得容器id a8f
ovs-docker add-port br0 eth0 a8f --ipaddress=192.168.66.240/23 --gateway=192.168.66.178
```