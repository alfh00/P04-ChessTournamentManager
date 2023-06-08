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
            [Menu("Nouveau tournois"), Menu("Charger un tournois"), Menu("Afficher les rapports"), Menu("Retour")],
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
