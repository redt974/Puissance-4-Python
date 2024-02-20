import numpy as np
import tkinter as tk
from tkinter import messagebox

LIGNES = 6
COLONNES = 7
CELL_SIZE = 80
RADIUS = CELL_SIZE // 2 - 5
OFFSET = 50

class Puissance4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Puissance 4")
        self.canvas = tk.Canvas(self.root, width=COLONNES*CELL_SIZE, height=LIGNES*CELL_SIZE + OFFSET)
        self.canvas.pack()
        self.board = np.zeros((LIGNES, COLONNES))
        self.turn = 0  # 0 for Player 1, 1 for Player 2
        self.draw_board()
        self.canvas.bind("<Button-1>", self.drop_piece)
        self.game_over = False
        self.root.mainloop()

    def draw_board(self):
        for c in range(COLONNES):
            for r in range(LIGNES):
                self.canvas.create_rectangle(c*CELL_SIZE, r*CELL_SIZE + OFFSET, (c+1)*CELL_SIZE, (r+1)*CELL_SIZE + OFFSET, fill="blue", outline="blue")
                self.canvas.create_oval(c*CELL_SIZE + 5, r*CELL_SIZE + OFFSET + 5, (c+1)*CELL_SIZE - 5, (r+1)*CELL_SIZE + OFFSET - 5, fill="white", outline="white")

    def drop_piece(self, event):
        if not self.game_over:
            x = event.x
            col = x // CELL_SIZE
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.drop_piece_on_board(row, col)
                if self.winning_move():
                    messagebox.showinfo("Victoire", f"Le joueur {self.turn + 1} a gagné !")
                    self.game_over = True
                self.turn += 1
                self.turn %= 2

    def is_valid_location(self, col):
        return self.board[0][col] == 0

    def get_next_open_row(self, col):
        for r in range(LIGNES-1, -1, -1):
            if self.board[r][col] == 0:
                return r

    def drop_piece_on_board(self, row, col):
        piece = self.turn + 1
        self.board[row][col] = piece
        color = "red" if piece == 1 else "yellow"
        self.canvas.create_oval(col*CELL_SIZE + 5, row*CELL_SIZE + OFFSET + 5, (col+1)*CELL_SIZE - 5, (row+1)*CELL_SIZE + OFFSET - 5, fill=color)
        self.root.update()

    def winning_move(self):
        # Check horizontal locations
        for c in range(COLONNES-3):
            for r in range(LIGNES):
                if self.board[r][c] == self.turn + 1 and self.board[r][c+1] == self.turn + 1 and self.board[r][c+2] == self.turn + 1 and self.board[r][c+3] == self.turn + 1:
                    return True

        # Check vertical locations
        for c in range(COLONNES):
            for r in range(LIGNES-3):
                if self.board[r][c] == self.turn + 1 and self.board[r+1][c] == self.turn + 1 and self.board[r+2][c] == self.turn + 1 and self.board[r+3][c] == self.turn + 1:
                    return True

        # Check positively sloped diagonals
        for c in range(COLONNES-3):
            for r in range(LIGNES-3):
                if self.board[r][c] == self.turn + 1 and self.board[r+1][c+1] == self.turn + 1 and self.board[r+2][c+2] == self.turn + 1 and self.board[r+3][c+3] == self.turn + 1:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLONNES-3):
            for r in range(3, LIGNES):
                if self.board[r][c] == self.turn + 1 and self.board[r-1][c+1] == self.turn + 1 and self.board[r-2][c+2] == self.turn + 1 and self.board[r-3][c+3] == self.turn + 1:
                    return True

        return False

if __name__ == "__main__":
    Puissance4()
