class Player:
    def __init__(self):
        self.name = None
        self.points = 0
        self.level = 0

    def update_player(self, points, level):
        self.points, self.level = int(points), int(level)

    def __repr__(self):
        return f"{self.name} - Points: {self.points} - Level: {self.level}"


class HighScores:
    def __init__(self):
        self.top_ten_scores = []

    def get_list_length(self):
        return len(self.top_ten_scores)

    def update_scores(self, Player):
        if self.file_exists():
            self.text_to_list()

        if self.player_count == 10:
            if Player.points > self.top_ten_scores[9].points:
                self.top_ten_scores.pop(9)
                
        if self.player_count >= 2:
            self.sort_scores()

        self.top_ten_scores.append(Player)
        self.list_to_text()
        print(self.top_ten_scores)
    
    def text_to_list(self):
        with open('scores.txt', 'r') as file:
            for line in file:
                if len(line) > 3:
                    line = line.replace('\n', '')
                    parts = line.split(';')
                    player = Player(parts[0])
                    print(parts)
                    player.update_player(parts[1], parts[2])
                    self.top_ten_scores.append(player)    

    def sort_scores(self):
        if self.player_count > 0:
            self.top_ten_scores = sorted(
                self.top_ten_scores, key=lambda x: x[points], reverse=True)

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
                file.write(
                    f"{player.name};{player.points};{player.level}\n")
