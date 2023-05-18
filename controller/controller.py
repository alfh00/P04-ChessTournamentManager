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

    def play_rounds(self, tournament):
        all_pairs = tournament.possible_pairs
        players = tournament.players
        num_rounds = tournament.num_rounds
        rounds = []

        # Initialize an undirected Graph with a node for each player
        graph = nx.Graph()
        graph.add_nodes_from(players)

        # Keep track of previous matches
        previous_pairings = []

        # Generate all possible pairings (matches), excluding previous pairings
        possible_pairings = [
            (p1, p2)
            for p1, p2 in itertools.combinations(players, 2)
            if (p1, p2) not in previous_pairings and (p2, p1) not in previous_pairings
        ]

        for round_num in range(1, num_rounds + 1):
            print(f"Round {round_num}:")
            round = Round(round_num)

            # Add an edge to the graph for each possible pairing based on score difference
            for player1, player2 in possible_pairings:
                if (player1, player2) in previous_pairings or (player2, player1) in previous_pairings:
                    score_difference = abs(player1.score - player2.score) + 10
                else:
                    score_difference = abs(player1.score - player2.score)
                graph.add_edge(player1, player2, weight=score_difference)

            matching = list(nx.algorithms.matching.min_weight_matching(graph, weight="weight"))

            for player1, player2 in matching:
                match = Match((player1, player2))
                result = self.views.get_match_result((player1, player2))

                if result == "1":
                    player1.score += 1
                    match.result = "1 - 0"
                elif result == "0":
                    player2.score += 1
                    match.result = "0 - 1"
                elif result == "0.5":
                    player1.score += 0.5
                    player2.score += 0.5
                    match.result = "0.5 - 0.5"
                # Add player pairing to previous_pairings
                previous_pairings.append((player1, player2))

                round.matches.append(match)

            rounds.append(round)

            players.sort(key=lambda x: x.score, reverse=True)

            for player in players:
                print(f"{player.first_name} score: {player.score}")

            # nx.draw_spring(graph, with_labels=True)
            # plt.show()
        tournament.rounds = rounds
        return tournament

    def create_match(self, pair):
        match = Match(pair)
        return match

    def collect_matches_results(self, matches):
        print(matches)
        for match in matches:
            result = self.views.get_match_result(match)
            match.result = result
        return matches
