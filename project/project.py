winner_combination = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

sideA = []
sideB = []
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def display_board():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if i < 6:
            print("--+---+--")

def winner():
    for combination in winner_combination:
        if all(pos in sideA for pos in combination):
            return 1
        elif all(pos in sideB for pos in combination):
            return -1
    if "-" not in board:
        return 0
    return None

def gameover():
    return winner() is not None

def main():
    print("Welcome to Tic-Tac-Toe!")
    display_board()

    while True:
        # Side A's turn
        a = int(input("Side A (Enter position from 1 to 9): ")) - 1
        if a not in sideA and a not in sideB and 0 <= a <= 8:
            sideA.append(a)
            board[a] = 'X'
            display_board()
            if gameover():
                if winner() == 1:
                    print("Side A wins!")
                elif winner() == 0:
                    print("It's a draw!")
                break
        else:
            print("Position already taken or invalid. Try again.")
            continue

        # Side B's turn
        b = int(input("Side B (Enter position from 1 to 9): ")) - 1
        if b not in sideB and b not in sideA and 0 <= b <= 8:
            sideB.append(b)
            board[b] = 'O'
            display_board()
            if gameover():
                if winner() == -1:
                    print("Side B wins!")
                elif winner() == 0:
                    print("It's a draw!")
                break
        else:
            print("Position already taken or invalid. Try again.")
            continue

main()

