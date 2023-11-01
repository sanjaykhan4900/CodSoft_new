from tkinter import *
import tkinter as tk
from tkinter import filedialog

class todo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400",)
        self.title("to-do-list-By-Sanjay")
        self.create()
        # self.mainloop()

    def create(self):
        self.input=tk.Entry(self,width=30,bg="skyblue",font="20")
        self.input.pack(pady=40)

        self.add_button=tk.Button(self,text="Add task",command=self.add_task,bg="green",fg="white",font="bold")
        self.add_button.pack(pady=5)

        self.listbox=tk.Listbox(self,selectmode=tk.SINGLE,bg="skyblue")
        self.listbox.pack(pady=5)

        self.button_frame=tk.Frame(self)
        self.button_frame.pack(pady=5)

        self.edit_button=tk.Button(self.button_frame,text="Edit Task",command=self.edit_task,bg="green",fg="white",font="bold")
        self.edit_button.grid(row=0,column=0,padx=5)

        self.delete_button=tk.Button(self.button_frame,text="Delete Task",command=self.delete_task,bg="green",fg="white",font="bold")
        self.delete_button.grid(row=0,column=1,padx=5)


    def add_task(self):
        task=self.input.get()
        if task:
            self.listbox.insert(tk.END,task)
            self.input.delete(0,tk.END)

    def edit_task(self):
        task_index=self.listbox.curselection()
        if task_index:
            new_task=self.input.get()
            if new_task:
                self.listbox.delete(task_index)
                self.listbox.insert(task_index,new_task)
                self.input.delete(0,tk.End)
    def delete_task(self):
        task_index=self.listbox.curselection()
        if task_index:
            self.listbox.delete(task_index)


