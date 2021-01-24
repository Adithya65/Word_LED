import RPi.GPIO as gpio
from tkinter import *

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(8,gpio.OUT,initial=gpio.LOW)
gpio.setup(12,gpio.OUT,initial=gpio.LOW)
gpio.setup(16,gpio.OUT,initial=gpio.LOW)
gpio.setup(18,gpio.OUT,initial=gpio.LOW)
gpio.setup(22,gpio.OUT,initial=gpio.LOW)
def exe():
    word=e1.get()
    e1.delete(0,END)
    
    length=len(word)
    if (length==1):
        gpio.output(8,gpio.HIGH)
    if (length ==2):
        gpio.output(8,gpio.HIGH)
        gpio.output(12,gpio.HIGH)
    if(length ==3):
        gpio.output(8,gpio.HIGH)
        gpio.output(12,gpio.HIGH)
        gpio.output(16,gpio.HIGH)
        
    if (length ==4):
        gpio.output(8,gpio.HIGH)
        gpio.output(12,gpio.HIGH)
        gpio.output(16,gpio.HIGH)
        gpio.output(18,gpio.HIGH)
        gpio.output(22,gpio.HIGH)
def stop():
    gpio.output(8,gpio.LOW)
    gpio.output(12,gpio.LOW)
    gpio.output(16,gpio.LOW)
    gpio.output(18,gpio.LOW)
    gpio.output(22,gpio.LOW)
    
root=Tk()
root.geometry("440x240")
lab=Label(root,text="enter the word",bg="#FFFF99")
lab.grid(row=0,column=0)
e1=Entry(root,bg="#FFB6C1")
e1.grid(row=0,column=1)
butt=Button(root,text="enter",command=exe).grid(row=1,column=1)
b3 = Button(root, text='Quit', bg= "cyan", command=stop)
b3.grid(row=2, column=3)
root.mainloop()
