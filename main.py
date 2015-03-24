#  import the modules we need, for creating a GUI...
from tkinter import Tk, Label, Menu, Button, PhotoImage
# module for running system files
import os

# all methods/functions
def box():
    os.system("python3 box.py")
    return


def snake():
    os.system("python3 snake1.py")
    return


def color():
    os.system("python3 color.py")
    return


def mastermind():
    os.system("python3 mastermind.py")
    return


def rock():
    os.system("python3 rock.py")
    return

def guide():
    mguide = Tk() # object of Tkinter for guide panel
    # creation of Guide GUI
    mguide.geometry("520x600+50+100")
    mguide.title("Guide for Games")
    boxlabel = Label(mguide,text="Box Game",font=("",15)).place(x=10,y=5)
    boxlabelc = Label(mguide,text="Box Game is a simple yet an interesting game."\
                      "In this game when you click on \nthe box the adjacent box/boxes get filled by your colour."\
                     " The player who has the \nhiggest number of"\
                     " colored boxes of its own wins the game.",justify="left").place(x=10,y=40) 
    snakelabel = Label(mguide,text="Snake Game",font=("",15)).place(x=10,y=100)
    snakelabelc = Label(mguide,text="It is the traditional snake game. The snake gets longer"\
                        " and longer by eating\nfruit and dies when he eats himself or"\
                         " touches the wall.",justify="left").place(x=10, y=130) 
    colorlabel = Label(mguide, text= "Colour Game",font=("",15)).place(x=10,y=190)
    colorlabelc = Label(mguide,text="It is a simple game in which you have to type in the colour of the words"\
                        ",\nand not the word text!",justify="left").place(x=10,y=225)
    mastermindlabel = Label(mguide,text="Mastermind Game",font=("",15)).place(x=10,y=285)
    mastermindlabelc = Label(mguide,text="It's a pencil and paper game played by two players."\
                             "The two players write a\n4-digit number on a sheet of paper. The digits"\
                             "must be all different, but there\nis a version, where digits can be used"\
                             "more than once. Each player has to find\nout the opponent's secret code."\
                             "To this purpose, the players - in turn - try to\nguess the opponent's number."\
                             " The opponent has to score the guess: A 'bull'\nis a digit which is located"\
                             " at the right position. If for example the hidden code\nis '4 3 2 5' and the"\
                             " guess is '4 3 1 2', then we have the two bulls '4' and '3' in\nthe guess"\
                             " '4 3 1 2'. A 'Cow' on the other hand is a correct number, which is on\nthe"\
                             " wrong position. The '2' of the previous example is a cow.\nMastermind obeys"\
                             " essentially the same rules as 'Bulls and Cows', \nbut colours are used"\
                             " instead of digits.",justify="left").place(x=10,y=315)
    rocklabel = Label(mguide,text="Rock Paper & Scissor Game",font=("",15)).place(x=10,y=500)
    rocklabelc = Label(mguide,text="You haven't enjoyed your childhood, go ask your friend",justify="left").place(x=10,y=530)
    
    return

def about():
    ab = Tk() #object of tkinter for About Panel
    # Creation of About GUI Panel
    ab.title("About")
    ab.geometry("300x150+200+100")
    Label(ab,text="Developed By:",font=("",12)).pack(padx=30,pady=20)
    Label(ab,text="Pranav Puri(kybrdbnd)",font=("",12)).pack()
    Label(ab,text="Contact No: +91 8860270019",font=("",12)).pack()
    return

# Main Gui
mGui = Tk() # object of Tkinter for Main Panel
# Creation og Main GUI Panel
mGui.geometry("500x350+400+200")
mGui.title("Mini Games for Python")
image = PhotoImage(file=r"/home/kybrdbnd/Projects/python_games/main.png")
Label(mGui, image=image).pack()
menubar = Menu(mGui)
helpmenu = Menu(menubar)
helpmenu.add_command(label="Guide!!!",command=guide)
helpmenu.add_command(label="About",command=about)
# optionmenu.add_command(label="EXIT", command=exit)
menubar.add_cascade(label="Help", menu=helpmenu)
mGui.config(menu=menubar)

mlabel = Label(mGui, text="Let's Play", font=("", 20),
               bg="white", fg="#f80052").place(x=10, y=10)
mexit = Button(mGui, text="Quit", command=exit, bg="white").place(x=440, y=10)
mbox = Button(mGui, text="BOX Game", command=box,
              bg="white", fg="#f80052").place(x=80, y=80)
msnake = Button(mGui, text="Snake Game", command=snake,
                bg="white", fg="#f80052").place(x=300, y=80)
mcolor = Button(mGui, text="Color Game", command=color,
                bg="white", fg="#f80052").place(x=80, y=160)
mcolor = Button(mGui, text="Mastermind", command=mastermind,
                bg="white", fg="#f80052").place(x=300, y=160)
mcolor = Button(mGui, text="Rock Paper and Scissor", command=rock,
                bg="white", fg="#f80052").place(x=160, y=235)


mGui.mainloop()
