import random
import tkinter as tk

window = tk.Tk()
window.title("Rock, paper, scissors game")
window.geometry("400x300-8-200")
window["padx"] = 20
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def choice_to_number(choice):
    rps = {"rock": 0, "paper": 1, "scissors": 2}
    return rps[choice]


def number_to_choice(number):
    rps = {0: "rock", 1: "paper", 2: "scissors"}
    return rps[number]


def random_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if user == comp:
        print("It's a tie !")
    elif (user-comp) % 3 == 1:
        print("You win.")
        USER_SCORE += 1
    else:
        print("Computer wins.")
        COMP_SCORE += 1
    text_area = tk.Text(master=window, height=20, width=40, bg="#FFFF99")
    text_area.grid(row=4, column=0)
    answer = "Your choice: {uc} \nComputer's choice: {cc}\nYour score: {us}\nComputer's score: {cs}\n".format(uc=USER_CHOICE, cc=COMP_CHOICE, us=USER_SCORE, cs=COMP_SCORE)
    text_area.insert(tk.END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "rock"
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "paper"
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "scissors"
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


button_1 = tk.Button(text="                 Rock", bg="skyblue", command=rock)
button_1.grid(row=1, column=0)
button_2 = tk.Button(text="                 Paper", bg="green", comman=paper)
button_2.grid(row=2, column=0)
button_3 = tk.Button(text="                 Scissors", bg="pink", command=scissors)
button_3.grid(row=3, column=0)

window.mainloop()
