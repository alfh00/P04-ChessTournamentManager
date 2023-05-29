import curses
from curses.textpad import Textbox, rectangle


class Views:
    def __init__(self, console):
        hei, wid, win = console  # (hei, wei, win)
        self.win = win
        self.hei = hei
        self.wid = wid

    def get_players_infos(self):
        players = []
        gathering = True

        while gathering:
            curses.curs_set(1)
            player_number = len(players) + 1
            self.win.addstr(0, 1, f"Entrer le nom du joueur N°{player_number}: ")

            editwin = curses.newwin(1, 28, 2, 2)
            rectangle(self.win, 1, 1, 3, 30)
            self.win.refresh()

            box = Textbox(editwin)
            box.edit()

            player = box.gather().strip().replace("\n", "")

            if player == "fini":
                gathering = False
                self.win.clear()
                break

            print(player)

            players.append(player)

        return players

    def get_tournament_infos(self):
        curses.echo()
        self.win.addstr("Entrez le nom du tournois: ")
        tounrnament_name = self.win.getstr().decode("utf-8")
        self.win.addstr("Entrez le Lieu du tournois: ")
        tounrnament_location = self.win.getstr().decode("utf-8")
        self.win.addstr("prédeterminer le nombre de tour: ")
        tounrnament_num_rounds = self.win.getstr().decode("utf-8")
        self.win.refresh()

        # self.win.refresh
        # tounrnament_location = input("Où se passe-t-il: ")
        # tounrnament_num_rounds = input("prédeterminer le nombre de tour: ")
        return tounrnament_name, tounrnament_location, tounrnament_num_rounds

    def get_match_result(self, pair):
        self.win.addstr(
            f"Entrez le resultat du match {pair[0].first_name} - {pair[1].first_name}\n(1) Si {pair[0].first_name} est gagnant\n(0) Si {pair[1].first_name} est gagnant\n(0.5) égalité\n>>> ",
        )
        result = self.win.getstr().decode("utf-8")
        print(f"{result}")
        self.win.refresh()

        return result

    def print_tournament_report(self, tournament):
        curses.curs_set(0)
        self.win.clear()
        self.win.addstr(f"Tournoi: {tournament.name}, Lieu:{tournament.location}\n\n")
        self.win.addstr(f"Début: {tournament.start_date}, Fin:{tournament.end_date}\n\n")

        for round in tournament.rounds:
            self.win.addstr(f"\nRound : {round.number}\n\n")
            for match in round.matches:
                self.win.addstr(f"{match.player_1.first_name} {match.result} {match.player_2.first_name}\n")

        self.win.getch()

    def print_round_number(self, round_num):
        self.win.addstr(f"\Tour N°: {round_num}\n\n")
