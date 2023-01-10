import json


def fileReader(filename: str):
    with open(filename) as file:
        data = file.read()
    return json.loads(data)


class PlayersApp:
    def __init__(self):
        pass

    def help(self):
        print('''
commands:
0 quit
1 search for player
3 countries
4 players in team
5 players from country
6 most points
7 most goals''')

    def get_player(self):
        name = input('name: ')
        for player in self.players:
            if player['name'] == name:
                print(
                    f"\n{player['name']:21}{player['nationality']:>3}{player['goals']:>4} + {player['assists']:>2} = {(player['goals'] + player['assists']):>3}")

    def execute(self):
        file_name = input('file name: ')
        self.players = fileReader(file_name)
        print(f"read the data of {len(self.players)} players")
        self.help()
        while True:
            command = input('\ncommand: ')
            if command == '0':
                break
            elif command == '1':
                self.get_player()


test = PlayersApp()
test.execute()
