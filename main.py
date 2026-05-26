import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
from PIL import Image, ImageTk 

df = pd.read_csv("data/questions.csv")

questions = df.sample(n=10).values.tolist()

score = 0
current_question = 0

def check_answer(answer):
  global score, current_question

  if answer == correct_answer.get():
    score += 1

  current_question += 1

  if current_question < len(questions):
    display_question()
  else:
    show_result()

def display_question():
  question, option1, option2, option3, option4, answer = questions[current_question]
  question_label.config(text=question)
  option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
  option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
  option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
  option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))

  correct_answer.set(answer)

def show_result():
  messagebox.showinfo("Quiz Result", f"Congratulations!\nYou completed the quiz.\n\n Your score: {score}/{len(questions)}")
  option1_btn.config(state=tk.DISABLED)
  option2_btn.config(state=tk.DISABLED)
  option3_btn.config(state=tk.DISABLED) 
  option4_btn.config(state=tk.DISABLED)

  play_again_btn.config(state=tk.NORMAL)
  play_again_btn.pack(pady=20)

def play_again():
  global score, current_question, questions
  score = 0
  current_question = 0
  
  questions = df.sample(n=10).values.tolist()
  
  option1_btn.config(state=tk.NORMAL)
  option2_btn.config(state=tk.NORMAL)
  option3_btn.config(state=tk.NORMAL)
  option4_btn.config(state=tk.NORMAL)

  play_again_btn.pack_forget()
  
  display_question()

window = tk.Tk()
window.title("Python Quiz")
window.geometry("500x450")

background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

window.config(bg=background_color)
window.option_add("*Font", "Arial 12")

image_original = Image.open("assets/app_icon.png")
image_resized = image_original.resize((64, 64), Image.Resampling.LANCZOS)
app_icon = ImageTk.PhotoImage(image_resized)

app_label = tk.Label(window, image=app_icon, bg=background_color)
app_label.pack(pady=10, side="top") 

question_label = tk.Label(window, text="", bg=background_color, fg=text_color, wraplength=400, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(window, text="Option 1", bg=button_color, fg=button_text_color, width=30, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(window, text="Option 2", bg=button_color, fg=button_text_color, width=30, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(window, text="Option 3", bg=button_color, fg=button_text_color, width=30, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(window, text="Option 4", bg=button_color, fg=button_text_color, width=30, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(window, command=play_again, text="Play Again", bg="#EEF085", fg=button_text_color, width=20, state=tk.DISABLED, font=("Arial", 10, "bold"))

display_question()

window.mainloop()

