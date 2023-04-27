import json

PLAYERS_FILE_PATH = "./models/players.json"


class Players:
    def __init__(self):
        self.players = self.load_data()["players"]
        self.lenght = self.load_data()["length"]

    def load_data(self):
        with open(PLAYERS_FILE_PATH, "r") as file:
            data = json.load(file)
            return data

    def add_player(self, new_player):
        new_player = Player(new_player)

        data = self.load_data()
        data["players"].append(new_player.__dict__)
        data["length"] += 1

        with open(PLAYERS_FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)


class Player:
    def __init__(self, new_player):
        self.id = new_player["id"]
        self.first_name = new_player["first_name"]
        self.last_name = new_player["last_name"]

    def edit_player(self, new_entries):
        self.id = new_entries["id"]
        self.first_name = new_entries["first_name"]
        self.last_name = new_entries["last_name"]

    # def add_player(self, new_player):
    #     new_player = Player(new_player)

    #     data = self.load_data()
    #     data["players"].append(new_player.__dict__)
    #     data["length"] += 1

    #     with open(PLAYERS_FILE_PATH, "w") as file:
    #         json.dump(data, file, indent=4)


class tournament:
    def __init__(self, title, start_date, end_date, players=[]):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.players = players

    def add_player(player):
        pass


players = Players()
players.add_player({"id": "AA00003", "first_name": "Ali3", "last_name": "Fathallah3"})
