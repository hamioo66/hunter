# -*-coding:UTF-8 -*-
#利用Tkinter创建一个用户登录界面
from Tkinter import*
root=Tk()
root.title(u"用户登录")
root.geometry("300x200")
root.resizable(width=False,height=True)
import  Logintest
login=Button(root,text=u"执行添加资讯",command=Logintest.main)
login.grid(row=2,column=1,sticky=E)
root.mainloop()
