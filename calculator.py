from tkinter import *

def click(event):
    global value
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if value.get().isdigit():
            value1=int(value.get())
        else:
            value1=eval(screen.get())
        value.set(value1)
        screen.update()
    elif text == "C":
        value.set("")
        screen.update()
    else:
        value.set(value.get() + text)
        screen.update()

root=Tk()
root.geometry("644x900")
root.title("Calculator By Sanjay")
value = StringVar()
value.set("")

screen=Entry(root,textvar=value,font="lucida 40 bold")
screen.pack(padx=10,pady=30,ipadx=8)

# First frame of 3 buttons
f1=Frame(root,bg="grey")
f1.pack()

b=Button(f1,text="9",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="8",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="7",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="-",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


# second frame of 3 buttons
f1=Frame(root,bg="grey")
f1.pack()

b=Button(f1,text="6",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="5",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="4",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="+",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


# third frame of 3 buttons
f1=Frame(root,bg="grey")
f1.pack()

b=Button(f1,text="3",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="2",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="1",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


b=Button(f1,text="=",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


# opration frame of 3 button


f1=Frame(root,bg="grey")
f1.pack()

# b=Button(f1,text="/",font="lucida 20 bold",padx=10,pady=10)
# b.pack(side=LEFT,padx=5,pady=5)
# b.bind("<Button-1>",click)

b=Button(f1,text="/",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="0",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="*",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)






b=Button(f1,text="C",font="lucida 20 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)



root.mainloop()