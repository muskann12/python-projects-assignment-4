board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def play_game():
    current_player = "X"
    while True:
        print_board()
        move = input(f"Player {current_player}, choose position (1-9): ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please choose a number from 1 to 9.")
            continue

        move = int(move) - 1

        if board[move] != " ":
            print("That position is already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
