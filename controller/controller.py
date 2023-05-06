from models.models import Player, Tournament
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
