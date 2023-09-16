from tkinter import *

Questions = ["MS-Word is an example of ______. ",
             "Ctrl, Shift and Alt are called _____keys.",
             "Junk e-mail is also called ______."]
Options = [["input device", "operating system", "application software"],
           ["function", "modifier", "adjustment"],
           ["spoof", "spool", "spam"]]

Answers = [3, 2, 3]

Score = 0
Total_No_Questions = 3
Question_no = 1
def start_again():
    global Score,Question_no
    
    Score = 0
    Question_no = 1
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=Questions[Question_no-1])
    option1.config(text=Options[Question_no-1][0])
    option2.config(text=Options[Question_no-1][1])
    option3.config(text=Options[Question_no-1][2])
    next_b.config(text="next")
    play_again.place_forget()
    score.place_forget()
    root.pack()
def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[Question_no-1] == selected_option :
        Score += 1

    Question_no += 1

    if Question_no > Total_No_Questions:
        root.pack_forget()
        score.place(relx=.5, rely=.5,anchor=CENTER)
        play_again.place(relx=.45, rely=.1)
        
        score.config(text="Score:"+str(Score), font=("Arial", 15))

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def start_game():
    user_screen.place_forget()
    root.pack()


Win = Tk()
Win.geometry("900x600")
Win.title("Quiz Game")

user_screen = Frame()
user_screen.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_message = Label(user_screen, width=60, font=("Arial", 15), text="Welcome to our Quiz Game")
intro_message.pack()
play_b = Button(user_screen, text="Play Game", command=start_game)
play_b.pack()

root = Frame(Win)
root.pack_forget()

question = Label(root, width=60, font=("Arial", 15), text=Questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1, text=Options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=Options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=Options[0][2], command=lambda: check(3))
option3.pack()

next_b = Button(root, text="next", command=next)
next_b.pack()

score = Label(Win)
score.place_forget()

play_again = Button(Win,text= "Play Again",command=start_again)
play_again.place_forget()

Win.mainloop()
