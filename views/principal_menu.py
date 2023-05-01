import curses


menu = {
    "Joueurs": {"Afficher les joueurs": None, "Ajouter un joueur": None, "Editer un joueur": None, "Retour": None},
    "Tournois": {"Afficher les tournois": None, "Ajouter un tournois": None, "Gestion Tournois": None},
    "Quitter": None,
    "Help": None,
}


class Views:
    def __init__(self, menu):
        self.menu = menu

    # def select_menu(self):
    #     if not self.menu:
    #         self.menu = menu

    def print_menu(self, stdscr, selected_row):
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(self.menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.menu) // 2 + idx

            if idx == selected_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()

    def navigate(self, stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        current_row = 0

        self.print_menu(stdscr, current_row)

        while 1:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER:
                stdscr.addstr(0, 0, f"Vous êtes dans {self.menu[current_row]}")
                stdscr.refresh()
                stdscr.getch()
                if current_row == len(self.menu) - 1:
                    break

            self.print_menu(stdscr, current_row)
            stdscr.refresh()

    def launch(self):
        curses.wrapper(self.navigate)


view = Views(menu)
view.launch()
