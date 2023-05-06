class Views:
    def __init__(self):
        ...

    def get_players_infos(self):
        players = []
        while True:
            entry = input("Entrez 's' pour sauvegarder\nEntrer le nom du joueur: ")
            if entry == "s":
                break
            players.append(entry)

        return players

    def get_tournament_infos(self):
        tounrnament_name = input("Entrez le nom du tournois: ")
        tounrnament_location = input("Où se passe-t-il: ")
        return tounrnament_name, tounrnament_location
