import visa,os,sys,threading,time
from pyvisa.resources.tcpip import TCPIPInstrument
from pyvisa.resources.usb import USBInstrument
from pyvisa.constants import *
import numpy as np
import PIL
from matplotlib import pyplot as plt

#设备总管理器
global rm
rm=visa.ResourceManager()

# 用于显示所有连接到电脑的设备名及其类型（USB/TCPIP)
def ResDiscover():
    global rm
    res=rm.list_resources()
    if len(res)>0:
        for dev in res:
            dev_name=str(dev)
            if dev_name.startswith('TCPIP'):
                print('LAN_INSTRUMENT')
                LAN_res=TCPIPInstrument(rm,dev_name)
                LAN_res.open()
                idn=LAN_res.query("*IDN?")
                print(idn)
                print('over')
                LAN_res.close()
            elif dev_name.startswith('USB'):
                print('USB_INSTRUMENT')
                USB_res=USBInstrument(rm,dev_name)
                USB_res.open()
                idn=USB_res.query("*IDN?")
                print(idn)
                print('over')
                USB_res.close()
    return(res)

#dev_name为设备的名称，由ResDiscover中获得，对于每台仪器其设备名称已固定
#WaveConnection返回的是某一个设备 

class WaveConnectionError(Exception):pass

def WaveConnection(dev_name):
    global rm
    try:
        if dev_name.startswith('TCPIP'):
            inst=TCPIPInstrument(rm,dev_name)
        elif dev_name.startswith('USB'):
            inst=USBInstrument(rm,dev_name)
        inst.open()
        return inst
    except WaveConnectionError:
        print("连接示波器失败")
        inst.close()
        return None

#inst为设备，返回的是PIL中的image
def WaveDisPlay(inst):
    inst.write("SAVe:ASSIgn:TYPe IMAGe")
    inst.write("SAVe:IMAGe:FILEFormat BMP")
    inst.write("SAVe:IMAGe D:/DPO2000/TEST.bmp")


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

res=ResDiscover()
inst=WaveConnection(res[0])


def ReadWav():
    inst.write('CURVE?')
    values=inst.read_raw()
    L=int(chr(values[1]))
    s=''
    for i in range(2,2+L):
        s=s+chr(values[i])
    s=int(s)
    data=[]
    y_unit=float(inst.query('WFMOutpre:YMUlt?'))
    x_unit=float(inst.query('WFMOutpre:XINcr?'))
    #print(set(values))
    for i in range(2+L,2+L+s):
        tmp=values[i]
        if tmp>127:
            tmp=tmp-255
        data.append(int(tmp)*y_unit)
    time=np.mat(range(len(data)))
    time=time*x_unit
    return time,data

def ReadInfo():
    inst.write('WAVFRM?')
    info=inst.read_raw()
    s=''
    for i in range(0,len(info)):
        if chr(info[i])=='#':
            break
        s=s+chr(info[i])
    return s


def PlotWave(time,data):
    f=11.76e3
    fig=plt.figure()
    ax=fig.add_subplot(111)
    plt.plot(time[0,:].T,data,color='r')
    sinew=np.sin(2*np.pi*f*time[0,:])
    plt.plot(time[0,:],max(data)*sinew[0,:],color='b')
    plt.show()

def GetXmax(info):
    s=info.split('"')
    s1=s[1].split(', ')
    XmaxS=s1[2]
    Xmax=''
    for i in range(len(XmaxS)):
        if (XmaxS[i]<'0' or XmaxS[i]>'9') and (XmaxS[i]!='.'):
            break
        Xmax=Xmax+XmaxS[i]
    Xmax=float(Xmax)
    return Xmax

time,data=ReadWav()
#info=ReadInfo()
PlotWave(time,data)
#GetXmax(info)



