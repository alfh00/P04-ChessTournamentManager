from controller.controller import Controller
from controller.menu_controller import MenuController
import curses


def init_curses():
    pass


def app():
    global controller, nav_controller
    controller = Controller()
    nav_controller = MenuController()
    action = nav_controller.start()
    print(action)

    if action == "Lancer un tournois":
        players = controller.collect_players_infos()
        tournament = controller.create_tournament(players)
        # print(tournament.possible_pairing)
        tournament = controller.play_rounds(tournament)


if __name__ == "__main__":
    try:
        init_curses()
        app()
    finally:
        curses.endwin()
