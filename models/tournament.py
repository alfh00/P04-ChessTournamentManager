import json


class tournament:
    def __init__(self, title, start_date, end_date, players=[]):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.players = players

    def add_player(self, player):
        self.players.append(player)
