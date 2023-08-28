import tkinter as tk
from tkinter import *
window=tk.Tk()

window.geometry("300x300")
window.title("calculator")

data=StringVar()
def click(txt):
    global value
    value=value+str(txt)
    data.set(value)
def clear():
    global value
    value=""
    data.set("")
def equal():
    global value
    res=str(eval(value))
    data.set(res)

display=tk.Entry(window,textvariable=data,bd=30,width=40,bg="light blue",justify="right")
display.pack()
display.grid(row=0,columnspan=4)

value=""

button1=tk.Button(window,text="1",bd=10,width=4,height=2,font="Ariel",command=lambda:click(1))
button1.grid(row=1,column=0)
button2=tk.Button(window,text="2",bd=10,width=4,height=2,font="Ariel",command=lambda:click(2))
button2.grid(row=1,column=1)
button3=tk.Button(window,text="3",bd=10,width=4,height=2,font="Ariel",command=lambda:click(3))
button3.grid(row=1,column=2)
buttonmul=tk.Button(window,text="*",bd=10,width=4,height=2,font="Ariel",command=lambda:click("*"))
buttonmul.grid(row=1,column=3)
button4=tk.Button(window,text="4",bd=10,width=4,height=2,font="Ariel",command=lambda:click(4))
button4.grid(row=2,column=0)
button5=tk.Button(window,text="5",bd=10,width=4,height=2,font="Ariel",command=lambda:click(5))
button5.grid(row=2,column=1)
button6=tk.Button(window,text="6",bd=10,width=4,height=2,font="Ariel",command=lambda:click(6))
button6.grid(row=2,column=2)
buttonadd=tk.Button(window,text="+",bd=10,width=4,height=2,font="Ariel",command=lambda:click("+"))
buttonadd.grid(row=2,column=3)

button7=tk.Button(window,text="7",bd=10,width=4,height=2,font="Ariel",command=lambda:click(7))
button7.grid(row=3,column=0)
button8=tk.Button(window,text="8",bd=10,width=4,height=2,font="Ariel",command=lambda:click(8))
button8.grid(row=3,column=1)
button9=tk.Button(window,text="9",bd=10,width=4,height=2,font="Ariel",command=lambda:click(9))
button9.grid(row=3,column=2)
buttonsub=tk.Button(window,text="-",bd=10,width=4,height=2,font="Ariel",command=lambda:click("-"))
buttonsub.grid(row=3,column=3)

buttonclr=tk.Button(window,text="c",bd=10,width=4,height=2,font="Ariel",command=lambda:clear())
buttonclr.grid(row=4,column=0)
button0=tk.Button(window,text="0",bd=10,width=4,height=2,font="Ariel",command=lambda:click(0))
button0.grid(row=4,column=1)
buttoneq=tk.Button(window,text="=",bd=10,width=4,height=2,font="Ariel",command=lambda:equal())
buttoneq.grid(row=4,column=2)
buttondiv=tk.Button(window,text="/",bd=10,width=4,height=2,font="Ariel",command=lambda:click("/"))
buttondiv.grid(row=4,column=3)

tk.mainloop()


