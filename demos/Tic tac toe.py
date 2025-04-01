import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print("Current Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    current_player = "X"
    while True:
        print_board(board)
        
        # Get user input
        try:
            row = int(input(f"Player {current_player}, enter your move row (0-2): "))
            col = int(input(f"Player {current_player}, enter your move column (0-2): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        
        # Place the move on the board
        board[row][col] = current_player
        
        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()