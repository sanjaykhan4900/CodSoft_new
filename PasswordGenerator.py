from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random
# import MySQLdb as mdb
# import mysql.connector

root=Tk()

def generate_password():
    try:
        length_password=ps.get()
        small_letters=string.ascii_lowercase
        capital_letters=string.ascii_uppercase
        digits=string.digits
        special_character=string.punctuation
        all_list=[]
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel("A problem has been Occured","please try again")

def save_user():
    print("accepted")


root.resizable(False,False)
all_no={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10",
        "11":"11","12":"12","13":"13","14":"14","15":"15","16":"16","17":"17",}
root.geometry("500x500")
root.title("Sanjay password generator")
root.config(bg="beige")
title=Label(root,text="PASSWORD GENERATOR BY SANJAY",bg="beige",fg="black",font=("futura",15,"bold"))
title.pack(pady="10px")
length=Label(root,text="Enter UserName :-" ,bg="beige",fg="darkgreen",font=("ubuntu" ,12))
length.place(x="30px",y="40px")
Username=StringVar()
name=Entry(root,textvariable=Username,font=("ubuntu",12))
name.place(x="210px",y="40px")


length=Label(root,text="Enter Length of Your Password :-" ,bg="beige",fg="darkgreen",font=("ubuntu" ,12))
length.place(x="30px",y="70px")

ps=IntVar()
selector=Combobox(root,textvariable=ps,state="readonly")
selector.place(x="210px",y="70px")
selector['values']=[i for i in all_no.keys()]

def on_enter(self):
    button['bg']="grey"
    button['fg']="white"
def on_leave(self):
    button['bg']="orange"
    button['fg']="black"

button=Button(root,text="Generate Password", bg="blue",fg="white",font=("ubuntu",15),cursor="hand2",command=generate_password)
button.pack(anchor="center",pady="70px")
button.bind("<Enter>",on_enter)
button.bind("<Leave>",on_leave)

button1=Button(root,text="SUBMIT", bg="blue",fg="white",font=("ubuntu",15),command=save_user)
button1.place(x="150px",y="220px")

button2=Button(root,text="RESET", bg="blue",fg="white",font=("ubuntu",15))
button2.place(x="150px",y="270px")

result=Label(root,text="Generated Password:-",bg="beige",fg="darkgreen",font=("ubuntu", 12))
result.place(y="170px",x="30px")

password=StringVar()
final_result=Entry(root,textvariable=password,state="readonly",font=("ubuntu",15))
final_result.place(x="190px",y="170px")

root.mainloop()