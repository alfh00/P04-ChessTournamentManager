from rich.console import Console
from rich.table import Table
import keyboard


class MenuView:
    def __init__(self, menu):
        self.menu = menu
        self.console = Console()
        self.current_menu = menu
        self.current_submenu_index = 0

    def display_menu(self):
        self.console.clear()
        table = Table(show_header=False, box=None, title=self.current_menu.name)
        for i, submenu in enumerate(self.current_menu.submenus):
            table.add_row(f"[{'red' if i != self.current_submenu_index else 'white'}]{submenu.name}[/]")
        table.add_row(
            f"[{'red' if self.current_submenu_index == len(self.current_menu.submenus) else 'white'}]Back to parent menu[/]"
        )
        self.console.print(table)

    def navigate_menu(self):
        while True:
            self.display_menu()
            event = keyboard.read_event(suppress=True)
            if event.event_type == "down":
                if event.name == "down":
                    self.current_submenu_index += 1
                    if self.current_submenu_index >= len(self.current_menu.submenus):
                        self.current_submenu_index = len(self.current_menu.submenus) - 1
                elif event.name == "up":
                    self.current_submenu_index -= 1
                    if self.current_submenu_index < 0:
                        self.current_submenu_index = 0
                elif event.name == "enter":
                    if self.current_submenu_index == len(self.current_menu.submenus):
                        # go back to the parent menu
                        if self.current_menu == self.menu:
                            # if we're already at the root menu, exit the loop
                            break
                        else:
                            self.current_menu = self.get_parent_menu(self.menu, self.current_menu)
                            self.current_submenu_index = 0
                    elif self.current_submenu_index < len(self.current_menu.submenus):
                        # navigate to the chosen submenu
                        self.current_menu = self.current_menu.submenus[self.current_submenu_index]
                        self.current_submenu_index = 0
            print(self.current_submenu_index)

    def get_parent_menu(self, root_menu, submenu):
        for menu in root_menu.submenus:
            if submenu in menu.submenus:
                return menu
        return root_menu
