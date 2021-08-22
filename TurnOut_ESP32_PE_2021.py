# ver 2.0 --> btCMD shortened from 4 to 3 Byte i.e. fw12 to fw12)
# ver 2.1 --> Added 3rd Servo's serie
#ver 3.0 --> added graphic component for TurnOut
# in caso di errore import blutooh https://stackoverflow.com/questions/62383192/pybluex-python-bluetooth-module-installation-error-error-in-pycharm

from tkinter import *
import tkinter as tk
from tkinter import Canvas, ttk
import serial
import time
import platform
import os.path
import serial.tools.list_ports
import bluetooth
import sys

#---------------------------------------------------------------------------------------------------------------------------


def disable_All():
    print("all disabled")

    Btn_2.config(fg="white", bg="gray", state=DISABLED)
    Btn_2.unbind('<Button-1>')
    Btn_7.config(fg="white", bg="gray", state=DISABLED)
    Btn_7.unbind('<Button-1>') 
    Btn_4.config(fg="white", bg="green", state=DISABLED)
    Btn_4.unbind('<Button-1>') 

# --------------------------------------------------------------------------------------------------------------------------
def BT_Connect():
    # port="/dev/tty.HC-06-DevB" #This will be different for various devices and on windows it will probably be a COM port.      

    ports = list(serial.tools.list_ports.comports())
    exitfor=""
    for p in ports:
        port = p[0]
        print(port)
        try:
            global bluetooth
            bluetooth = serial.Serial(port, 115200, write_timeout=1)
            bluetooth.flushInput()
            #print(p[1]
            if ("Bluetooth" in p[1]):
                print("la porta 1", port)
                bluetooth.write(b"test")
                time.sleep(0.1)
                print("la porta2 ", port)
                input_data = bluetooth.read()
                # These are bytes coming in so a decode is needed
                print(input_data.decode())
                if(input_data.decode()=='k'):
                    exitfor='y'
                lblConn = Label(window, text="Connected", fg="green")
                lblConn.place(x=200, y=190)
                return bluetooth

        except serial.serialutil.SerialException:
            print("NOT Connected")
            exitfor='n'
            #lblConn = Label(window, text="NO Bluetooth Connection", fg="red")
            #lblConn.place(x=250, y=200)
        
        if(exitfor=='y'):
            break
            
    if(exitfor=='n'):
        disable_All()
#------------------------------------------------------------------------------------------------------------------------
def Initialize ():

    global Btn_2
    global Dev_2_23
    global S_2
    global Btn_7
    global Dev_7
    global S_7
    
    Dev_2_23=w.create_line(400, 370, 470, 330, fill="#476042", width=3)
    Btn_2.config(bg="black")
    Btn_2.config(fg="white")
    Btn_2.config(command=lambda: turn("f23"))
    S_2=False

    Dev_7=w.create_line(370, 240, 300, 200, fill="#476042", width=3)
    Btn_7.config(bg="black")
    Btn_7.config(fg="white")
    Btn_7.config(command=lambda: turn("f77"))
    S_7=False

    Dev_1B_4=w.create_line(200, 370, 250, 400, fill="#476042", width=3)
    Btn_4.config(bg="black")
    Btn_4.config(fg="white")
    Btn_4.config(command=lambda: turn("f44"))
    S_4=False

#-----------------------------------------------------------------------------------------------------------------------
def turn(BtCmd):

    print(BtCmd)
    if (BtCmd == "exit"):
        print("EXIT")
        sys.exit()
        
    if (BtCmd == "init"):
        Initialize ()
    
    bluetooth.flushInput()  # This gives the bluetooth a little kick
    bluetooth.write(BtCmd.encode())
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
def Btn_2Press(Event):
    global S_2

    if S_2==False:
        Dev_2_23=w.create_line(400, 370, 470, 330,  fill="#1f1", width=3) 
        Btn_2.config(command=lambda: turn("r2"))
        Btn_2.config(bg="red")
        Btn_2.config(fg="blue")
        S_2=True
    else:
        Dev_2=w.create_line(400, 370, 470, 330, fill="#476042", width=3)
        Btn_2.config(command=lambda: turn("f2"))
        Btn_2.config(bg="Black")
        Btn_2.config(fg="White")
        S_2=False
#---------------------------------------------------------------------------------------------------------------------------
def Btn_7Press(Event):
    global S_7

    if S_7==False:
        Dev_7=w.create_line(370, 240, 300, 200,  fill="#1f1", width=3) 
        Btn_7.config(command=lambda: turn("r77"))
        Btn_7.config(bg="red")
        Btn_7.config(fg="blue")
        S_7=True
    else:
        Dev_7=w.create_line(370, 240, 300, 200, fill="#476042", width=3)
        Btn_7.config(command=lambda: turn("f77"))
        Btn_7.config(bg="Black")
        Btn_7.config(fg="White")
        S_7=False

#---------------------------------------------------------------------------------------------------------------------------
def Btn_4Press(Event):
    global S_4
    #Trk_2L=w.create_line(500, 180, 400, 165, fill="#476042", width=3) 
    if S_4==False:
        Dev_1B_4=w.create_line(200, 370, 250, 400,  fill="#1f1", width=3) 
        Btn_4.config(command=lambda: turn("r44"))
        Btn_4.config(bg="red")
        Btn_4.config(fg="blue")
        S_4=True
    else:
        Dev_1B_4=w.create_line(200, 370, 250, 400, fill="#476042", width=3)
        Btn_4.config(command=lambda: turn("f44"))
        Btn_4.config(bg="Black")
        Btn_4.config(fg="White")
        S_4=False

# ############################################## MAIN CODE ################################################################

# ============================================= Status Tracks declarations ===============================================
S_2=False
S_4=False
S_7=False

#============================== Form Creation ==========================================================================
window = Tk()
window.title("Welcome TurnOuts app")
window.geometry('640x480')
w = Canvas(window, width=640, height=480)
w.pack()
style = ttk.Style()
style.theme_use('default')

#=========================== TurnOut Schema Creation ====================================================================

Trk_1T=w.create_line(130, 50, 550, 50, fill="#476042", width=3)
Dev_1T_01=w.create_line(300, 50, 200, 90, fill="#476042", width=3)

Trk_2T=w.create_line(130, 90, 550, 90, fill="#476042", width=3)

Trk_2L=w.create_line(100, 100, 100, 300, fill="#476042", width=3)

Trk_1B=w.create_line(130, 370, 550, 370, fill="#476042", width=3)
Dev_1B_4=w.create_line(200, 370, 250, 400, fill="#476042", width=3)
Btn_4=Button(window, text="Turn 4", bg='Black',
            fg="White", command=lambda: turn("r44"))
Btn_4.place(x=130, y=375)
Trk_2B=w.create_line(130, 330, 550, 330, fill="#476042", width=3)
Dev_2=w.create_line(400, 370, 470, 330, fill="#476042", width=3)
Btn_2=Button(window, text="Turn 2", bg='Black',
            fg="White", command=lambda: turn("r22"))
Btn_2.place(x=400, y=375)   

Trk_2R=w.create_line(580, 100, 580, 300, fill="#476042", width=3)
Dev_5=w.create_line(580, 180, 540, 240, fill="#476042", width=3)
Trk_5=w.create_line(300, 240, 540, 240, fill="#476042", width=3)
Dev_7=w.create_line(370, 240, 300, 200, fill="#476042", width=3)
Btn_7=Button(window, text="Turn 7", bg='Black',
            fg="White", command=lambda: turn("r77"))
Btn_7.place(x=340, y=250)   

Dev_6=w.create_line(470, 240, 340, 170, fill="#476042", width=3)

# =============================================================================================================================
Btn_2.bind('<Button-1>', Btn_2Press)
# =============================================================================================================================
Btn_7.bind('<Button-1>', Btn_7Press)
# =============================================================================================================================
Btn_4.bind('<Button-1>', Btn_4Press)
# =============================================================================================================================
reset = Button(window, text="  Reset   ", command=lambda: turn("init"))
reset.place(x=300, y=450)
# =============================================================================================================================
esci = Button(window, text="    Exit    ", command=lambda: turn("exit"))
esci.place(x=380, y=450)
# ============================================================================================================================

PlatF=platform.system()
print(PlatF)
if (PlatF=="Windows"):
    BCK_COL="#F0F0F0"
else:
    BCK_COL="#D3D3D3"
BT_Connect()
 
window.mainloop()
