from random import choice


def roll(die: str):
    if die == 'A':
        return int(choice('333336'))
    elif die == 'B':
        return int(choice('222555'))
    elif die == 'C':
        return int(choice('144444'))


def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(times):
        if roll(die1) == roll(die2):
            ties += 1
        elif roll(die1) > roll(die2):
            die1_wins += 1
        else:
            die2_wins += 1

    return die1_wins, die2_wins, ties


if __name__ == '__main__':
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
