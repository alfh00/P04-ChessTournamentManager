from controller.controller import Controller
from controller.menu_controller import MenuController

program_launched = True


def app():
    controller = Controller()
    menu_controller = MenuController()
    menu_controller.start()

    # while program_launched:
    #     menu_controller.run()

    #     # players = controller.collect_players_infos()
    #     # tournament = controller.create_tournament(players)
    #     # # print(tournament.possible_pairing)
    #     # # print(tournament.num_rounds)
    #     # round = controller.create_rounds(tournament.players, tournament.num_rounds)


if __name__ == "__main__":
    app()
