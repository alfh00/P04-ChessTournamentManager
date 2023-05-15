from models.models import Player, Tournament, Round, Match
from views.views import Views
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import random


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
        title, location, num_rounds = tournament_infos
        tournament = Tournament(title, location, players, num_rounds)
        return tournament

    def create_rounds(self, tournament):
        all_pairs = tournament.possible_pairs
        players = tournament.players
        num_rounds = tournament.num_rounds
        rounds = []

        for round_number in range(1, num_rounds + 1):
            round_pairs = []
            print(f"Round {round_number} fight:")

            for match in range(len(players) // 2):
                pair = random.choice(all_pairs)
                print("THIS IS A PAIR", pair)
                round_pairs.append(pair)
                all_pairs.remove(pair)

                current_round = Round(
                    round_number,
                    round_pairs,
                )
                rounds.append(current_round)

            round_matches = self.create_matches(round_pairs)

            matches_results = self.collect_matches_results(round_matches)

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
