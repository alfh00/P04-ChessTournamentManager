import curses


class MenuView:
    def __init__(self, menu, console):
        """
        Initializes the MenuView object.

        Args:
            menu (Menu): The menu object to be displayed.
            console (tuple): A tuple containing height, width, and curses window.
        """
        hei, wid, w = console
        self.menu = menu
        self.current_menu = menu
        self.current_row = 0
        self.win = w
        self.hei = hei
        self.wid = wid

    def print_menu(self):
        """
        Prints the current menu on the screen.
        """
        self.win.clear()

        for idx, row in enumerate(self.current_menu.submenus):
            x = self.wid // 2 - len(row.name) // 2
            y = self.hei // 2 - len(self.current_menu.submenus) // 2 + idx

            if idx == self.current_row:
                self.win.addstr(y, x, row.name, curses.color_pair(1))
            else:
                self.win.addstr(y, x, row.name)
            self.win.addstr(0, 0, self.current_menu.name, curses.color_pair(1))
        self.win.refresh()

    def navigate_menu(self):
        """
        Allows the user to navigate the menu and returns the selected action.

        Returns:
            str: The name of the selected action.
        """
        self.print_menu()

        while True:
            if not self.current_menu.submenus:
                return self.current_menu.name
            key = self.win.getch()
            self.win.clear()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.current_menu.submenus) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if self.menu == self.current_menu and self.current_row == len(self.menu.submenus) - 1:
                    quit()
                elif self.current_row == len(self.current_menu.submenus) - 1:
                    self.current_menu = self.get_parent_menu(self.menu, self.current_menu)
                    self.current_row = 0
                else:
                    self.current_menu = self.current_menu.submenus[self.current_row]
                    self.current_row = 0

            self.print_menu()
            self.win.refresh()

    def get_parent_menu(self, root_menu, submenu):
        """
        Returns the parent menu of a given submenu.

        Args:
            root_menu (Menu): The root menu object.
            submenu (Menu): The submenu object.

        Returns:
            Menu: The parent menu object.
        """
        for menu in root_menu.submenus:
            if submenu in menu.submenus:
                return menu
        return root_menu
