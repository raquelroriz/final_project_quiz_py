import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk


class QuizGame:
    def __init__(self, window):
        self.window = window

        self.bg_color = "#F5F7FA"
        self.text_color = "#2D3436"

        self.button_color = "#6C5CE7"
        self.button_text_color = "#FFFFFF"

        self.play_again_color = "#00B894"

        self.df = pd.read_csv("data/questions.csv")
        self.questions = self.df.sample(n=10).values.tolist()

        self.score = 0
        self.current_question = 0

        self.correct_answer = tk.IntVar()

        self.setup_ui()
        self.display_question()


    def setup_ui(self):
        self.window.title("Python Quiz Game")
        self.window.geometry("500x450")
        self.window.config(bg=self.bg_color)
        self.window.option_add("*Font", "Arial 12")

        try:
            image = Image.open("assets/app_icon.png")
            image = image.resize((64, 64))
            self.app_icon = ImageTk.PhotoImage(image)

            tk.Label(self.window, image=self.app_icon, bg=self.bg_color).pack(pady=10)

        except:
            pass

        self.question_label = tk.Label(
            self.window,
            text="",
            bg=self.bg_color,
            fg=self.text_color,
            wraplength=400,
            font=("Arial", 12, "bold")
        )
        self.question_label.pack(pady=20)

        button_style = {
            "bg": self.button_color,
            "fg": self.button_text_color,
            "width": 30,
            "font": ("Arial", 10, "bold"),
            "bd": 0,
            "relief": "flat",
            "cursor": "hand2"
        }


        self.option1_btn = tk.Button(self.window, text="Option 1",
                                     command=lambda: self.check_answer(1),
                                     **button_style)
        self.option1_btn.pack(pady=8)

        self.option2_btn = tk.Button(self.window, text="Option 2",
                                     command=lambda: self.check_answer(2),
                                     **button_style)
        self.option2_btn.pack(pady=8)

        self.option3_btn = tk.Button(self.window, text="Option 3",
                                     command=lambda: self.check_answer(3),
                                     **button_style)
        self.option3_btn.pack(pady=8)

        self.option4_btn = tk.Button(self.window, text="Option 4",
                                     command=lambda: self.check_answer(4),
                                     **button_style)
        self.option4_btn.pack(pady=8)

        self.play_again_btn = tk.Button(
            self.window,
            text="Play Again",
            command=self.play_again,
            bg=self.play_again_color,
            fg="white",
            width=20,
            font=("Arial", 10, "bold"),
            state=tk.DISABLED,
            bd=0,
            relief="flat",
            cursor="hand2"
        )


    def display_question(self):
        q, o1, o2, o3, o4, answer = self.questions[self.current_question]

        self.question_label.config(text=q)

        self.option1_btn.config(text=o1, state=tk.NORMAL)
        self.option2_btn.config(text=o2, state=tk.NORMAL)
        self.option3_btn.config(text=o3, state=tk.NORMAL)
        self.option4_btn.config(text=o4, state=tk.NORMAL)

        self.correct_answer.set(answer)

    def check_answer(self, answer):
        if answer == self.correct_answer.get():
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo(
            "Quiz Result",
            f"You finished the quiz!\n\nScore: {self.score}/{len(self.questions)}"
        )

        self.option1_btn.config(state=tk.DISABLED)
        self.option2_btn.config(state=tk.DISABLED)
        self.option3_btn.config(state=tk.DISABLED)
        self.option4_btn.config(state=tk.DISABLED)

        self.play_again_btn.config(state=tk.NORMAL)
        self.play_again_btn.pack(pady=20)

    def play_again(self):
        self.score = 0
        self.current_question = 0

        self.questions = self.df.sample(n=10).values.tolist()

        self.play_again_btn.pack_forget()

        self.display_question()


if __name__ == "__main__":
    window = tk.Tk()
    app = QuizGame(window)
    window.mainloop()
