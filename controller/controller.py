from models.models import Player, Tournament, Round, Match
from views.views import Views
import itertools
import networkx as nx
import matplotlib.pyplot as plt


class Controller:
    def __init__(self):
        self.views = Views()

    def collect_players_infos(self):
        players_infos = self.views.get_players_infos()
        players = []
        for player in players_infos:
            players.append(Player(player))

        return players

    def create_tournament(self, players):
        tournament_infos = self.views.get_tournament_infos()
        name, location, num_rounds = tournament_infos
        tournament = Tournament(name, location, players, num_rounds)
        return tournament

    def create_rounds(self, players, num_rounds):
        players = players.sort(key=lambda x: x.rank, reverse=True)
        # matrix = [[0 if col <= row else False for col in range(len(players))] for row in range(len(players))]
        seen = []
        for round_number in num_rounds:
            print(f"Round {round_number} fight:")
            mid = len(players) // 2
            winners = players[:mid]
            loosers = players[mid:]

    def create_matches(self, pairs):
        matches = []
        for pair in pairs:
            match = Match(pair)
            matches.append(match)
        return matches

    def collect_matches_results(self, matches):
        print(matches)
        for match in matches:
            result = self.views.get_match_result(match)
            match.result = result
        return matches
