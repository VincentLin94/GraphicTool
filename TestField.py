

import os
import math
import datetime as dt

file = '.\cap_mem.txt'
time = ['Thu Dec 3 14:22:08', 'Fri Dec 14 15:39:00']
power = []
mem = []
buff = []
swap = []
voltage = []
current = []

if len(time[0]) == 18:
    st = dt.datetime(2020, 12, int(time[0][8]), int(time[0][10:12]), int(time[0][13:15]))
else:
    st = dt.datetime(2020, 12, int(time[0][8:10]), int(time[0][11:13]), int(time[0][14:16]))
if len(time[-1]) == 18:
    et = dt.datetime(2020, 12, int(time[-1][8]), int(time[-1][10:12]), int(time[-1][13:15]))
else:
    et = dt.datetime(2020, 12, int(time[-1][8:10]), int(time[-1][11:13]), int(time[-1][14:16]))
rt = et - st
rt = rt.total_seconds()
hour = round(rt / 3600, 2)
print(hour)
# print(int(time[0][6:8]))
# print(rt, type(rt))



# print(n)
# print(data)
# data = data[0].split('|')
# print(data)

# time.append(data[0].replace('CST', '').replace('2020', '').replace('2021', ''))
# print(time, power, voltage, current)

# files = os.listdir()
# print(files)
# cap = 'cap-mem.txt' in files
# info = 'battery_info.log' in files
# print(cap, info)
# raise ValueError('Failed to load txt or log file, check the file and try again.')

