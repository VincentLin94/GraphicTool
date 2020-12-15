# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:39:08 2020

Version 1.0     2020-12-10 10:20:34
    a. [cap-mem.txt] file supported
    b. Capable of generating [Power chart] and [Mem & Swap chart]

----------------------------------------------------------------------------
Version 1.1     2020-12-10 16:34:04
    a. [battery_info.log] file supported
    b. Capable of generating [Capacity chart] and [Voltage & Current chart]
    c. Main code structure optimized
    d. Files detection and errors notice added

----------------------------------------------------------------------------
Version 1.2     2020-12-10 18:59:24
    a. fixed an issue that data in [cap-mem.txt] is separated by comma instead of blanks
    b. fixed an issue that data in [battery_info.log] need to transfer into integers
    c. fixed an issue that log files does not have uniformity

----------------------------------------------------------------------------
Version 1.3     2020-12-15
    a. Optimized the axis structure by ticks
    b. Line legends added
    c. Peak and valley, start and end for Y axis annotated
    d. Will now create a subdirectory for pngs generated
    e. Will now calculate the operating time of the scripts

@author: linwc
"""

import matplotlib.pyplot as plt
import os
import shutil
import math
import datetime as dt


class CapStyle:

    # 读取txt文件
    def readTxt(self, file):
        '''
        :param file: 'cap-mem.txt'文件
        :return: None
        '''

        with open(file) as f:
            data = f.readlines()  # 逐行读取文件内容
            data.pop()
            for d in data:  # 将data中数据逐行处理并插入各自列表中
                n = d.replace('\n', '').split(',')
                if len(n) == 5:
                    time.append(n[0])
                    power.append(int(n[1]))
                    mem.append(int(int(n[2])/1024))
                    swap.append(int(int(n[3])/1024))
                else:
                    time.append(n[0])
                    power.append(int(n[1]))
                    mem.append(int(int(n[2])/1024))
                    buff.append(int(int(n[3])/1024))
                    swap.append(int(int(n[4])/1024))

    # 绘制时间-电量二维折线图
    def timePower(self, time, power):
        '''
        :param time: 时间线
        :param power: 电量
        :return: None
        '''
        plt.subplots()
        plt.plot(time, power, 'b', linewidth=2)  # 设置坐标轴参数，颜色，线宽
        plt.title('Power curve')  # 设置标题
        plt.xlabel('Time')  # 设置x轴名称
        plt.ylabel('Power (%)')  # 设置y轴名称
        plt.xticks(rotation=90)  # 使x轴坐标纵向显示
        ticks = int(math.log2(len(time)) * 2.5)    # 计算合适的x轴坐标密度
        plt.xticks(time[::ticks])   # 调整x轴坐标显示密度
        plt.tight_layout()  # 使用紧凑布局
        plt.grid(alpha=0.5, linestyle=':')  # 显示基准线
        plt.savefig('电量曲线 by Cap.png', dpi=480)  # 保存折线图

    # 绘制时间-总内存-swap内存二维折线图
    def timeMemSwap(self, time, mem, buff, swap):
        '''
        :param time: 时间线
        :param mem: 总内存
        :param buff: buffers内存
        :param swap: swap内存
        :return: None
        '''
        plt.subplots()  # 创建画布
        # 绘制memory曲线 - 绿色
        plt.plot(time, mem, 'g', linewidth=2, label='Mem')
        plt.text(time[0], mem[0], '%s' % mem[0], color='g', style='italic')
        plt.text(time[-1], mem[-1], '%s' % mem[-1], color='g', style='italic')
        mem_max = mem.index(max(mem))
        plt.text(time[mem_max], mem[mem_max], '%s' % max(mem), color='brown', style='italic')

        # 绘制buffer曲线 - 黄色
        if buff:
            plt.plot(time, buff, 'y', linewidth=2, label='Buff')
            plt.text(time[0], buff[0], '%s' % buff[0], color='y', style='italic')
            plt.text(time[-1], buff[-1], '%s' % buff[-1], color='y', style='italic')
            buff_max = buff.index(max(buff))
            plt.text(time[buff_max], buff[buff_max], '%s' % max(buff), color='brown', style='italic')

        # 绘制swap曲线 - 红色
        plt.plot(time, swap, 'r', linewidth=2, label='Swap')
        plt.text(time[0], swap[0], '%s' % swap[0], color='r', style='italic')
        plt.text(time[-1], swap[-1], '%s' % swap[-1], color='r', style='italic')

        plt.title('Memory Curve')  # 设置标题
        plt.xlabel('Time')  # 设置x轴名称
        plt.ylabel('Mem/Swap/Buff (M)')  # 设置y轴名称
        plt.xticks(rotation=90)  # 使x轴坐标纵向显示
        ticks = int(math.log2(len(time)) * 2.5)    # 计算合适的x轴坐标密度
        plt.xticks(time[::ticks])   # 调整x轴坐标显示密度
        plt.tight_layout()  # 使用紧凑布局
        plt.grid(alpha=0.5, linestyle=':')  # 显示基准线
        plt.legend()    # 显示曲线标签
        plt.savefig('内存曲线 by Cap.png', dpi=480)  # 保存折线图


class InfoStyle:

    # 读取log文件
    def readLog(self, file):
        '''
        :param file: 'battery_info.log'文件
        :return: None
        '''
        with open(file) as f:
            data = f.readlines()    # 逐行读取文件内容
            data.pop()
            for d in data:  # 将data中数据逐行处理并插入各自列表中
                n = d.split('|')
                time.append(n[0].replace('CST', '').replace('2020', '')
                            .replace('2021', '').rstrip(' ').replace(':', '-'))
                capacity.append(int(n[3]))
                voltage.append(int(n[5])/1000)
                current.append(int(n[7])/1000)

    # 绘制时间-电量二维折线图
    def timeCap(self, time, capacity):
        '''
        :param time: 时间线
        :param capacity: 电量
        :return: None
        '''
        plt.subplots()
        plt.plot(time, capacity, 'b', linewidth=2)  # 设置坐标轴参数，颜色，线宽
        plt.title('Capacity Curve')  # 设置标题
        plt.xlabel('Time')  # 设置x轴名称
        plt.ylabel('Capacity (%)')  # 设置y轴名称
        plt.xticks(rotation=90)  # 使x轴坐标纵向显示
        ticks = int(math.log2(len(time)) * 2.5)    # 计算合适的x轴坐标密度
        plt.xticks(time[::ticks])   # 调整x轴坐标显示密度
        plt.tight_layout()  # 使用紧凑布局
        plt.grid(alpha=0.5, linestyle=':')  # 显示基准线
        plt.savefig('电量曲线 by Info.png', dpi=480)  # 保存折线图

    # 绘制时间-运行电压-运行电流二维折线图
    def timeVolCur(self, time, voltage, current):
        '''
        :param time: 时间线
        :param voltage: 运行电压
        :param current: 运行电流
        :return: None
        '''
        plt.subplots()  # 创建画布
        # 绘制voltage曲线 - 红色
        plt.plot(time, voltage, 'r', linewidth=2, label='Voltage')
        plt.text(time[0], voltage[0], '%s' % voltage[0], color='r', style='italic')
        plt.text(time[-1], voltage[-1], '%s' % voltage[-1], color='r', style='italic')
        vol_max = voltage.index(max(voltage))
        plt.text(time[vol_max], voltage[vol_max], '%s' % max(voltage), color='brown', style='italic')

        # 绘制current曲线 - 蓝色
        plt.plot(time, current, 'b', linewidth=2, label='Current')
        plt.text(time[0], current[0], '%s' % current[0], color='b', style='italic')
        plt.text(time[-1], current[-1], '%s' % current[-1], color='b', style='italic')
        cur_max = current.index(max(current))
        plt.text(time[cur_max], current[cur_max], '%s' % max(current), color='brown', style='italic')

        plt.title('Voltage-Current Curve')  # 设置标题
        plt.xlabel('Time')  # 设置x轴名称
        plt.ylabel('Voltage & Current (mV & mA)')  # 设置y轴名称
        plt.xticks(rotation=90)  # 使x轴坐标纵向显示
        ticks = int(math.log2(len(time)) * 2.5)    # 计算合适的x轴坐标密度
        plt.xticks(time[::ticks])   # 调整x轴坐标显示密度
        plt.tight_layout()  # 使用紧凑布局
        plt.grid()  # 显示基准线
        plt.legend()    # 显示曲线标签
        plt.savefig('运行电压 & 电流曲线 by Info.png', dpi=480)  # 保存折线图


if __name__ == '__main__':
    print('Initiating...')
    # 创建预存列表
    time = []  # 时间线
    power = []  # 电量
    mem = []  # 总内存
    buff = []   # buffers内存
    swap = []  # swap内存
    capacity = []   # 剩余电量
    voltage = []    # 运行电压
    current = []    # 运行电流
    try:
        files = os.listdir()    # 列出当前目录下所有文件
        cap1 = 'cap-mem.txt' in files
        cap2 = 'cap_mem.txt' in files
        info = 'battery_info.log' in files
        # 判断cap-mem.txt是否存在
        if cap1 or cap2:
            if cap1:
                file = '.\cap-mem.txt'
            else:
                file = '.\cap_mem.txt'
            CapStyle().readTxt(file)
            print('cap-mem.txt load successfully.')
            st = dt.datetime(2020, 12, int(time[0][6:8]), int(time[0][9:11]), int(time[0][11:]))
            et = dt.datetime(2020, 12, int(time[-1][6:8]), int(time[-1][9:11]), int(time[-1][11:]))
            rt = round(((et - st).total_seconds() / 3600), 2)
            save = '.\%s ~ %s (%sh)' % (time[0], time[-1], rt)
            os.mkdir(save)
            shutil.move(file, save)
            os.chdir(save)
            CapStyle().timePower(time, power)
            print('Power chart generate successfully.')
            CapStyle().timeMemSwap(time, mem, buff, swap)
            print('Memory chart generate successfully.')
            print('Shutting down...')

        # 判断battery_info.log是否存在
        elif info:
            file = '.\\battery_info.log'
            InfoStyle().readLog(file)
            print('battery_info.log load successfully.')
            if len(time[0]) == 18:
                st = dt.datetime(2020, 12, int(time[0][8]), int(time[0][10:12]), int(time[0][13:15]))
            else:
                st = dt.datetime(2020, 12, int(time[0][8:10]), int(time[0][11:13]), int(time[0][14:16]))
            if len(time[-1]) == 18:
                et = dt.datetime(2020, 12, int(time[-1][8]), int(time[-1][10:12]), int(time[-1][13:15]))
            else:
                et = dt.datetime(2020, 12, int(time[-1][8:10]), int(time[-1][11:13]), int(time[-1][14:16]))
            rt = round(((et - st).total_seconds() / 3600), 2)
            save = '.\%s ~ %s (%sh)' % (time[0], time[-1], rt)
            os.mkdir(save)
            shutil.move(file, save)
            os.chdir(save)
            InfoStyle().timeCap(time, capacity)
            print('Capacity chart generate successfully.')
            InfoStyle().timeVolCur(time, voltage, current)
            print('Voltage & Current chart generate successfully.')
            print('Shutting down...')
        # 若未检测到log文件，则提示
        else:
            print('Failed to detect txt or log file,'
                  'please make sure to put them in the same folder with this program.')
    # 若文件内容或格式出错，则报错
    except:
        raise ValueError('Failed to load txt or log file, '
                         'check the integrity of the file and try again.')


