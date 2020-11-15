import datetime

import serial
import time

import binascii
first_time = datetime.datetime.now

#ser = serial.Serial("/dev/tty.usbserial-14140",115200)
ser = serial.Serial("com4",115200)
if ser.isOpen():
    print('open sucess')
for i in range(10000):
    j = (hex(i)).replace("0x","")
    k = j.zfill(4)
    # if i<=1:
    data = "55aa02000700080001000300060007000700ff0009" + k  #55aa针头，02：代表扭矩，01代表角速度，后面每四个代表一个扭矩数据
    #     #     # else:
    #     data = "55aa02000700080001000300060007000700ff0009" + k
    # print(data,i)
    #这里发出去的数据必须是偶数位
    cmd = bytes().fromhex(data)
    ser.write(cmd)
    print(i,cmd)
    time.sleep(0.1)  #0.001是1毫秒=1000Hz
    # time.sleep(0.00001)
print("finish")
# last_time = datetime.datetime.now()
# use_time = float(last_time) - float(first_time)
# print(last_time)

