#!/bin/bash
###Compute node
instance=$1
VM_IP=$2
VLAN_ID=$3
TUNNEL_PORT=1
VM_MAC=`virsh domiflist $instance|grep br0$instance|awk '{print $5}'`
VM_PORT=`ovs-ofctl show br-wan|grep $instance|awk -F '(' '{print $1}'|tr -d ' '`
ovs-ofctl add-flow br-wan "table=0,priority=100,in_port=${VM_PORT},arp,dl_src=${VM_MAC},arp_spa=${VM_IP},actions=mod_vlan_vid:${VLAN_ID},resubmit(,1)"
ovs-ofctl add-flow br-wan "table=0,priority=100,in_port=${VM_PORT},ip,dl_src=$VM_MAC,nw_src=${VM_IP},actions=mod_vlan_vid:${VLAN_ID},resubmit(,2)"
ovs-ofctl add-flow br-wan "table=0,priority=100,in_port=${TUNNEL_PORT},arp,actions=resubmit(,1)"
ovs-ofctl add-flow br-wan "table=0,priority=100,in_port=${TUNNEL_PORT},ip,actions=resubmit(,2)"
ovs-ofctl add-flow br-wan "table=1,priority=100,arp,arp_tpa=${VM_IP},actions=strip_vlan,output:${VM_PORT}"
ovs-ofctl add-flow br-wan "table=1,priority=99,in_port=${TUNNEL_PORT},actions=drop"
ovs-ofctl add-flow br-wan "table=1,priority=98,actions=output:${TUNNEL_PORT}"
ovs-ofctl add-flow br-wan "table=2,priority=100,ip,dl_dst=${VM_MAC},actions= strip_vlan,output:${VM_PORT}"
ovs-ofctl add-flow br-wan "table=2,priority=99,in_port=${TUNNEL_PORT},actions=drop"
ovs-ofctl add-flow br-wan "table=2,priority=98,actions=output:${TUNNEL_PORT}"
