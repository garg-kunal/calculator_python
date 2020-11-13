import tkinter
from tkinter import *
# from function import change
from functools import partial
# from tkinter.ttk import * 

win=Tk()

x1=StringVar()
x2=StringVar()
op=StringVar()
    
def change(x):
    if(x == '+' or x == '-' or x == '*' or x == '/' ):
        op.set(op.get() + str(x))
    else:
        if(op.get()==""):
            x1.set(x1.get() + str(x))  
        else:
            x2.set(x2.get() + str(x))      



def equal():
    if(op.get() == "+"):
        print(int(x1.get())+int(x2.get()))
    elif(op.get()== "-"):
        print(int(x1.get())-int(x2.get()))
    elif(op.get()=="*"):
        print(int(x1.get())*int(x2.get())) 
    else:
        print(int(x1.get())/int(x2.get()))        



win.title("Calculator")
win.geometry("500x500")
ans=45
lb=Entry(win,text="Answer is:")
lb.grid(row=1,column=1)

btn1=Button(win,text="1",padx=10,pady=10,command=partial(change,"1"))
btn2=Button(win,text="2",padx=10,pady=10,command=partial(change,"2"))
btn3=Button(win,text="3",padx=10,pady=10,command=partial(change,"3"))
btn4=Button(win,text="4",padx=10,pady=10,command=partial(change,"4"))
btn5=Button(win,text="5",padx=10,pady=10,command=partial(change,"5"))
btn6=Button(win,text="6",padx=10,pady=10,command=partial(change,"6"))
btn7=Button(win,text="7",padx=10,pady=10,command=partial(change,"7"))
btn8=Button(win,text="8",padx=10,pady=10,command=partial(change,"8"))
btn9=Button(win,text="9",padx=10,pady=10,command=partial(change,"9"))
btn0=Button(win,text="0",padx=10,pady=10,command=partial(change,"0"))
btn10=Button(win,text="+",padx=10,pady=10,command=partial(change,"+"))
btn11=Button(win,text="=",padx=10,pady=10,command=equal)

btn10.grid(row=10,column=20)
btn11.grid(row=40,column=30)
btn1.grid(row=4,column=2)
btn2.grid(row=4,column=3)
btn3.grid(row=4,column=4)
btn4.grid(row=5,column=2)
btn5.grid(row=5,column=3)
btn6.grid(row=5,column=4)
btn7.grid(row=6,column=2)
btn8.grid(row=6,column=3)
btn9.grid(row=6,column=4)
btn0.grid(row=7,column=3)







win.mainloop()
