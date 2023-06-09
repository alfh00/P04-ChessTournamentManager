import curses

from controller.controller import Controller
from controller.menu_controller import MenuController


def init_curses():
    """
    Initializes the curses library and sets up the screen and window.
    """
    scr = curses.initscr()  # initialize the screen
    curses.curs_set(0)  # hide the cursor
    curses.noecho()  # do not echo user input
    curses.start_color()  # enable color support
    curses.cbreak()  # enter cbreak mode
    hei, wid = scr.getmaxyx()  # get screen dimensions
    wid = wid if wid % 2 == 0 else wid - 1  # adjust width if odd
    w = curses.newwin(hei, wid, 0, 0)  # create a new window
    w.keypad(True)  # enable keypad input
    global console
    console = hei, wid, w  # store the window in console variable
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # initialize color pairs


def reset_terminal_settings():
    """
    Resets the terminal settings after the program is done.
    """
    curses.nocbreak()  # exit cbreak mode
    curses.curs_set(False)  # show the cursor
    console[2].keypad(False)  # disable keypad input
    curses.echo()  # enable echoing of user input
    curses.endwin()  # end curses


def app():
    """
    Main application loop.
    """
    while True:
        init_curses()
        nav_controller = MenuController(console)
        controller = Controller(console)
        action = nav_controller.start()  # display menu and get user action

        # Players Actions

        if action == "Afficher les joueurs":
            player = controller.show_players()  # get player selection
            controller.show_player_info(player)  # display player info

        if action == "Ajouter un joueur":
            controller.add_player()  # add a new player

        if action == "Supprimer un joueur":
            player = controller.show_players()  # get player selection
            controller.delete_player(player)  # delete selected player

        # Tournois Actions

        if action == "Nouveau tournois":
            players = controller.collect_players_infos()  # collect player info
            tournament = controller.create_tournament(players)  # create a new tournament
            tournament = controller.play_rounds(tournament)  # play tournament rounds

        if action == "Continuer un tournois":
            controller.find_tournament_and_play()  # find and continue an existing tournament

        if action == "Afficher les rapports":
            controller.print_report()  # display tournament reports

        action = None
        reset_terminal_settings()


if __name__ == "__main__":
    try:
        app()
    finally:
        curses.endwin()  # make sure curses is properly ended
