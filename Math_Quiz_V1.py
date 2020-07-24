from tkinter import *
from functools import partial
import random


class Start:
    def __init__(self, parent):

        background_color = "#78ffd1"

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.help_frame = Frame(pady=10, padx=10)
        self.help_frame.grid()

        self.number_questions = IntVar()
        self.number_questions.set(0)

        self.numbers_used_low = IntVar()
        self.numbers_used_low.set(0)

        self.numbers_used_high = IntVar()
        self.numbers_used_high.set(0)

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
                                            wrap=275, justify=LEFT,
                                            padx=10, pady=10,)
        self.math_instructions.grid(row=1)

        self.question_frame = Frame(self.start_frame, width=10)
        self.question_frame.grid(row=2)

        self.entry_frame = Frame(self.start_frame, width=5)
        self.entry_frame.grid(row=3)

        self.add_questions_button = Label(self.question_frame,
                                       font="Arial 15 bold",
                                       text="Set Amount of Questions")
        self.add_questions_button.grid(row=0, column=0)

        # Number of questions
        self.start_amount_entry = Entry(self.question_frame,
                                        font="Arial 19 bold", width=10,)
        self.start_amount_entry.grid(row=0, column=1)

        self.amount_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="Use numbers between")
        self.numbers_between_button.grid(row=2, column=0)

        # Low number entry box
        self.numbers_used_entry_low = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.numbers_used_entry_low.grid(row=2, column=1, padx=20)

        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="and")
        self.numbers_between_button.grid(row=2, column=2)

        # high number entry box
        self.numbers_used_entry_high = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.numbers_used_entry_high.grid(row=2, column=3, padx=20)

        self.numbers_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275, justify=LEFT)
        self.numbers_error_label.grid(row=3, columnspan=2, pady=5)

        # button frame (row 3)
        self.question_type_frame = Frame(self.start_frame)
        self.question_type_frame.grid(row=4)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Blue Multiplication question_type button
        self.multiplication_button = Button(self.question_type_frame, text="Multiplication",
                                       command=lambda: self.to_quiz("*"),
                                       font=button_font, bg="#1170ed")
        self.multiplication_button.grid(row=0, column=0, pady=10)

        # Yellow Subtraction question_type button
        self.subtraction_button = Button(self.question_type_frame, text="Subtraction",
                                       command=lambda: self.to_quiz("-"),
                                       font=button_font, bg="#FFFF33")
        self.subtraction_button.grid(row=0, column=1, pady=10)

        # Green Addition question_type button
        self.addition_button = Button(self.question_type_frame, text="Addition",
                                       command=lambda: self.to_quiz("+"),
                                       font=button_font, bg="#99FF33")
        self.addition_button.grid(row=0, column=2, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=1, pady=10)

    def to_quiz(self, question_type):
        # Number checking function
        question_amount = self.start_amount_entry.get()

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        try:
            question_amount = int(question_amount)

            if question_amount <= 0:
                has_errors = "yes"
                error_feedback = "Sorry, the smallest amount of " \
                                 "questions you can play with is 1"
            elif question_amount > 50:
                has_errors = "yes"
                error_feedback = "You cannot play with more than 50 " \
                                 "Questions!"

            elif question_amount >= 1:
                self.number_questions.set(question_amount)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:

            numbers_used_low = self.numbers_used_entry_low.get()

            error_back = "#ffafaf"
            has_errors = "no"

            self.start_amount_entry.config(bg="white")
            self.amount_error_label.config(text="")

            try:
                numbers_used_low = int(numbers_used_low)

                if numbers_used_low <= 0:
                    has_errors = "yes"
                    error_feedback = "Sorry, the smallest amount of " \
                                     "questions you can play with is 1"
                elif numbers_used_low > 50:
                    has_errors = "yes"
                    error_feedback = "You cannot play with more than 50 " \
                                     "Questions!"

                elif numbers_used_low >= 1:
                    self.numbers_used_low.set(numbers_used_low)

            except ValueError:
                has_errors = "yes"
                error_feedback = "Please enter a whole number(no text / decimals)"

            if has_errors == "yes":
                self.start_amount_entry.config(bg=error_back)
                self.amount_error_label.config(text=error_feedback)

            else:

                numbers_used_high = self.numbers_used_entry_high.get()

                error_back = "#ffafaf"
                has_errors = "no"

                self.start_amount_entry.config(bg="white")
                self.amount_error_label.config(text="")

                try:
                    numbers_used_high = int(numbers_used_high)

                    if numbers_used_high <= 0:
                        has_errors = "yes"
                        error_feedback = "Sorry, the smallest amount of " \
                                         "questions you can play with is 1"
                    elif numbers_used_high > 50:
                        has_errors = "yes"
                        error_feedback = "You cannot play with more than 50 " \
                                         "Questions!"

                    elif numbers_used_high >= 1:
                        self.numbers_used_high.set(numbers_used_high)

                except ValueError:
                    has_errors = "yes"
                    error_feedback = "Please enter a whole number(no text / decimals)"

                if has_errors == "yes":
                    self.start_amount_entry.config(bg=error_back)
                    self.amount_error_label.config(text=error_feedback)

                else:

                    # code for starting game:
                    self.number_questions.set(question_amount)

                    question_amount = self.number_questions.get()
                    numbers_used_low = self.numbers_used_low.get()
                    numbers_used_high = self.numbers_used_high.get()

                    Quiz(self, question_type, question_amount, numbers_used_high, numbers_used_low)

        # hide start up menu disabled for testing purposes
        root.withdraw()

    def to_help(self):
        get_help = Help(self)


class Quiz:
    def __init__(self, partner, question_type, question_amount, numbers_used_low,
                 numbers_used_high):
        print(question_type)
        print(question_amount)
        print(numbers_used_low)
        print(numbers_used_high)

        # GUI Setup
        self.quiz_box = Toplevel()

        # So user can quit with x in top corner
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # Frame for main quiz functions
        self.quiz_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.quiz_frame.grid()

        # Frame for help button
        self.help_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.help_frame.grid()

        # Frame for the quit button
        self.quit_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.quit_frame.grid()

        # Top heading
        self.math_quiz_label = Label(self.quiz_frame,
                                          text="Play",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        # Instructions for user
        self.math_instructions = Label(self.quiz_frame, font="Arial 10 italic",
                                       text="Please enter the answer of the"
                                            "question below. Then click on "
                                            "the submit button to continue "
                                            "to the next question. ",
                                            wrap=275, justify=LEFT,
                                            padx=10, pady=10,)
        self.math_instructions.grid(row=1)

        # question number
        self.question_number_label = Label(self.quiz_frame,
                                          text="Question 3",
                                          font=("Arial", "12", "bold"),
                                          padx=10, pady=10)
        self.question_number_label.grid(row=2)

        self.questions_label = Label(self.quiz_frame,
                                       font="Arial 15 bold",
                                       text="Set Amount of Questions")
        self.questions_label.grid(row=3, column=0)

        # entry box for answers
        self.question_answer_entry = Entry(self.quiz_frame,
                                        font="Arial 19 bold", width=5)
        self.question_answer_entry.grid(row=3, column=1, padx=15)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Orange Multiplication question_type button
        self.multiplication_button = Button(self.quiz_frame, text="Submit",
                                            command=lambda: self.to_questions,
                                            font=button_font, bg="#4ee6ab")
        self.multiplication_button.grid(row=4, column=0, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       bg="#808080", fg="white",
                                       font="Arial 15 bold",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=1, pady=5)

        # Quit button
        self.quit_button = Button(self.quit_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold",
                                  command=self.to_quit, padx=10, pady=5)
        self.quit_button.grid(row=6, pady=10)

    def to_questions(self, question_amount):
        question_amount = 5

        numbers_used_low = 1
        numbers_used_high = 8
        operator = "*"
        display_op = "×"

        for item in range(0, question_amount):
            # generate question
            num_1 = random.randint(numbers_used_low, numbers_used_high)
            num_2 = random.randint(numbers_used_low, numbers_used_high)

            question = "{} {} {}".format(num_1, operator, num_2)
            display_question = "{} {} {} = ".format(num_1, display_op, num_2)
            answer = eval(question)

            print("{} {}".format(display_question, answer))

    # setting up for the help button
    def to_help(self):
        get_help = Help(self)

    # so the quit button functions correctly
    def to_quit(self):
        root.destroy()


class Help:
    def __init__(self, partner):
        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and "releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up help GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Help!"
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss Button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()