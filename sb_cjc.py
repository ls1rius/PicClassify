#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import sys
from tkinter import *
from PIL import Image
from tkinter import messagebox

with open("./config.json",'r') as load_f:
	load_config = json.load(load_f)

fileDirPath = load_config['fileDirPath']
typeList = load_config['typeList']
fileNameList = []

for filename in os.listdir(fileDirPath):
	if(filename.endswith('jpg') or filename.endswith('png')):
		fileNameList.append(filename)

print(fileNameList)

for item in typeList:
	if not os.path.exists(item['typeDirPath']):
		os.mkdir(item['typeDirPath'])

class SBCJC:
	def __init__(self):
		self.window = Tk() #创建窗口
		self.window.title("sb cjc") #给窗口命名
		self.picIdx = 0
		self.filename = fileNameList[self.picIdx]
		filePath = fileDirPath+"\\"+self.filename
		img = PhotoImage(file=filePath)
		self.label = Label(self.window,image=img)
		self.label.pack()

		#创建frame的框架，窗口window为这个框架的父容器
		self.frame = Frame(self.window)
		self.frame.pack()

		Button(self.frame, text=typeList[0]['typeName'], command = lambda :self.saveToFile(typeList[0]['typeDirPath']+"\\"+self.filename)).grid(row = (int)(0/10), column = (0%10))
		Button(self.frame, text=typeList[1]['typeName'], command = lambda :self.saveToFile(typeList[1]['typeDirPath']+"\\"+self.filename)).grid(row = (int)(1/10), column = (1%10))
		Button(self.frame, text=typeList[2]['typeName'], command = lambda :self.saveToFile(typeList[2]['typeDirPath']+"\\"+self.filename)).grid(row = (int)(2/10), column = (2%10))
		Button(self.frame, text=typeList[3]['typeName'], command = lambda :self.saveToFile(typeList[3]['typeDirPath']+"\\"+self.filename)).grid(row = (int)(3/10), column = (3%10))

		#创建事件循环直到关闭主窗口
		self.window.mainloop()

	def saveToFile(self, savePath):


		if self.picIdx >= len(fileNameList):
			messagebox.showinfo(message="已经是最后一张了")
			return
		
		filePath = fileDirPath+"\\"+self.filename
		img = Image.open(filePath)
		img.save(savePath)

		print((str)(self.picIdx) + "\n")
		print(self.filename+"------>"+savePath + "\n")
		with open("./log.txt","a+") as f:
			f.write((str)(self.picIdx) + "\n")
			f.write(self.filename+"------>"+savePath + "\n")
		f.close()

		self.picIdx = self.picIdx + 1
		self.showPic()
		

	def showPic(self):
		# 报错警告
		try:
			self.filename = fileNameList[self.picIdx]
		except:
			pass
		filePath = fileDirPath+"\\"+self.filename

		img = PhotoImage(file=filePath)
		self.label.config(image=img)
		self.label.image = img

SBCJC()