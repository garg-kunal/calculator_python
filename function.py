import tkinter
from tkinter import *

x1=StringVar()
x2=StringVar()

def add():
    
def sub(x1,x2):
    return x1-x2
def mul(x1,x2):
    return x1*x2
def div(x1,x2):
    return x1/x2     
def change(x1):
    if(x1 == '+' or x1 == '-' or x1 == '*' or x1 == '/' ):
        x2.get()+x1
    else:
        x1.get()+x1    
def equal():
    if(op.get() == "+"):
        print(int(x1.get())+int(x2.get()))
    elif(op.get()== "-"):
        print(int(x1.get())-int(x2.get()))
    elif(op.get()=="*"):
        print(int(x1.get())*int(x2.get())) 
    else:
        print(int(x1.get())/int(x2.get()))          


