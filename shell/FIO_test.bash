#!/bin/bash
#Author:Your Walter Jia
#Date && Time:2017-02-07 10:22:40
#description:测试服务器IOPS和吞吐量

# 测试次数
run_Number=3

# IO的大小，如需其他值，以"1M"形式追加
bs_Size=("4K" "4M")

# 测试路径
path="/dev/sdb"

# 测试时长，需要跑完则将此值设置为空
run_Long="--runtime=10"

# 测试文件大小
run_Size="--size=10G"

# 压缩测试结果至文件，自定义压缩文件名称
result_Name="fio_test"

# 测试参数
custom_option="--filename=${path} -ioengine=libaio --direct=1 ${run_Size} --numjobs=16 --group_reporting --iodepth=32 ${run_Long}"

# 测试开始时间
run_Time=`date +"%Y-%m-%d-%H-%M"`

# 创建缓存文件夹
for bs in ${bs_Size[*]};do
    mkdir /tmp/raid_${bs}_${run_Time}
    echo -e  "#" "\t" "块大小" "\t" "类型" "\t" "吞吐量" "\t" "IOPS" >> /tmp/raid_${bs}_${run_Time}.txt
done

# while循环次数
zero=0
while [[ ${run_Number} -gt ${zero} ]]; do
    for bs in ${bs_Size[*]};do
        # 顺序读
        # fio测试
        fio ${custom_option} --rw=read --bs=${bs} --name=raid_${bs}_read_${zero} > /tmp/raid_${bs}_${run_Time}/raid_${bs}_read_${zero}_${run_Time}.log
        rw=`grep 'rw=' /tmp/raid_${bs}_${run_Time}/raid_${bs}_read_${zero}_${run_Time}.log | sed -n 1p | awk '{print \$3}' | cut -d ',' -f 1`
        # 吞吐量保存至变量
        throughput=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_read_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 2 | cut -d '=' -f 2`
        # 如果是KB显示，则转成成MB
        if [[ $throughput =~ "KB" ]]; then
            temp_Number=`echo ${throughput} | grep -o '[0-9]\+' | sed -n 1p`
            throughput="`expr $temp_Number / 1024`MB/s"
        fi
        # IOPS保存至变量
        iops=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_read_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 3 | cut -d '=' -f 2`
        # 输出结果至文件
        echo -e ${zero} "\t" ${bs} "\t" ${rw} "\t" ${throughput} "\t" ${iops} >> /tmp/raid_${bs}_${run_Time}.txt

        # 随机读
        # fio测试
        fio ${custom_option} --rw=randread --bs=${bs} --name=raid_${bs}_randread_${zero} > /tmp/raid_${bs}_${run_Time}/raid_${bs}_randread_${zero}_${run_Time}.log
        rw=`grep 'rw=' /tmp/raid_${bs}_${run_Time}/raid_${bs}_randread_${zero}_${run_Time}.log | sed -n 1p | awk '{print \$3}' | cut -d ',' -f 1`
        # 吞吐量保存至变量
        throughput=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_randread_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 2 | cut -d '=' -f 2`
        # 如果是KB显示，则转成成MB
        if [[ $throughput =~ "KB" ]]; then
            temp_Number=`echo ${throughput} | grep -o '[0-9]\+' | sed -n 1p`
            throughput="`expr $temp_Number / 1024`MB/s"
        fi
        # IOPS保存至变量
        iops=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_randread_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 3 | cut -d '=' -f 2`
        # 输出结果至文件
        echo -e ${zero} "\t" ${bs} "\t" ${rw} "\t" ${throughput} "\t" ${iops} >> /tmp/raid_${bs}_${run_Time}.txt

        # 顺序写
        # fio测试
        fio ${custom_option} --rw=write --bs=${bs} --name=raid_${bs}_write_${zero} > /tmp/raid_${bs}_${run_Time}/raid_${bs}_write_${zero}_${run_Time}.log
        rw=`grep 'rw=' /tmp/raid_${bs}_${run_Time}/raid_${bs}_write_${zero}_${run_Time}.log | sed -n 1p | awk '{print \$3}' | cut -d ',' -f 1`
        # 吞吐量保存至变量
        throughput=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_write_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 2 | cut -d '=' -f 2`
        # 如果是KB显示，则转成成MB
        if [[ $throughput =~ "KB" ]]; then
            temp_Number=`echo ${throughput} | grep -o '[0-9]\+' | sed -n 1p`
            throughput="`expr $temp_Number / 1024`MB/s"
        fi
        # IOPS保存至变量
        iops=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_write_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 3 | cut -d '=' -f 2`
        # 输出结果至文件
        echo -e ${zero} "\t" ${bs} "\t" ${rw} "\t" ${throughput} "\t" ${iops} >> /tmp/raid_${bs}_${run_Time}.txt

        # 随机写
        # fio测试
        fio ${custom_option} --rw=randwrite --bs=${bs} --name=raid_${bs}_randwrite_${zero} > /tmp/raid_${bs}_${run_Time}/raid_${bs}_randwrite_${zero}_${run_Time}.log
        rw=`grep 'rw=' /tmp/raid_${bs}_${run_Time}/raid_${bs}_randwrite_${zero}_${run_Time}.log | sed -n 1p | awk '{print \$3}' | cut -d ',' -f 1`
        # 吞吐量保存至变量
        throughput=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_randwrite_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 2 | cut -d '=' -f 2`
        # 如果是KB显示，则转成成MB
        if [[ $throughput =~ "KB" ]]; then
            temp_Number=`echo ${throughput} | grep -o '[0-9]\+' | sed -n 1p`
            throughput="`expr $temp_Number / 1024`MB/s"
        fi
        # IOPS保存至变量
        iops=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_randwrite_${zero}_${run_Time}.log | sed s/[[:space:]]//g | cut -d ',' -f 3 | cut -d '=' -f 2`
        # 输出结果至文件
        echo -e ${zero} "\t" ${bs} "\t" ${rw} "\t" ${throughput} "\t" ${iops} >> /tmp/raid_${bs}_${run_Time}.txt
                                        
        # 混合随机读写
        # fio测试
        fio ${custom_option} -rw=randrw -rwmixread=70 --bs=${bs} --name=raid_${bs}_rw_${zero} > /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log
        rw1=`grep 'rw=' /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log | sed -n 1p | awk '{print \$3}' | cut -d ',' -f 1`
        # 吞吐量保存至变量
        throughput1=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log | sed -n 1p | sed s/[[:space:]]//g | cut -d ',' -f 2 | cut -d '=' -f 2`
        # 如果是KB显示，则转成成MB
        if [[ $throughput1 =~ "KB" ]]; then
            temp_Number=`echo ${throughput1} | grep -o '[0-9]\+' | sed -n 1p`
            throughput1="`expr $temp_Number / 1024`MB/s"
        fi
        # IOPS保存至变量
        iops1=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log | sed -n 1p | sed s/[[:space:]]//g | cut -d ',' -f 3 | cut -d '=' -f 2`
        rw2=`grep 'rw=' /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log | sed -n 2p | awk '{print \$3}' | cut -d ',' -f 1`
        # 吞吐量保存至变量
        throughput2=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log | sed -n 2p | sed s/[[:space:]]//g | cut -d ',' -f 2 | cut -d '=' -f 2`
        # 如果是KB显示，则转成成MB
        if [[ $throughput2 =~ "KB" ]]; then
            temp_Number=`echo ${throughput2} | grep -o '[0-9]\+' | sed -n 1p`
            throughput2="`expr $temp_Number / 1024`MB/s"
        fi
        # IOPS保存至变量
        iops2=`grep iops /tmp/raid_${bs}_${run_Time}/raid_${bs}_rw_${zero}_${run_Time}.log | sed -n 2p | sed s/[[:space:]]//g | cut -d ',' -f 3 | cut -d '=' -f 2`
        # 输出结果至文件
        echo -e ${zero} "\t" ${bs} "\t" ${rw1} "\t" ${throughput1} "\t" ${iops1} >> /tmp/raid_${bs}_${run_Time}.txt
        echo -e ${zero} "\t" ${bs} "\t" ${rw2} "\t" ${throughput2} "\t" ${iops2} >> /tmp/raid_${bs}_${run_Time}.txt

    done
    # 测试次数+1
    zero=`expr $zero + 1`
done



# 压缩测试结果
tar -czvf /tmp/${result_Name}-${run_Time}.tar.gz /tmp/raid_*_${run_Time}/ /tmp/raid_*_${run_Time}.txt > /dev/null 2>&1

# 控制台显示数据
for bs in ${bs_Size[*]};do
    cat /tmp/raid_${bs}_${run_Time}.txt | column -t
done

echo "下载/tmp/${result_Name}-${run_Time}.tar.gz查看详细测试结果"