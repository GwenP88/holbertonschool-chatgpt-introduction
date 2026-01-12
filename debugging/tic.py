#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board):
    # Rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    # Columns
    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def read_position(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Out of range. Row and column must be 0, 1, or 2.")
            continue

        return row, col

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = read_position(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # Check win BEFORE switching player
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
