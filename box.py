# box game

# import the modules we need, for creating a GUI...

import tkinter as tk
from tkinter import messagebox as messagebox


board = [[None] * 10 for _ in range(10)]

counter = 0
root = tk.Tk()
root.geometry("275x250+100+300")
root.title("Box Game")

# method for drawing the game
def check_board():
    freespaces = 0
    redspaces = 0
    greenspaces = 0
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] == "red":
                redspaces += 1
            elif board[i][j] == "green":
                greenspaces += 1
            elif board[i][j] == None:
                freespaces += 1

    if freespaces == 0:
        if greenspaces > redspaces:
            winner = "green"
        elif greenspaces < redspaces:
            winner = "red"
        else:
            winner = "draw"

        if winner != "draw":
            messagebox.showinfo("Game Over!", winner + " wins!")
        else:
            messagebox.showinfo("Game Over!", "The game was a draw!")


# method to color the particular box
def on_click(i, j, event):
    global counter
    if counter < 100:
        if board[i][j] == None:
            color = "green" if counter % 2 else "red"
            enemycolor = "red" if counter % 2 else "green"
            event.widget.config(bg=color)
            board[i][j] = color
            for k in range(-1, 2):
                for l in range(-1, 2):
                    try:
                        if board[i + k][j + l] == enemycolor:
                            board[i + k][j + l] = color
                    except IndexError:
                        pass
            counter += 1
            global gameframe
            gameframe.destroy()
            redraw()
            root.wm_title(enemycolor + "'s turn")
        else:
            messagebox.showinfo("Alert", "This square is already occupied!")
        check_board()

# call the main game everytime after one_click method
def redraw():
    global gameframe
    gameframe = tk.Frame(root)
    gameframe.pack()

    for i, row in enumerate(board):

        for j, column in enumerate(row):
            name = str(i) + str(j)
            L = tk.Label(gameframe, text='    ',
                         bg="grey" if board[i][j] == None else board[i][j])
            L.grid(row=i, column=j, padx='3', pady='3')
            L.bind('<Button-1>', lambda e, i=i, j=j: on_click(i, j, e))


redraw()
root.mainloop()
