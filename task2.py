import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[j][i] == player for j in range(3)) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row number (0-2): "))
            col = int(input(f"Player {player}, enter column number (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                return
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def computer_move(board, player):
    empty_cells = get_empty_cells(board)
    row, col = random.choice(empty_cells)
    board[row][col] = player

def play_tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]

    print_board(board)

    players = ["X", "O"]
    current_player_idx = random.randint(0, 1)

    while True:
        current_player = players[current_player_idx]
        if current_player == "X":
            player_move(board, current_player)
        else:
            computer_move(board, current_player)

        print_board(board)

        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player_idx = (current_player_idx + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()
