from tkinter import *

import random
import time 
import datetime 

root=Tk()

root.geometry("1200x6000")
root.title("Encrypt and Decrypt 1.0")


header=Frame(root,width=1600)
header.pack()

body=Frame(root,width=1000)
body.pack()

localtime=time.asctime(time.localtime(time.time()))
label1=Label(header,font=('helvetica',50,'bold'),text="Cipher Generation",fg="Black",bd=10,anchor='w')
label1.grid(row=0,column=0)

label2=Label(header,text=localtime,fg="Blue",bd=10,anchor='w')
label2.grid(row=1,column=0)

import base64


message=StringVar()
key=StringVar()
mode=StringVar()
result=StringVar()

#clear the space
def Clear():
    message.set("")
    key.set("")
    mode.set("")
    result.set("")

def encode(key,clear):
	#varaible to store the encoded thing
	enc=[]
	for i in range(len(clear)):
		# using modulo and getting the key digit
		key_c=key[i%len(key)]
		# after comming the ascii value of keydigit and message digit .storage is done
		enc_c=chr((ord[clear[i]]+ord(key_c))%256)
		
		enc.append(enc_c)
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
	dec=[]
	# base64 conversion is done
	enc=base64.urlsafe_b64encode(enc).decode()

	for i in range(len(enc)):
		# using modulo and getting the key digit
		key_c=key[i%len(key)]
		# after comming the ascii value of key digit and message digit is stored
		dec_c=chr((256+ord(enc[i])-ord(key_c))%256)
		dec.append(dec_c)
	return "".join(dec)

def Ref():
	print("Message: ",message.get())
	clear=message.get()
	k=key.get()
	if mode.get()=='e':
		result.set(encode(k,clear))
	elif mode =='d':
		result.set(decode(k,clear))

#Name
label_name=Label(body,text="Message :",fg="Brown",font=('helvetica',20,'bold'))
label_name.grid(row=0,column=0)

Name_entry=Entry(body,textvariable=message)
Name_entry.grid(row=0,column=1)

# Key_entry
label_name=Label(body,text="Key :",fg="Brown",font=('helvetica',20,'bold'))
label_name.grid(row=1,column=0)

Message_entry=Entry(body,textvariable=key)
Message_entry.grid(row=1,column=1)



# Mode_entry
label_name=Label(body,text="Mode :",fg="Brown",font=('helvetica',20,'bold'))
label_name.grid(row=2,column=0)

Message_entry=Entry(body,textvariable=mode)
Message_entry.grid(row=2,column=1)


# Result_entry
label_name=Label(body,text="Result :",fg="Brown",font=('helvetica',20,'bold'))
label_name.grid(row=3,column=0)


Message_entry=Entry(body,textvariable=result)
Message_entry.grid(row=3,column=1)



#show 
Show_button=Button(header,text="Show",fg="red",command=Ref)
Show_button.grid(row=5,column=1)


#clear
Clear_button=Button(header,text="Clear",fg="red",command=Clear)
Clear_button.grid(row=5,column=2)


root.mainloop()
