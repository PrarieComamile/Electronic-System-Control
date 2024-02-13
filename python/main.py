import serial
import time
import alsaaudio
import pyautogui
import os

ser = serial.Serial('/dev/ttyUSB0', 9600)
mixer = alsaaudio.Mixer('Master')


onceki_deger = False
onceki_deger1 = False
onceki_deger2 = False

def discord():
    os.system("discord")
    
def update():
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(1)
    pyautogui.write("sudo apt update")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("[*Sisteminizin Şifresi]")
    pyautogui.press("enter")
    
def func():
    os.system("code")
    
    
    
while True:
    # Arduinodan gelen veriyi okuyun
    data = ser.readline().decode().rstrip()
    data = data.split("+")
    
    
    try:
        volume = int(data[3])/1023 * 100
        mixer.setvolume(int(volume))
        
        if data[0] == "0":
            onceki_deger = False
        if data[1] == "0":
            onceki_deger1 = False
        if data[2] == "0":
            onceki_deger2 = False
        
        if data[0] == "1" and onceki_deger==False:
            onceki_deger = True
            discord()
            time.sleep(0.1)
            
        if data[1] == "1" and onceki_deger1==False:
            onceki_deger1 = True
            update()
            time.sleep(0.1)
            
        if data[2] == "1" and onceki_deger2==False:
            onceki_deger2 = True
            func()
            time.sleep(0.1)
                
    except:
        print("Hata!")



    print(data)
