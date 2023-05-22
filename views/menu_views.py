import curses


class MenuView:
    def __init__(self, menu):
        self.menu = menu
        self.current_menu = menu
        self.current_row = 0
        self.scr = curses.initscr()
        # self.menu.submenus.append("Retour")

    def print_menu(self):
        self.scr.clear()
        h, w = self.scr.getmaxyx()

        for idx, row in enumerate(self.current_menu.submenus):
            x = w // 2 - len(row.name) // 2
            y = h // 2 - len(self.current_menu.submenus) // 2 + idx

            if idx == self.current_row:
                # self.scr.attron(curses.color_pair(1))
                self.scr.addstr(y, x, row.name, curses.color_pair(1))
                # self.scr.attroff(curses.color_pair(1))
            else:
                self.scr.addstr(y, x, row.name)

        self.scr.refresh()

    def navigate_menu(self):
        curses.curs_set(0)
        curses.start_color()
        self.scr.keypad(1)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.print_menu()

        while True:
            key = self.scr.getch()
            self.scr.clear()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.current_menu.submenus) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # Quit if we are on the root menu
                if self.menu == self.current_menu and self.current_row == len(self.current_menu.submenus) - 1:
                    break
                # get parent menu if we are on a submenu
                elif self.current_row == len(self.current_menu.submenus) - 1:
                    self.current_menu = self.get_parent_menu(self.menu, self.current_menu)
                    self.current_row = 0
                elif not len(self.current_menu.submenus):
                    return self.current_menu.name
                # get child submenus on selection
                else:
                    self.current_menu = self.current_menu.submenus[self.current_row]
                    self.current_row = 0

            self.print_menu()
            self.scr.refresh()

    def start(self):
        curses.wrapper(self.navigate_menu)

    def get_parent_menu(self, root_menu, submenu):
        for menu in root_menu.submenus:
            if submenu in menu.submenus:
                return menu
        return root_menu
