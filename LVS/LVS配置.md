# lvs配置问题
[TOC]

## LVS DR模型无法正常提供服务

### 环境1. Director只有一个公网ip，且该ip为VIP，后端Real Server ip为同段的公网ip

问题： Director无法获取RIP的mac地址
解决： 在Director上手动绑定后端RIP的mac （ arp -s ）

### 环境2. Director有一个公网ip，一个内网ip，且该ip为VIP，后端Real Server ip为同段的内网ip

问题： 后端Real Server可以正常收到Director发的数据包，无法出去
原因： linux 内核反向路由检测不通过，丢弃数据包
>反向路由过滤
反向路由过滤机制是Linux通过反向路由查询，检查收到的数据包源IP是否可路由（Loose mode）、是否最佳路由（Strict mode），如果没有通过验证，则丢弃数据包，设计的目的是防范IP地址欺骗攻击。rp_filter提供了三种模式供配置：
0 - 不验证
1 - RFC3704定义的严格模式：对每个收到的数据包，查询反向路由，如果数据包入口和反向路由出口不一致，则不通过
2 - RFC3704定义的松散模式：对每个收到的数据包，查询反向路由，如果任何接口都不可达，则不通过

解决： sysctl -w net.ipv4.conf.eth0.rp_filter=2