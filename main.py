import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_csv("questions.csv")
questions = df.sample(n=20).values.tolist()

window = tk.Tk()
window.title("Python Quiz")
window.geometry("400x450")

background_color = "#abb0b0"
text_color = "#333333"
button_color = "#4CAF50"

window.config(bg=background_color)
window.option_add("*Font", "Arial 12")

window.mainloop()

