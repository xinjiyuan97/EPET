import visa,os,sys,threading,time
from pyvisa.resources.tcpip import TCPIPInstrument
from pyvisa.resources.usb import USBInstrument
from pyvisa.constants import *
import numpy as np
import PIL

#设备总管理器
global rm
rm=visa.ResourceManager()

# 用于显示所有连接到电脑的设备名及其类型（USB/TCPIP)
def ResDiscover():
    global rm
    res=rm.list_resources()
    if len(res)>0:
        for dev in res:
            dev_name=str(des)
            if dev_name.startswith('TCPIP'):
                print('LAN_INSTRUMENT')
                LAN_res=TCPIPInstrument(rm,dev_name)
                LAN_res.open()
                idn=LAN_res.query_ascii_values("*IDN?")
                print(idn)
                print('over')
                LAN_res.close()
            elif dev_name.startswith('USB'):
                print('USB_INSTRUMENT')
                USB_res=USBInstrument(rm,dev_name)
                USB_res.open()
                idn=USB_res.query_ascii_values("*IDN?")
                print(idn)
                print('over')
                USB_res.close()
    return(res)

#dev_name为设备的名称，由ResDiscover中获得，对于每台仪器其设备名称已固定
#WaveConnection返回的是某一个设备 
def WaveConnection(dev_name):
    global rm
    inst=TCPIPInstrument(rm,dev_name)
    inst.open()
    return inst

#inst为设备，返回的是PIL中的image
def WaveDisPlay(inst):
    inst.write(":DISPlay:DATA?")
    ori=inst.read_raw()
    bmp=ori[11:]
    img = PIL.Image.frombuffer('RGB', (800,480), ori)
    return img

#inst为设备，chan指设备的第几个通道，返回横纵坐标X、Y，类型为list
def WaveData(inst,chan):
    inst.write(":WAV:SOUR CHAN"+str(chan))
    inst.write(":WAV:MODE NORM")
    inst.write(":WAV:FORM ASCii")
    Y_ori=inst.query_ascii_values(":WAV:DATA?")
    xINCRE=float(inst.query_ascii_values(":WAV:XINC?"))
    scale=float(inst.query_ascii_values(":CHAN1l:SCAL?"))
    Y=[]
    X=[]
    sum=0
    for i in len(Y_ori):
        tmp=float(Y_ori)-127
        Y.append(tmp/128*5*scale)
        X.append(sum)
        sum+=xINCRE
    return (X,Y)














