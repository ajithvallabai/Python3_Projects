from tkinter import *
from otherfunctions import *

expression=""

#action performed when a button is pressed
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        result=evaluation(expression)
        #result=eval(expression) #this line can also be used instead of above line 
        #in order to show how to import functions from other file i have used above line 
        equation.set(result)
    except:
        equation.set("Error 0xd232232211101")

#clearing the field
def clear():
    global expression    
    expression=""
    equation.set(expression)

if __name__=="__main__":
    #initialising tkinter()
    r=Tk()
    r.title('Calculator')
    r.configure(background="light blue")

    #Two frames are made one for digit buttons another for entry field
    frame=Frame(r)
    frame_entry=Frame(r)
    frame_entry.pack()
    frame.pack()

    #buttons
    button1=Button(frame,text='1',width=5,height=5,command=lambda:press(1)).grid(row=0,column=0)
    button2=Button(frame,text='2',width=5,height=5,command=lambda:press(2)).grid(row=0,column=1)
    button3=Button(frame,text='3',width=5,height=5,command=lambda:press(3)).grid(row=0,column=2)
    button4=Button(frame,text='4',width=5,height=5,command=lambda:press(4)).grid(row=1,column=0)
    button5=Button(frame,text='5',width=5,height=5,command=lambda:press(5)).grid(row=1,column=1)
    button6=Button(frame,text='6',width=5,height=5,command=lambda:press(6)).grid(row=1,column=2)
    button7=Button(frame,text='7',width=5,height=5,command=lambda:press(7)).grid(row=2,column=0)
    button8=Button(frame,text='8',width=5,height=5,command=lambda:press(8)).grid(row=2,column=1)
    button9=Button(frame,text='9',width=5,height=5,command=lambda:press(9)).grid(row=2,column=2)
    button0=Button(frame,text='0',width=5,height=5,command=lambda:press(0)).grid(row=3,column=0)

    buttonplus=Button(frame,text='+',width=5,height=5,command=lambda:press('+')).grid(row=0,column=3)
    buttonminus=Button(frame,text='-',width=5,height=5,command=lambda:press('-')).grid(row=1,column=3)
    buttonastr=Button(frame,text='*',width=5,height=5,command=lambda:press('*')).grid(row=2,column=3)
    buttondiv=Button(frame,text='/',width=5,height=5,command=lambda:press('/')).grid(row=3,column=1)
    buttonequal=Button(frame,text='=',width=5,height=5,command=lambda:equal()).grid(row=3,column=2)
    buttonclr=Button(frame,text='Clear',width=5,height=5,command=lambda:clear()).grid(row=3,column=3)

    #Entry field formation
    equation=StringVar()
    e1=Entry(frame_entry,textvariable=equation,width=35).grid(row=4)
    
    #to run the mainloop infinite times
    r.mainloop()