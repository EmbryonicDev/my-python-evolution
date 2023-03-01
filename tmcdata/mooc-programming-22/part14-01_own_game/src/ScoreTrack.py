class Player:
    def __init__(self):
        self.name = ""
        self.points = 0
        self.level = 0

    def update_player(self, points, level):
        self.points, self.level = int(points), int(level)

    def update_name(self, char):
        if len(self.name) < 12:
            self.name += char

    def pop_name(self):
        if len(self.name) > 0:
            self.name = self.name[:-1]

    def __repr__(self):
        return f"{self.name} - Points: {self.points} - Level: {self.level}"


class HighScores:
    def __init__(self):
        self.top_ten_scores = []

    def get_list_length(self):
        return len(self.top_ten_scores)

    def if_high_score(self, player):
        if ((self.get_list_length() < 10 or
                player.points > min(i.points for i in self.top_ten_scores)) and
                player.name != None):
            return True
        return False

    def get_new_game_scores(self):
        if self.file_exists():
            self.text_to_list()
        if self.get_list_length() > 1:
            self.sort_scores()
            self.list_to_text()

    def print_players(self):
        for player in self.top_ten_scores:
            print(player)

    def update_scores(self, player):
        if self.if_high_score(player):
            self.top_ten_scores.append(player)

        self.sort_scores()

        if self.get_list_length() > 10:
            self.top_ten_scores = self.top_ten_scores[0:10]

        self.list_to_text()

        print('update_scores() - executed like <<<< - Ted Bundy - >>>>')
        # For testing
        self.print_players

    def text_to_list(self):
        with open('scores.txt', 'r') as file:
            for line in file:
                if len(line) > 3:
                    line = line.replace('\n', '')
                    parts = line.split(';')
                    player = Player()
                    print(parts)
                    player.update_player(parts[0], parts[1], parts[2])
                    self.top_ten_scores.append(player)

    def sort_scores(self):
        self.top_ten_scores.sort(key=lambda x: x.points, reverse=True)
        print('scores were sorted')

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

    def list_to_text(self):
        with open('scores.txt', 'w') as file:
            for player in self.top_ten_scores:
                if player.name != "":
                    file.write(
                        f"{player.name};{player.points};{player.level}\n")
