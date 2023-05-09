from models.models import Player, Tournament, Round, Match
from views.views import Views


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

    def create_round(self, players):
        round = Round(players)
        num_players = len(players)
        round_players = sorted(round.players, key=lambda x: (x.score, x.rank), reverse=True)
        # print(round_players)
        for i in range(num_players - 1):
            for j in range(i + 1, num_players):
                player_1 = round_players[i]  # .first_name
                player_2 = round_players[j]  # .first_name
                round.pairing.append((player_1, player_2))

        return round

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
