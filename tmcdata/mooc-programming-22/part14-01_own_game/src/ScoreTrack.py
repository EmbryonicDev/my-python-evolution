class Player:
    def __init__(self, name: str):
        self.name = name
        self.points = 0
        self.level = 0

    def add_point(self):
        self.points += 1

    def add_point(self):
        self.level += 1


class HighScores:
    def __init__(self):
        self.top_ten_scores = []

    def update_scores(self, Player):
        if self.file_exists():
            self.text_to_list()

        if len(self.top_ten_scores) == 10:
            if Player.points > self.top_ten_scores[9].points:
                self.top_ten_scores.pop(9)

        self.top_ten_scores.append(Player)
        self.sort_scores()
        self.list_to_text()
        print(self.top_ten_scores)

    def sort_scores(self):
        self.top_ten_scores = sorted(
            self.top_ten_scores, key=lambda x: x.points, reverse=True)

    def file_exists(self):
        file = 'scores.txt'
        try:
            f = open(file, 'r')
            print("File Exists")
            return True
        except IOError:
            f = open(file, 'w+')
            print("File Created")
            return True

    def text_to_list(self):
        with open('scores.txt', 'r') as file:
            for line in file:
                parts = line.split(';')
                player = Player(parts[0], parts[1], parts[3])
                self.top_ten_scores.append(player)

    def list_to_text(self):
        with open('scores.txt', 'w') as file:
            for player in self.top_ten_scores:
                file.write(
                    f"{player.name};{player.points};{player.level}\n")
