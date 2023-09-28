def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * len(board[0] * 3))


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Welcome to Tic Tac Toe!\n")

    while True:
        print_board(board)

        row = int(input(f"\nPlayer {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
        print(" ")

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("The position is not available.\n")
            continue

        if check_winner(board, current_player):
            winner = current_player
            break

        if is_board_full(board):
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


if __name__ == '__main__':
    main()

