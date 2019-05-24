from airtest.core.api import *


def device_zbzh(x,y):
    devs= ["127.0.0.1:62001", "127.0.0.1:62025", "172.16.140.72:5566"] #连接的设备数组
    for i in range(len(devs)):
        device = connect_device('Android:///' + devs[i] + '')
        w, h = device.get_current_resolution()
        pos = [(x/w)*w, (y/h)*h]
        print(w, h )
    return pos


print(device_zbzh(0.5,0.5))