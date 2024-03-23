def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter your row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter your column (1-3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Row and column must be between 1 and 3.")
        except ValueError:
            print("Please enter a number.")

def play_game():
  #TO DO

if __name__ == "__main__":
    play_game()
