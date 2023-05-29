import curses
from time import sleep

from controller.controller import Controller
from controller.menu_controller import MenuController


def init_curses():
    # initialize the screen
    scr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.start_color()
    # initialize the window
    global console
    hei, wid = scr.getmaxyx()
    wid = wid if wid % 2 == 0 else wid - 1
    w = curses.newwin(hei, wid, 0, 0)
    w.keypad(True)
    console = hei, wid, w
    # initialize color_pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)


def app():
    # nav_controller = MenuController(console)
    # controller = Controller(console)

    while True:
        nav_controller = MenuController(console)
        controller = Controller(console)
        action = nav_controller.start()

        if action == "Lancer un tournois":
            players = controller.collect_players_infos()
            tournament = controller.create_tournament(players)
            tournament = controller.play_rounds(tournament)
        if action == "Quitter":
            break

        action = None


if __name__ == "__main__":
    try:
        init_curses()
        app()
    finally:
        curses.endwin()
