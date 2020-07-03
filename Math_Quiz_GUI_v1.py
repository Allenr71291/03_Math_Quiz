from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.math_quiz_label = Label(self.start_frame,
                                          text="Math Quiz",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        self.math_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter the number of "
                                          "questions you would like to "
                                          "answer in the box below. Keep "
                                          "in mind that you cant have less "
                                          "than 0 questions!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_instructions.grid(row=1)

        self.question_amount = Entry(self.start_frame, font="Arial 16 bold")
        self.question_amount.grid(row=2)

        # Entry box (row 2)
        self.question_amount = Entry(self.start_frame, font="Arial 19 bold")
        self.question_amount.grid(row=2)

        # button frame (row 3)
        self.question_frame = Frame(self.start_frame)
        self.question_frame.grid(row=3)

        # Buttons here:
        button_font = "arial 12 bold"

        # Orange low stakes button
        self.Subtraction_button = Button(self.question_frame, text="Subtraction",
                                       command=lambda: self.to_quiz("-"),
                                       font=button_font, bg="#FF9933")
        self.Subtraction_button.grid(row=0, column=0, pady=10)

        #yellow medium stakes button
        self.Addition_button = Button(self.question_frame, text="Addition",
                                       command=lambda: self.to_quiz("+"),
                                       font=button_font, bg="#FFFF33")
        self.Addition_button.grid(row=0, column=1, pady=10)

        self.Multiplication_button = Button(self.question_frame, text="Multiplication",
                                       command=lambda: self.to_quiz("*"),
                                       font=button_font, bg="#99FF33")
        self.Multiplication_button.grid(row=0, column=2, pady=10)

        self.help_button = Button(self.question_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white")
        self.help_button.grid(row=1, column=1, pady=10)

    def to_quiz(self, stakes):
        starting_balance = self.question_amount.get()
        Quiz(self, stakes, starting_balance)


class Quiz:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()