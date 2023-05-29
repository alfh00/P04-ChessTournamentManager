from models.models import Menu
from views.menu_views import MenuView

MENU = Menu(
    "Main Menu",
    [
        Menu(
            "Joueurs",
            [Menu("Afficher les joueurs"), Menu("Ajouter un joueur"), Menu("Supprimer un joueur"), Menu("Retour")],
        ),
        Menu(
            "Tournois",
            [Menu("Afficher les tournois"), Menu("Lancer un tournois"), Menu("Retour")],
        ),
        Menu("Quitter"),
    ],
)


class MenuController:
    def __init__(self, console):
        self.menu = MENU
        self.menu_view = MenuView(self.menu, console)

    def start(self):
        return self.menu_view.navigate_menu()
