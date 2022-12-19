# Write your solution here
import random


class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2


class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def __count_vowels(self, word: str):
        vowels = 'aeiou'
        total_vowels = 0
        for letter in word:
            if letter in vowels:
                total_vowels += 1
        return total_vowels

    def round_winner(self, player1_word: str, player2_word: str):
        p1_vowels = self.__count_vowels(player1_word)
        p2_vowels = self.__count_vowels(player2_word)
        if p1_vowels > p2_vowels:
            return 1
        if p2_vowels > p1_vowels:
            return 2


class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def __get_wins(self, player_word: str, opponent_word: str):
        winners = (('rock', 'scissors'), ('paper', 'rock'),
                   ('scissors', 'paper'))
        wins = 0
        if (player_word, opponent_word) in winners:
            wins += 1
        return wins

    def round_winner(self, player1_word, player2_word):
        choices = ('rock', 'paper', 'scissors')
        if player2_word not in choices and player1_word in choices:
            return 1
        elif player1_word not in choices and player2_word in choices:
            return 2
        elif player1_word not in choices and player2_word not in choices:
            return

        p1_wins = self.__get_wins(player1_word, player2_word)
        p2_wins = self.__get_wins(player2_word, player1_word)
        if p1_wins > p2_wins:
            return 1
        elif p2_wins > p1_wins:
            return 2
