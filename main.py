import curses

from controller.controller import Controller
from controller.menu_controller import MenuController


def init_curses():
    # initialize the screen
    scr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.start_color()
    curses.cbreak()
    # initialize the window
    hei, wid = scr.getmaxyx()
    wid = wid if wid % 2 == 0 else wid - 1
    w = curses.newwin(hei, wid, 0, 0)
    w.keypad(True)
    global console
    console = hei, wid, w
    # initialize color_pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)


def reset_terminal_settings():
    curses.nocbreak()
    curses.curs_set(False)
    console[2].keypad(False)
    curses.echo()
    curses.endwin()


def app():
    while True:
        init_curses()
        nav_controller = MenuController(console)
        controller = Controller(console)
        action = nav_controller.start()

        # Players Actions

        if action == "Afficher les joueurs":
            player = controller.show_players()
            controller.show_player_info(player)

        if action == "Ajouter un joueur":
            controller.add_player()

        if action == "Supprimer un joueur":
            player = controller.show_players()
            controller.delete_player(player)

        # Tournois Actions

        if action == "Nouveau tournois":
            players = controller.collect_players_infos()
            tournament = controller.create_tournament(players)
            tournament = controller.play_rounds(tournament)

        if action == "Continuer un tournois":
            controller.find_tournament_and_play()

        if action == "Afficher les rapports":
            controller.print_report()

        action = None
        reset_terminal_settings()


if __name__ == "__main__":
    try:
        app()
    finally:
        curses.endwin()
