class Views:
    def __init__(self):
        ...

    def get_players_infos(self):
        players = []

        while True:
            player_number = len(players) + 1
            entry = input(f"Entrer le nom du joueur N°{player_number} ou 's' pour sauvegarder: ")
            if entry == "s":
                break
            players.append(entry)

        return players

    def get_tournament_infos(self):
        tounrnament_name = input("Entrez le nom du tournois: ")
        tounrnament_location = input("Où se passe-t-il: ")
        tounrnament_num_rounds = input("prédeterminer le nombre de tour: ")
        return tounrnament_name, tounrnament_location, tounrnament_num_rounds

    def get_match_result(self, pair):
        result = input(
            f"Entrez le resultat du match {pair[0].first_name} - {pair[1].first_name}\n(1) Si {pair[0].first_name} est gagnant\n(0) Si {pair[1].first_name} est gagnant\n(0.5) égalité\n>>> "
        )

        return result
