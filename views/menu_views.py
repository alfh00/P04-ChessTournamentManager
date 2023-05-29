import curses


class MenuView:
    def __init__(self, menu, console):
        hei, wid, w = console  # (hei, wei, w)
        self.menu = menu
        self.current_menu = menu
        self.current_row = 0
        self.win = w
        self.hei = hei
        self.wid = wid
        # self.menu.submenus.append("Retour")

    def print_menu(self):
        self.win.clear()

        for idx, row in enumerate(self.current_menu.submenus):
            x = self.wid // 2 - len(row.name) // 2
            y = self.hei // 2 - len(self.current_menu.submenus) // 2 + idx

            if idx == self.current_row:
                # self.win.attron(curses.color_pair(1))
                self.win.addstr(y, x, row.name, curses.color_pair(1))
                # self.win.attroff(curses.color_pair(1))
            else:
                self.win.addstr(y, x, row.name)
            self.win.addstr(0, 0, self.current_menu.name, curses.color_pair(1))
        self.win.refresh()

    def navigate_menu(self):
        self.print_menu()

        while True:
            # return action if on a leaf submenu pressed
            if not self.current_menu.submenus:
                return self.current_menu.name
            # otherwise keep navigating
            key = self.win.getch()
            self.win.clear()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.current_menu.submenus) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # Quit if we are on the root menu
                if self.menu == self.current_menu and self.current_row == len(self.menu.submenus) - 1:
                    return "Quitter"
                # get parent menu if we are on a submenu
                elif self.current_row == len(self.current_menu.submenus) - 1:
                    self.current_menu = self.get_parent_menu(self.menu, self.current_menu)
                    self.current_row = 0
                # get child submenus if selected
                else:
                    self.current_menu = self.current_menu.submenus[self.current_row]
                    self.current_row = 0
            print(self.current_menu.name)
            print(self.current_row)
            self.print_menu()
            self.win.refresh()

    def get_parent_menu(self, root_menu, submenu):
        for menu in root_menu.submenus:
            if submenu in menu.submenus:
                return menu
        return root_menu
