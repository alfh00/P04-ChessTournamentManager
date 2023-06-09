import math
from datetime import datetime
import json
import jsonpickle


class Tournament:
    def __init__(self, name, location, players, num_rounds=None):
        self.name = name
        self.location = location
        self.start_date = datetime.now().strftime("%m/%d/%Y, %H:%M")
        self.end_date = None
        self.num_rounds = self.calculate_rounds_number(num_rounds, players)
        self.prev_pairs = []
        self.rounds = []
        self.players = players
        self.description = ""
        self.PATH = "./db/tournaments.json"

    def calculate_rounds_number(self, num_rounds, players):
        if not num_rounds or num_rounds == "":
            return math.ceil(math.log2(len(players) - 1))
        else:
            return int(num_rounds)

    def load_data(self):
        with open(self.PATH, "r") as f:
            data = json.load(f)
        return data

    def save_data(self, data):
        with open(self.PATH, "w") as f:
            json.dump(data, f, indent=4)

    def save(self):
        data = self.load_data()
        tournaments = data["tournaments"]
        all_tournaments = [jsonpickle.decode(tournament) for tournament in tournaments]
        all_tournaments = list(filter(lambda x: x.name != self.name, all_tournaments))
        all_tournaments.append(self)
        sereilized_tournaments = {"tournaments": [jsonpickle.encode(tournament) for tournament in all_tournaments]}
        self.save_data(sereilized_tournaments)

    def __str__(self):
        return f"Tournament(name: {self.name},\nLocation: {self.location},\nStart: {self.start_date},\
            \nEnd: {self.end_date},\nRounds_num{self.num_rounds},\nprev_pairs{self.prev_pairs}\
            ,\nRounds{self.rounds},\nPlayers: {self.players},\nDescription: {self.description})"

    def __repr__(self):
        return self.__str__()


class Player:
    def __init__(self, fname, lname, bday):
        self.first_name = fname
        self.last_name = lname
        self.birthday = bday
        self.rank = 0
        self.score = 0
        self.PATH = "./db/players.json"

    def load_data(self):
        with open(self.PATH, "r") as f:
            data = json.load(f)
        return data

    def save_data(self, data):
        with open(self.PATH, "w") as f:
            json.dump(data, f, indent=4)

    def save(self):
        data = self.load_data()
        serialized_tournament = jsonpickle.encode(self)
        data["players"].append(serialized_tournament)
        self.save_data(data)

    def delete(self):
        raw_players = self.load_data()["players"]
        players = [jsonpickle.decode(player) for player in raw_players]
        players = list(filter(lambda x: x.first_name != self.first_name, players))
        sereilized_players = {"players": [jsonpickle.encode(player) for player in players]}
        self.save_data(sereilized_players)

    def __str__(self):
        return f"Player({self.first_name}, {self.last_name}, {self.birthday}, {self.rank}, {self.score})"

    def __repr__(self):
        return self.__str__()


class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []

    def __str__(self):
        return f"Round {self.number}: {len(self.matches)} matches"

    def __repr__(self):
        return f"Round(round_number={self.number}, matches={self.matches})"


class Match:
    def __init__(self, pair):
        self.player_1 = pair[0]
        self.player_2 = pair[1]
        self.result = None

    def __str__(self):
        return f"{self.player_1.first_name} vs {self.player_2.first_name}\n result {self.result}"

    def __repr__(self):
        return f"Match({self.player_1.first_name}, {self.player_2.first_name}, result={self.result})"


class Menu:
    def __init__(self, name, submenus=None):
        self.name = name
        self.submenus = submenus if submenus else []
