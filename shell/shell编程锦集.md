#shell编程锦集

##判断是否执行成功

```
check(){
  zt=$?
  if [ $zt -ne 0 ];then
    echo "failed,exiting...."
    exit 2
  fi  
}
```

##判断参数是否存在

```
checkparameter(){
  if [ -z "$1" ]; then
    echo -e "$2 参数为空 ...\n"
    exit 3
  fi

}
```

##判断文件是否存在
```
file_exsit(){
  if [ ! -f $1 ];then
    echo "$1 not exsit."
    exit 4
  fi
}
```
##脚本帮助信息
```
usage(){
  echo "$0 -s 源数据库内网ip -m 修改源数据库内网ip -a IP掩码前缀 -d 目标数据库内网ip -g 目标管理ip -n NAT服务器管理ip -b NAT服务器数据库内网ip"
  exit 0
}
```

##命令行选项
```
while getopts :s:d:m:g:n:a:b: OPTION;do
  case $OPTION in
    s)  
      sip=$OPTARG
      ;;  
    d)  
      dip=$OPTARG
      ;;  
    m)  
      msip=$OPTARG
      ;;  
    g)  
      dmip=$OPTARG
      ;;  
    n)  
      netmip=$OPTARG
      ;;  
    a)  
      mask=$OPTARG
      ;;  
    b)  
      netip=$OPTARG
      ;;  
    \?)                       #如果出现错误，则解析为?
      usage
      ;;  
  esac
done
```


