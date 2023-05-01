import json

PLAYER_PATH = "./models/db/players.json"


class Players:
    def __init__(self):
        self.path = PLAYER_PATH

    def load_data(self):
        with open(self.path, "r") as f:
            data = json.load(f)
        return data

    def save_data(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def add_player(self, new_player):
        data = self.load_data()

        data["players"].append(new_player)
        data["length"] += 1

        self.save_data(data)

    def delete_player(self, player):
        data = self.load_data()
        data["players"] = list(filter((lambda x: x["first_name"] != player["first_name"]), data["players"]))
        data["length"] -= 1
        self.save_data(data)

    def update_player(self, updated_player):
        id, first_name, last_name = updated_player.values()
        data = self.load_data()
        for player in data["players"]:
            if player["id"] == id:
                player["first_name"] = first_name
                player["last_name"] = last_name
        self.save_data(data)


class Player:
    def __init__(self, player):
        self.id = player["id"]
        self.first_name = player["first_name"]
        self.last_name = player["last_name"]


players = Players()
# players.add_player({"id": "AA001", "first_name": "Al", "last_name": "Fh"})
players.update_player({"id": "KY1806", "first_name": "Morganeeee", "last_name": "Harrisse"})
# players.delete_player({"id": "AA001", "first_name": "Al", "last_name": "Fh"})
