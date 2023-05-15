from controller.controller import Controller
from controller.menu_controller import MenuController

program_launched = True


def app():
    controller = Controller()
    # nav_controller = MenuController()
    # nav_controller.start()

    players = controller.collect_players_infos()
    print(len(players))
    tournament = controller.create_tournament(players)
    # print(tournament.possible_pairing)
    rounds = controller.create_rounds(tournament)


if __name__ == "__main__":
    app()
