from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from time import sleep

# Initialiser la fenêtre
root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.configure(background='white')
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

# Variable pour le jeu (avec la grille)
player = 1
liste_win = ['X','O']
global board
board = [
    ['','',''],
    ['','',''],
    ['','','']
]
global board_win
board_win = []

# Creer la grille
def grid():
    # Liste qui contient tous les bouttons
    global button
    button = []
    # Variable qui permet de trouver le bouton dans la liste
    count = -1
    for i in range(3):
        for y in range(3):
            count += 1
            button.append(Button(
                root,
                bg='white',
                fg='white',
                height=6,
                width=10,
                font=('Helvetica 22'),
                command=lambda number=count, ipos=i, ypos=y: [changePlayer(1), change(number), setInGrid(ipos,ypos,number,board)]
            ))
            button[count].grid(row=i,column=y)

# Changement de tour
def changePlayer(num):
    global player
    player += num

# Mettre le bouton dans la grille board    
def setInGrid(i,y,number,board):
    board_win.append('Turn')

    # Verifier si la case est déjà utilisée
    if board[i][y] == '':
        if player % 2 == 0:
            board[i][y] = 'O'
        else:
            board[i][y] = 'X'
    # Si non, remettre les variables comman avant le coup
    else:
        messagebox.showerror('Erreur', 'La case est déjà utilisée')
        changePlayer(-1)
        if board[i][y] == 'O':
            board[i][y] = 'O'
            button[number].configure(text='O')
        else:
            board[i][y] = 'X'
            button[number].configure(text='X')
        board_win.pop()
    # Print le board      
    print(board)  
    print(board_win) 

    # Verifier si gagné
    if win():
        if player % 2 == 0:
            winner = 'O'
        else:
            winner = 'X'
        messagebox.showinfo('Bravo', '{} a gagné la partie'.format(winner))

        # Recommencer
        recommencer()

    elif tie():
        recommencer(True)

# Retourne True si gagné
def win():
    for elements in liste_win:
        # Lignes
        if board[0][0] == board[0][1] == board[0][2] == elements: return True
        if board[1][0] == board[1][1] == board[1][2] == elements: return True
        if board[2][0] == board[2][1] == board[2][2] == elements: return True
        
        # Colonnes
        if board[0][0] == board[1][0] == board[2][0] == elements: return True
        if board[0][1] == board[1][1] == board[2][1] == elements: return True
        if board[0][2] == board[1][2] == board[2][2] == elements: return True
        
        # Diagonales
        if board[0][0] == board[1][1] == board[2][2] == elements: return True
        if board[0][2] == board[1][1] == board[2][0] == elements: return True

# Egalité
def tie():
    if len(board_win) == 9:
        return True

# Reset board
def resetBoard():
    global board
    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

# Sur la fenêtre definir entre X ou O        
def change(number):
    if player % 2 == 0:
        button[number].configure(text='O')
    else:
        button[number].configure(text='X')

# Recommencer
def recommencer(egalite):
    if egalite:
        messagebox.showinfo('Egalité', 'Egalité')

    rep = messagebox.askyesno('Rejouer', 'Voulez vous rejouer ?')

    board = resetBoard()

    if rep:
        for child in root.winfo_children():
            child.destroy()
        start()
    # Quitter
    else:
        root.quit()

# Fonction start
def start():
    grid()
    global board_win
    board_win = []

# Commencer
if __name__ == '__main__':
    start()
    root.mainloop()