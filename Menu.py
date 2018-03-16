#Menu 1.0
print("======STARTING=========")
import os
def clear():
    os.system("clear")
print("Welcome")
options=[]
class option:
    def __init__(self,cmd,name,confirm=False):
        self.name=name
        self.cmd=cmd
        self.confirm=confirm
        options.append(self)
    def do(self):
        action="y"
        if self.confirm:
            action=input("Confirm Y/N")
        action=action.lower()
        if not action in ["y","yes","y","ok"]:
            return 2
        try:
            os.system(self.cmd)
            return 0
        except:
            return 1

try:
    width,height=os.get_terminal_size(0)
except:
    width=40
    height=50
option("echo nothing","sample",True)
option("sudo apt-get -y update&&sudo apt-get -y upgrade&&sudo apt-get -y rpi-update","Upgrade and update",True)
option("lsusb","usbutil")

import time
time.sleep(1)
clear()
def loadmenu():
    x=""
    c=0
    
    print(width*"=")
    print("x to quit")
    while x!="x" or not c==(len(options)-1):
        try:
            
            x=input("")
            if x!="" and x!="x":
                o=options[int(x)].do()
                if o==0:
                    print("Command ran")
                elif o==1:
                    print("error")
                elif o==2:
                    print("canceled")
                continue
            if x=="x":
                break
            print("["+str(c)+"] "+options[c].name)
            
            c=c+1
            
        except Exception as e:
            print("ERROR code:1 error:"+str(e))
if __name__=="__main__":
    loadmenu()
