import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
from PIL import Image, ImageTk 

df = pd.read_csv("questions.csv")
questions = df.sample(n=20).values.tolist()

window = tk.Tk()
window.title("Python Quiz")
window.geometry("500x450")

background_color = "#abb0b0"
text_color = "#333333"
button_color = "#4CAF50"

window.config(bg=background_color)
window.option_add("*Font", "Arial 12")

image_original = Image.open("app_icon.png")
image_resized = image_original.resize((64, 64), Image.Resampling.LANCZOS)
app_icon = ImageTk.PhotoImage(image_resized)

app_label = tk.Label(window, image=app_icon, bg=background_color)
app_label.pack(pady=10, side="top") 

window.mainloop()

