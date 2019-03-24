from tkinter import *

import random
import time 
import datetime 

root=Tk()

root.geometry("1200x6000")
root.title("QR Code 1.0")


header=Frame(root,width=1600)
header.pack()

body=Frame(root,width=1000)
body.pack()


header=Frame(root,width=1600)
header.pack()

body=Frame(root,width=1000)
body.pack()

localtime=time.asctime(time.localtime(time.time()))
label1=Label(header,font=('helvetica',50,'bold'),text="QR Code Generation",fg="Black",bd=10,anchor='w')
label1.grid(row=0,column=0)

label2=Label(header,text=localtime,fg="Blue",bd=10,anchor='w')
label2.grid(row=1,column=0)

import base64
import pyqrcode 
from pyqrcode import QRCode



message=StringVar()
Filename=StringVar()
# mode=StringVar()
# result=StringVar()

#clear the space
def Clear():
    message.set("")
    Filename.set("")

def action(message):
    url=pyqrcode.create(message.get())
    url.svg(Filename.get()+".svg",scale=8)

def Ref():
    #print("reference")
    action(message)
    #print(type(message.get()))
    #action(message)

#Name
label_name=Label(body,text="Name :",fg="Brown",font=('helvetica',20,'bold'))
label_name.grid(row=0,column=0)

Message_entry=Entry(body,textvariable=message)
Message_entry.grid(row=0,column=1)


# Filename_entry
label_name=Label(body,text="Filename :",fg="Brown",font=('helvetica',20,'bold'))
label_name.grid(row=1,column=0)

Filename_entry=Entry(body,textvariable=Filename)
Filename_entry.grid(row=1,column=1)



#Generate
Show_button=Button(header,text="Generate",fg="red",command=Ref)
Show_button.grid(row=5,column=1)


#clear
Clear_button=Button(header,text="Clear",fg="red",command=Clear)
Clear_button.grid(row=5,column=2)



root.mainloop()




