# from PyQt5.QtCore import *
import serial
# import threading
#
#
# time_x = []
# shuiwen_y = [0,]
# youya_y = [0,]
# fadongji_y = [0,]
# genqieqiyouya_y = [0,]
# genqieqiliuliang_y = [0,]
# shusonggunyouya_y = [0,]
# shusonggunliuliang_y = [0,]
# qieduandaoyouya_y = [0,]
# qieduandaoliuliang_y = [0,]
# paifengjiyouya_y = [0,]
# paifengjiliuliang_y = [0,]
# erjishusongyouya_y = [0,]
# erjishusongliuliang_y = [0,]
#
# class WorkThread(threading.Thread):
#     def __init__(self):
#         super(WorkThread,self).__init__()
#
#     def run(self):
#         # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
#         # portx = "/dev/ttyS1"
#         portx = "COM5"
#         # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
#         bps = 115200
#         # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
#         timex = 5
#         # 打开串口，并得到串口对象
#         ser = serial.Serial(portx, bps, timeout=timex)
#         global time_x, shuiwen_y, youya_y, fadongji_y, genqieqiyouya_y, genqieqiliuliang_y,shusonggunyouya_y, shusonggunliuliang_y,\
#                qieduandaoyouya_y, qieduandaoliuliang_y, paifengjiyouya_y, paifengjiliuliang_y, erjishusongyouya_y, erjishusongliuliang_y
#         while True:
#             line = ser.read(23)
#             # print(line)
#             if line:
#                 data = line.hex()
#                 # print(data)
#                 # data2 = int(data,10)
#                 data2 = '0x' + data[6:10]
#                 genqieqiyouya_y.append(int(data2,16))
#                 data3 = '0x' + data[10:14]
#                 shusonggunyouya_y.append(int(data3,16))
#                 data4 = '0x' + data[14:18]
#                 qieduandaoyouya_y.append(int(data4, 16))
#                 data5 = '0x' + data[18:22]
#                 paifengjiyouya_y.append(int(data5, 16))
#                 data6 = '0x' + data[22:26]
#                 erjishusongyouya_y.append(int(data6, 16))
#                 data7 = '0x' + data[26:30]
#                 shuiwen_y.append(int(data7, 16))
#                 data8 = '0x' + data[30:34]
#                 youya_y.append(int(data8, 16))
#                 data9 = '0x' + data[34:38]
#                 fadongji_y.append(int(data9, 16))
#                 # print(genqieqiyouya_y,shusonggunyouya_y)
#                 # print(data2)
#                 # print(int(data2,16))
#             #     data = int(line,10)
#             #     print(data)
#         # self.trigger.emit()
#
# if __name__ == '__main__':
#     thread = WorkThread()
#     thread.start()