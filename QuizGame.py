
from tkinter import *
from tkinter import messagebox as mbox
import json
class Quiz:

	def __init__(self):
		self.q_no=0
		self.display_title()
		self.display_question()
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_options()
		self.buttons()
		self.data_size=len(question)
		self.correct=0

	def check_ans(self, q_no):
		if self.opt_selected.get() == answer[q_no]:
			return True

	def display_result(self):
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		mbox.showinfo("Result", f"{result}\n{correct}\n{wrong}")



	def next_btn(self):
		if self.check_ans(self.q_no):
			self.correct += 1
		self.q_no += 1
		if self.q_no==self.data_size:
			self.display_result()
			tk.destroy()
		else:
			self.display_question()
			self.display_options()

	def buttons(self):
		next_button = Button(tk, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",15,"bold"))
		next_button.place(x=340,y=370)
		quit_button = Button(tk, text="Quit", command=tk.destroy,
		width=5,bg="black", fg="white",font=("ariel",15," bold"))
		quit_button.place(x=710,y=55)

	def display_options(self):
		val=0
		self.opt_selected.set(0)
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1

	def display_question(self):
		q_no = Label(tk, text=question[self.q_no], width=62,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		q_no.place(x=71, y=101)

	def display_title(self):
		title = Label(tk, text="Quiz Game By Sanjay",
		width=50, bg="blue",fg="white", font=("ariel", 18, "bold"))
		title.place(x=0, y=2)

	def radio_buttons(self):
		question_list = []
		y_pos = 155
		while len(question_list) < 4:
			radio_btn = Radiobutton(tk,text=" ",variable=self.opt_selected,
			value = len(question_list)+1,font = ("ariel",14))
			question_list.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 50
		return question_list

tk = Tk()
tk.geometry("790x500")
tk.title("Quiz Game By Sanjay")
with open('questions.json') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
quiz = Quiz()
tk.mainloop()

