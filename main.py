def print_board(board):
    for row in board:
        print(" | ".join(row))
        if row < len(board):
            print("---------")


def check_winner(board, player):
    return 0


def is_board_full(board):
    return 0


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Welcome to Tic Tac Toe!\n")

    print_board(board)


if __name__ == '__main__':
    main()

