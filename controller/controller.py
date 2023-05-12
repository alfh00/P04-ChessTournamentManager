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
        name, location = tournament_infos
        tournament = Tournament(name, location, players)
        return tournament

    def create_rounds(self, players, num_rounds):
        # Shuffle players randomly to avoid predictable pairing based on order
        # random.shuffle(players)

        # Initialize an undirected Graph with a node for each player
        graph = nx.Graph()
        graph.add_nodes_from(players)

        # Keep track of player pairings that have already happened
        previous_pairings = set()

        for round_num in range(num_rounds):
            print(f"Round {round_num + 1}:")

            # Generate all possible pairings (matches), excluding previous pairings
            possible_pairings = [
                (p1, p2)
                for p1, p2 in itertools.combinations(players, 2)
                if (p1, p2) not in previous_pairings and (p2, p1) not in previous_pairings
            ]

            # Add first edge to the graph for each possible pairing between players based on score difference
            # Add second edge: "paired" boolean as players never played
            for player1, player2 in possible_pairings:
                score_difference = abs(player1.score - player2.score)
                graph.add_edge(player1, player2, weight=score_difference, paired=False)

            matching = nx.max_weight_matching(graph, weight="weight", maxcardinality=True)
            for match in matching:
                if not graph[match[0]][match[1]]["paired"]:
                    result = input(f"result {match[0].first_name} vs {match[1].first_name}: ")
                    if result == "1":
                        match[0].score += 1
                    elif result == "0":
                        match[1].score += 1
                    elif result == "0.5":
                        match[0].score += 0.5
                        match[1].score += 0.5
                    graph[match[0]][match[1]]["paired"] = True

                    # Add player pairing to previous_pairings
                    previous_pairings.add((match[0], match[1]))

            players.sort(key=lambda x: x.score, reverse=True)

            for player in players:
                print(f"{player.first_name} score: {player.score}")

            # Reset paired attribute of edges for next round
            # for edge in graph.edges:
            #     graph[edge[0]][edge[1]]["paired"] = False

            # nx.draw_spring(graph, with_labels=True)
            # plt.show()

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
