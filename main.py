from controller.controller import Controller


def app():
    controller = Controller()
    players = controller.collect_players_infos()
    tournament = controller.create_tournament(players)


if __name__ == "__main__":
    app()
