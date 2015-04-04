# rock paper and scissor game
#  import the modules we need, for creating a GUI...
from tkinter import *
from tkinter import PhotoImage
import random


def computerRandom():
    options = ["Rock", "Paper", "Scissors"]
    randomChoice = random.randint(0, 2)
    computer_choice.set(options[randomChoice])  # added into the program
    return options[randomChoice]


def comparison(humanChoice, computerChoice):
    if humanChoice == computerChoice:
        return ("Draw")
    if humanChoice == "Rock" and computerChoice == "Paper":
        return ("Computer Wins")
    if humanChoice == "Paper" and computerChoice == "Scissors":
        return ("Computer Wins")
    if humanChoice == "Scissors" and computerChoice == "Rock":
        return ("Computer Wins")
    else:
        return ("Human Wins")


def play():

    humanChoice = player_choice.get()  # Modified this line
    computerChoice = computerRandom()
    result = comparison(humanChoice, computerChoice)

    if result == "Draw":
        result_set.set("Its a draw")
    elif result == "Computer Wins":
        result_set.set("Unlucky you lost!")
    else:
        result_set.set("Well done you won!")


# Setup of main GUI
root = Tk()
root.title('Rock Paper Scissors')
root.geometry("300x170+100+200")
image = PhotoImage(file=r"/home/kybrdbnd/Projects/mini_games/rock.png")
Label(root, image=image).pack(fill="both")
# Variables
player_choice = StringVar()
computer_choice = StringVar()
result_set = StringVar()
# player_choice.set("Rock")  ## Required to set player as "Rock" by default

# Layout of GUI
# Player
Label(root, text='Player',font=("",15)).place(x=10,y=5)
Radiobutton(root, text='Rock', variable=player_choice, value='Rock',font=("",12)).place(x=10,y=40)
Radiobutton(root, text='Paper', variable=player_choice, value='Paper',font=("",12)).place(x=10,y=80)
Radiobutton(root, text='Scissors', variable=player_choice,
            value='Scissors',font=("",12)).place(x=10,y=120)

# Computer
Label(root, text='Computer',font=("",15)).place(x=160,y=5)
Radiobutton(root, text='Rock', variable=computer_choice, value='Rock',font=("",12)).place(x=170,y=40)
Radiobutton(root, text='Paper', variable=computer_choice, value='Paper',font=("",12)).place(x=170,y=80)
Radiobutton(root, text='Scissors', variable=computer_choice,
            value='Scissors',font=("",12)).place(x=170,y=120)

# Play
Button(root, text="Play", command=play,font=("",10)).place(x=100,y=60)

# Result
Label(root, textvariable=result_set,font=("",10)).place(x=30,y=150)

root.mainloop()
