from datetime import datetime


class Tournament:
    def __init__(self, name, location, players, rounds_number=4):
        self.name = name
        self.location = location
        self.start_date = datetime.now()
        self.end_date = None
        self.rounds_number = rounds_number
        self.rounds_list = []
        self.players = players
        self.description = ""

    def __str__(self):
        return f"Tournament(Name: {self.name},\nLocation: {self.location},\nStart: {self.start_date},\nEnd: {self.end_date},\nRounds_number: {self.rounds_number},\nRounds_list{self.rounds_list},\nPlayers: {self.players},\nDescription: {self.description})"

    def __repr__(self):
        return self.__str__()


class Player:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ""
        self.birthday = ""
        self.rank = 0
        self.score = 0

        def __str__(self):
            return f"Player({self.first_name}, {self.last_name}, {self.birthday}, {self.rank}, {self.score})"

        def __repr__(self):
            return self.__str__()


class Round:
    def __init__(self, players):
        self.players = players
        self.round_number = 0
        self.pairing = []
        self.matches = []

    def __str__(self):
        return f"Round {self.round_number}: {len(self.matches)} matches"

    def __repr__(self):
        return f"Round(players={self.players}, round_number={self.round_number}, pairing={self.pairing}, matches={self.matches})"


class Match:
    def __init__(self, pair):
        self.player_1 = pair[0]
        self.player_2 = pair[1]
        self.result = None

    def __str__(self):
        return f"{self.player_1.first_name} vs {self.player_2.first_name}"

    def __repr__(self):
        return f"Match({self.player_1.first_name}, {self.player_2.first_name}, result={self.result})"
