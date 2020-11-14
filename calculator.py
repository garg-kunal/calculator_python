import tkinter
from tkinter import *
# from function import change
from functools import partial
# from tkinter.ttk import * 

win=Tk()

x1=StringVar()
x2=StringVar()
op=StringVar()
fin=StringVar()
fin.set("");
    
def change(x):
    fin.set(fin.get()+str(x)) 
    if(x == '+' or x == '-' or x == '*' or x == '/' ):
        op.set(op.get() + str(x))
    else:
        if(op.get()==""):
            x1.set(x1.get() + str(x))
             
        else:
            x2.set(x2.get() + str(x))      
    return fin.get()



def equal():
    if(op.get() == "+"):
        fin.set(int(x1.get())+int(x2.get()))
    elif(op.get()== "-"):
        fin.set(int(x1.get())-int(x2.get()))
    elif(op.get()=="*"):
        fin.set(int(x1.get())*int(x2.get())) 
    elif(op.get()=="/"):
        fin.set(int(x1.get())/int(x2.get())) 
def cancel():
    x1.set('')
    x2.set('')
    fin.set('')
    op.set('')



win.title("Calculator")
# win.geometry("500x500")
# win.attributes("-fullscreen",True)
topframe = Frame(win)
topframe.grid(row=0,column=1 )
lb=Label(topframe,textvariable=fin,bg="white",width="150")

lb.grid(row=1)
bottomframe = Frame(win)
bottomframe.grid(row=1,column=1 )

btn1=Button(bottomframe,text="1",padx=10,pady=10,command=partial(change,"1"),height=4, width=5)
btn2=Button(bottomframe,text="2",padx=10,pady=10,command=partial(change,"2"),height=4, width=5)
btn3=Button(bottomframe,text="3",padx=10,pady=10,command=partial(change,"3"),height=4, width=5)
btn4=Button(bottomframe,text="4",padx=10,pady=10,command=partial(change,"4"),height=4, width=5)
btn5=Button(bottomframe,text="5",padx=10,pady=10,command=partial(change,"5"),height=4, width=5)
btn6=Button(bottomframe,text="6",padx=10,pady=10,command=partial(change,"6"),height=4, width=5)
btn7=Button(bottomframe,text="7",padx=10,pady=10,command=partial(change,"7"),height=4, width=5)
btn8=Button(bottomframe,text="8",padx=10,pady=10,command=partial(change,"8"),height=4, width=5)
btn9=Button(bottomframe,text="9",padx=10,pady=10,command=partial(change,"9"),height=4, width=5)
btn0=Button(bottomframe,text="0",padx=10,pady=10,command=partial(change,"0"),height=4, width=5)
btn10=Button(bottomframe,text="+",padx=10,pady=10,command=partial(change,"+"),height=4, width=5)
btn11=Button(bottomframe,text="=",padx=10,pady=10,command=equal,height=4, width=5)
btn12=Button(bottomframe,text="-",padx=10,pady=10,command=partial(change,"-"),height=4, width=5)
btn13=Button(bottomframe,text="*",padx=10,pady=10,command=partial(change,"*"),height=4, width=5)
btn14=Button(bottomframe,text="/",padx=10,pady=10,command=partial(change,"/"),height=4, width=5)
btn15=Button(bottomframe,text="Del",padx=10,pady=10,command=cancel,height=4, width=5)



btn1.grid(row=4,column=1)
btn2.grid(row=4,column=2)
btn3.grid(row=4,column=3)
btn4.grid(row=5,column=1)
btn5.grid(row=5,column=2)
btn6.grid(row=5,column=3)
btn7.grid(row=6,column=1)
btn8.grid(row=6,column=2)
btn9.grid(row=6,column=3)
btn0.grid(row=7,column=2)
btn10.grid(row=4,column=4)
btn11.grid(row=7,column=3)
btn12.grid(row=5,column=4)
btn13.grid(row=6,column=4)
btn14.grid(row=7,column=4)
btn15.grid(row=7,column=1)







win.mainloop()
