from views.menu_views import MenuView
from models.models import Menu


MENU = Menu(
    "Main Menu",
    [
        Menu(
            "Joueurs",
            [Menu("Afficher les joueurs"), Menu("Ajouter un joueur"), Menu("Supprimer un joueur")],
        ),
        Menu(
            "Tournois",
            [Menu("Afficher les tournois"), Menu("Lancer un tournois")],
        ),
    ],
)


class MenuController:
    def __init__(self):
        self.menu = MENU

    def start(self):
        menu_view = MenuView(self.menu)
        menu_view.navigate_menu()
