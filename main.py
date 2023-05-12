from controller.controller import Controller


def app():
    controller = Controller()
    players = controller.collect_players_infos()
    tournament = controller.create_tournament(players)
    # print(tournament.__str__)
    round = controller.create_rounds(tournament.players, tournament.num_rounds)


if __name__ == "__main__":
    app()
