from tkinter import *
from tkinter import ttk
from sender import *
from receiver import *
from ui_login import * 

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
from utils import *
from datetime import datetime
import os 
from shutil import copyfile
# from time import datetime
from key_log import *
from PIL import ImageTk, Image
import numpy as np
import cv2
import webbrowser
import time
class windown:
	screen=Tk()
	def __init__(self):
		self.screen.title('Gửi mail')
		scrW=self.screen.winfo_screenwidth()
		scrH=self.screen.winfo_screenheight()
		self.screen.geometry('1000x600+%d+%d'%(scrW/2-500,scrH/2-300))
		self.screen.configure(bg='#ffd5cc')
		self.screen.resizable(False, False)
		self.cv=Canvas(self.screen,height=600,width=1000,bg='#cceaff')
		self.cv.place(x=0,y=0)
	def destroy():
		self.cv.destroy()
		self.screen.destroy()
class content_mail:
	mail_s=""
	password_s=""
	mail_r=""
	password_r=""
	get_data=False
	def __init__(self,wd):
		self.parent=wd
		img = ImageTk.PhotoImage(Image.open("source/control.png"))
		self.label1 = Label(self.parent.cv,image=img)
		self.label1.image = img
		self.label1.place(x=0, y=0)
		self.label_mail=Label(self.parent.cv,text="Please enter your email of sender: ")
		self.label_mail.place(x=130,y=170)
		self.AddEnt=Entry(wd.cv,font="Times 20 bold",width=50)
		self.AddEnt.place(x=130,y=200)
		self.label_pass=Label(self.parent.cv,text="Please enter your password of sender: ")
		self.label_pass.place(x=130,y=250)
		self.PassEnt=Entry(wd.cv,font="Times 20 bold",width=50, show="*")
		self.PassEnt.place(x=130,y=280)
		
		self.label_mail_r=Label(self.parent.cv,text="Please enter your email of receiver: ")
		self.label_mail_r.place(x=130,y=320)
		self.AddEnt_r=Entry(wd.cv,font="Times 20 bold",width=50)
		self.AddEnt_r.place(x=130,y=350)
		self.label_pass_r=Label(self.parent.cv,text="Please enter your password of receiver: ")
		self.label_pass_r.place(x=130,y=390)
		self.PassEnt_r=Entry(wd.cv,font="Times 20 bold",width=50, show="*")
		self.PassEnt_r.place(x=130,y=420)
		self.Submit=Button(wd.cv,
        text='Đăng nhập',
        bg='#ffecb4',
        fg='black',
        command=self.get_result,
        font='Times 15 bold',
        height=1,
        width=20,
        )
		self.Regis=Button(wd.cv,
        text='Đăng ký',
        bg='#ffecb4',
        fg='black',
        command=self.open_fun,
        font='Times 15 bold',
        height=1,
        width=20,
        )
		self.Submit.place(x=130,y=470)
		self.Regis.place(x=420,y=470)
		self.label_kq=Label(self.parent.cv,text="")
		self.label_kq.place(x=420,y=470)
	def get_result(self):
		self.mail_s=self.AddEnt.get()
		self.password_s=self.PassEnt.get()
		self.mail_r=self.AddEnt_r.get()
		self.password_r=self.PassEnt_r.get()
		self.get_data=True
		self.log_in()
	def open_fun(self):
		webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
	def destroy(self):
		self.Submit.destroy()
		self.Regis.destroy()
		self.AddEnt.destroy()
		self.AddEnt_r.destroy()
		self.PassEnt.destroy()
		self.PassEnt_r.destroy()
		self.label1.destroy()
		self.label_mail.destroy()
		self.label_pass.destroy()
		self.label_pass_r.destroy()
		self.label_mail_r.destroy()
		self.label_kq.destroy()
		self.parent.cv.destroy()
		self.parent.screen.destroy()
	def log_in(self):
		print('run')
		try:
		    self.sender = Sender(self.mail_s,self.password_s)
		    self.receiver = Receiver (self.mail_r,self.password_r)
		    self.label_kq=Label(self.parent.cv,text="Success")
		    self.label_kq.place(x=420,y=540)
		    self.destroy()
		except:
		    self.label_kq=Label(self.parent.cv,text="Some thing wrong")
		    self.label_kq.place(x=420,y=540)
#-----------------------------------------
