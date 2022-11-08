# Write your solution here
def who_won(board_game: list):
    player1 = 0
    player2 = 0

    for row in board_game:
        for piece in row:
            if piece == 1:
                player1 += 1
            elif piece == 2:
                player2 += 1

    if player1 == player2:
        return 0
    elif player1 > player2:
        return 1
    else:
        return 2


if __name__ == "__main":
    go_list = [
        [2, 0, 0, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 1, 2, 0, 2, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 2, 2, 0],
        [2, 0, 2, 0, 2, 0, 1, 0, 0],
        [0, 0, 1, 2, 0, 1, 2, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(who_won(go_list))
