import itertools
from datetime import datetime

# import matplotlib.pyplot as plt
import networkx as nx

from models.models import Match, Player, Round, Tournament
from views.views import Views

import json
import jsonpickle


class Controller:
    def __init__(self, console):
        self.views = Views(console)

    def collect_players_infos(self):
        players_infos = self.views.get_players_infos()
        players = []
        for player in players_infos:
            players.append(Player(player["Prénom"], player["Nom"], player["Date de naissance"]))
        return players

    def create_tournament(self, players):
        tournament_infos = self.views.get_tournament_infos()
        title, location, num_rounds = tournament_infos
        tournament = Tournament(title, location, players, num_rounds)
        return tournament

    def play_rounds(self, tournament):
        players = tournament.players
        num_rounds = tournament.num_rounds

        # Initialize an undirected Graph with a node for each player
        graph = nx.Graph()
        graph.add_nodes_from(players)

        # Keep track of previous matches
        previous_pairings = tournament.prev_pairs

        # Generate all possible pairings (matches), excluding previous pairings
        possible_pairings = [
            (p1, p2)
            for p1, p2 in itertools.combinations(players, 2)
            if (p1, p2) not in previous_pairings and (p2, p1) not in previous_pairings
        ]

        for round_num in range(len(tournament.rounds) + 1, num_rounds + 1):
            self.views.print_round_number(round_num)

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
                tournament.prev_pairs.append((player1, player2))

                round.matches.append(match)

            tournament.rounds.append(round)

            if self.views.ask_save():
                tournament.save()
                return self.views.show_confirmation("Tournois sauvegardé", 3)

            players.sort(key=lambda x: x.score, reverse=True)

            # for player in players:
            #     print(f"{player.first_name} score: {player.score}")

            # nx.draw_spring(graph, with_labels=True)
            # plt.show()

        tournament.end_date = datetime.now().strftime("%m/%d/%Y, %H:%M")

        self.views.print_tournament_report(tournament)
        tournament.save()
        self.views.show_confirmation(f"Le Tournois {tournament.name} a été sauvegardé", 3)

        return tournament

    def create_match(self, pair):
        match = Match(pair)
        return match

    def collect_matches_results(self, matches):
        for match in matches:
            result = self.views.get_match_result(match)
            match.result = result
        return matches

    def find_tournament_and_play(self):
        with open("./db/tournaments.json", "r") as f:
            data = json.load(f)["tournaments"]

        all_tournaments = [jsonpickle.decode(tournament) for tournament in data]
        in_progress_tournaments = list(filter(lambda x: x.end_date is None, all_tournaments))
        if not in_progress_tournaments:
            self.views.show_confirmation("Aucun Tournois encours", 3)
        else:
            tournament = self.views.show_tournament_list(in_progress_tournaments)
            return self.play_rounds(tournament)

    def print_report(self):
        with open("./db/tournaments.json", "r") as f:
            data = json.load(f)["tournaments"]

        all_tournaments = [jsonpickle.decode(tournament) for tournament in data]

        tournament = self.views.show_tournament_list(all_tournaments)
        self.views.print_tournament_report(tournament)

    def add_player(self):
        players_infos = self.views.get_players_infos()

        players = []
        for player in players_infos:
            players.append((Player(player["Prénom"], player["Nom"], player["Date de naissance"])))

        for player in players:
            player.save()
            self.views.show_confirmation(f"{player.first_name} {player.last_name} sauvegardé avec succes", 1)

    def show_players(self):
        with open("./db/players.json", "r") as f:
            player_data = json.load(f)["players"]

        if not player_data:
            return self.views.show_confirmation("Aucun joueur enregitré", 3)
        else:
            all_players = [jsonpickle.decode(player) for player in player_data]

            player = self.views.show_players_list(all_players)

            return player

    def show_player_info(self, player):
        return self.views.show_player_infos(player)

    def delete_player(self, player):
        confirm = self.views.ask_for_confirmation(f"vous voulez supprimer le joueur {player.first_name} Y/N")
        if confirm:
            player.delete()
            self.views.show_confirmation(f"{player.first_name} {player.last_name} a été supprimé", 3)
