kvm 相关命令
#clone
virt-clone --connect=qemu:///system -o Master -n Slave  -f /home/img/Slave.img
	从虚拟机Master clone到 虚拟机Slave  硬盘文件放在/home/img/Slave.img


#键盘映射问题
<graphics type='vnc' port='-1' autoport='yes' keymap='en-us'/>


#开机自动启动虚拟机
virsh autostart NAME

virsh list            #列出在运行的虚拟机
virsh start kvm1         #启动kvm1虚拟机
virsh shutdown kvm1   #关闭kvm1虚拟机
virsh destroy kvm1    #强制关闭vm1虚拟机
virsh autostart kvm1  #设置kvm1为自启动
virsh undefine kvm1   #删除kvm1虚拟机
virsh suspend vm1     #暂停kvm1虚拟机
virsh resume vm1      #从暂停状态还原vm1虚拟机



yum install xorg-x11-xinit xorg-x11-proto-devel xorg-x11-server-utils xorg-x11-xauth




virt-install -n  win2008R2-x64 --description "gainet.com windows 2008 R2 bit" --ram 2048 --vcpus 2 --cpu host-passthrough --accelerate --hvm --os-variant=win2k8 --network bridge:br0,model=virtio --graphics vnc,listen=0.0.0.0,port=5906 --disk path=/home/vmdisk/win2008R2.qcow2,bus=virtio,cache=writeback,format=qcow2,size=10  --cdrom /home/cn_windows_server_2008_r2_standard_enterprise_datacenter_web_x64_dvd_x15-50360.iso  --disk path=/home/virtio-win-0.1.100_x86.man,device=floppy  --boot cdrom  --noautoconsole


#set server type
Stype='SERVER_TYPE'
echo "$Stype" > /etc/.server.type
chattr +i /etc/.server.type
#end set server type


--kvm 添加openvswitch桥
<interface type='bridge'>
    <source bridge='br0'/>
    <virtualport type='openvswitch'>
    </virtualport>
    <model type='virtio'/>
</interface>
--kvm 添加linux bridge 桥
DEVICE=br-wan
TYPE=Bridge
ONBOOT=yes
BOOTPROTO=static
IPV6INIT=no
IPADDR=172.16.2.101
PREFIX=24


DEVICE=em1
TYPE=Ethernet
HWADDR=14:18:77:67:E8:11
ONBOOT=yes
BRIDGE=br-wan

---
virt-install -n "${instance_name}" --description "${instance_description}" \
--ram "${instance_mem}" --vcpus "${instance_cpu}" --cpu host-model --accelerate --hvm \
--network bridge:br0${instance_name},model=virtio \
--network bridge:br1${instance_name},model=virtio  \
--disk "${disk_path}",bus=virtio,cache=writeback,driver_type=qcow2,size=10 \
--boot hd,cdrom --graphics vnc,listen=0.0.0.0  --noautoconsole \
--input tablet,bus=usb \
--serial file,path=${instance_dir}console.log \
--cdrom /data/iso/welcome.iso


virt-install -n "aydon_ceph01" --description "aydon_ceph01" \
--ram "2048" --vcpus "4" --cpu host-model --accelerate --hvm \
--network bridge:br-lan,model=virtio \
--network bridge:br-pub,model=virtio \
--network bridge:br-cluster,model=virtio \
--disk "/data/vmfs/aydon_ceph01/aydon_ceph01.qcow2",bus=virtio,cache=writeback,driver_type=qcow2 \
--disk "/data/vmfs/aydon_ceph01/aydon_ceph01-data.qcow2",bus=virtio,cache=writeback,driver_type=qcow2,size=50 \
--disk "/data/vmfs/aydon_ceph01/aydon_ceph01-sys.qcow2",bus=virtio,cache=writeback,driver_type=qcow2,size=50 \
--boot hd,cdrom --graphics vnc,listen=0.0.0.0  --noautoconsole --autostart


virt-install -n "aydon_ceph02" --description "aydon_ceph02" \
--ram "2048" --vcpus "4" --cpu host-model --accelerate --hvm \
--network bridge:br-lan,model=virtio \
--network bridge:br-pub,model=virtio \
--network bridge:br-cluster,model=virtio \
--disk "/data/vmfs/aydon_ceph02/aydon_ceph02.qcow2",bus=virtio,cache=writeback,driver_type=qcow2 \
--disk "/data/vmfs/aydon_ceph02/aydon_ceph02-data.qcow2",bus=virtio,cache=writeback,driver_type=qcow2,size=50 \
--disk "/data/vmfs/aydon_ceph02/aydon_ceph02-sys.qcow2",bus=virtio,cache=writeback,driver_type=qcow2,size=50 \
--boot hd,cdrom --graphics vnc,listen=0.0.0.0  --noautoconsole --autostart


virt-install -n "aydon_ceph03" --description "aydon_ceph03" \
--ram "2048" --vcpus "4" --cpu host-model --accelerate --hvm \
--network bridge:br-lan,model=virtio \
--network bridge:br-pub,model=virtio \
--network bridge:br-cluster,model=virtio \
--disk "/data/vmfs/aydon_ceph03/aydon_ceph03.qcow2",bus=virtio,cache=writeback,driver_type=qcow2 \
--disk "/data/vmfs/aydon_ceph03/aydon_ceph03-data.qcow2",bus=virtio,cache=writeback,driver_type=qcow2,size=50 \
--disk "/data/vmfs/aydon_ceph03/aydon_ceph03-sys.qcow2",bus=virtio,cache=writeback,driver_type=qcow2,size=50 \
--boot hd,cdrom --graphics vnc,listen=0.0.0.0  --noautoconsole --autostart


virt-install -n "aydon_ceph_client" --description "aydon_ceph_client" \
--ram "2048" --vcpus "4" --cpu host-model --accelerate --hvm \
--network bridge:br-lan,model=virtio \
--network bridge:br-pub,model=virtio \
--disk "/data/vmfs/aydon_client/aydon__client.qcow2",bus=virtio,cache=writeback,driver_type=qcow2 \
--boot hd,cdrom --graphics vnc,listen=0.0.0.0  --noautoconsole --autostart


virt-install -n "aydon_centos6.8" --description "aydon_centos6.8" \
--ram "2048" --vcpus "4" --cpu host-model --accelerate --hvm \
--network bridge:br-lan,model=virtio \
--network bridge:br-pub,model=virtio \
--disk "/data/vmfs/aydon_centos6.8/aydon_centos6.8.qcow2",bus=virtio,cache=writeback,driver_type=qcow2 \
--boot hd,cdrom --graphics vnc,listen=0.0.0.0  --noautoconsole --autostart
--添加网卡

virsh attach-interface aydon_ceph03 bridge br-cluster --model virtio --live --config

--添加硬盘
1、创建硬盘
qemu-img create -f qcow2 /data/vmfs/aydon_ceph03/aydon_ceph03_sys_extent.qcow2 50G
2、新建添加硬盘的xml
add_disk.xml
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2' cache='writeback'/>
      <source file='/data/vmfs/aydon_ceph03/aydon_ceph03_sys_extent.qcow2'/>
      <backingStore/>
      <target dev='vdc' bus='virtio'/>
      <alias name='virtio-disk0'/>
    </disk>
3、添加硬盘
virsh attach-device aydon_ceph03 add_disk.xml --live --config

