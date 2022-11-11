def play_turn(game_board: list, x: int, y: int, piece: str):
    if (
        0 <= x <= 2 and
        0 <= y <= 2 and
        game_board[y][x] == ''
    ):
        game_board[y][x] = piece
        return True

    return False


if __name__ == "__main__":
    game_board = [['', 'O', 'X'], ['', 'X', 'X'], ['X', 'X', '']]
    print(play_turn(game_board, 0, 0, "X"))
    print(game_board)
