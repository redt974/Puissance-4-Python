import numpy as np

LIGNES = 6
COLONNES = 7

def create_board():
    return np.full((LIGNES, COLONNES), "_")

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == "_"

def get_next_open_row(board, col):
    for r in range(LIGNES-1, -1, -1):
        if board[r][col] == "_":
            return r

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLONNES-3):
        for r in range(LIGNES):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLONNES):
        for r in range(LIGNES-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLONNES-3):
        for r in range(LIGNES-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLONNES-3):
        for r in range(3, LIGNES):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def print_board(board):
    for row in board:
        print(" ".join(row))

def main():
    board = create_board()
    game_over = False
    turn = 0

    print("Joueur 1 : X")
    print("Joueur 2 : O")
    print_board(board)

    while not game_over:
        # Player 1 input
        if turn == 0:
            col = int(input("Joueur 1 : Choisissez une colonne (1-7): ")) - 1

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, "X")

                if winning_move(board, "X"):
                    print("Joueur 1 a gagné!")
                    game_over = True

        # Player 2 input
        else:
            col = int(input("Joueur 2 : Choisissez une colonne (1-7): ")) - 1

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, "O")

                if winning_move(board, "O"):
                    print("Joueur 2 a gagn2!")
                    game_over = True

        print_board(board)
        turn += 1
        turn %= 2  # Alternate between players

if __name__ == "__main__":
    main()
