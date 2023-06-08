import curses
from curses.textpad import Textbox, rectangle
from time import sleep


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
            self.win.clear()
            player_infos = {"Prénom":"", "Nom":"","Date de naissance":""}

            for key, val in player_infos.items():
                curses.curs_set(1)
                player_number = len(players) + 1
                self.win.addstr(0, 1, f"Entrer le {key} du joueur N°{player_number}: ")

                editwin = curses.newwin(1, 28, 2, 2)
                rectangle(self.win, 1, 1, 3, 30)
                self.win.refresh()

                box = Textbox(editwin)
                box.edit()
                self.win.clear()

                player_infos[key] = box.gather().strip().replace("\n", "")

            players.append(player_infos)
            
            gathering = self.ask_for_confirmation('Ajouter encore des joueurs Y/N?')

        return players

    def get_tournament_infos(self):
        curses.echo()
        self.win.clear()
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
        self.win.scrollok(True)
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
        self.win.addstr(f"\nTour N°: {round_num}\n\n")
    
    def ask_save(self):
        self.win.addstr("Continuez (C) ou Sauveagrder (S): ")
        res = self.win.getstr().decode("utf-8").upper()
        return False if res == "C" else True
    
    def show_confirmation( self, message, time ):
        self.win.clear()
        w = self.wid // 2 - len(message) // 2
        h = self.hei // 2 
        self.win.addstr(h, w, message)
        self.win.refresh()
        sleep(time)
    
    def ask_for_confirmation( self, message ):
        self.win.clear()
        w = self.wid // 2 - len(message) // 2
        h = self.hei // 2 
        self.win.addstr(h, w, message)
        curses.echo()
        res = self.win.getstr(h+1, w).decode("utf-8").upper()
        self.win.refresh()
        curses.noecho()
        return False if res == "N" else True
        

    def show_tournament_list(self, tournament_list):

        def print_list(curr_row):
            for idx, t in enumerate(tournament_list):
                x = self.wid // 2 - len(t.name) // 2
                y = self.hei // 2 - len(tournament_list) // 2 + idx

                if idx == curr_row:
                    self.win.addstr(y, x, t.name, curses.color_pair(1))
                else:
                    self.win.addstr(y, x, t.name)
                
            self.win.refresh()
        
        def navigate_menu(tournament_list):
            current_idx = 0
            print_list(current_idx)

            while True:
                
                if not tournament_list:
                    return 
                # otherwise keep navigating
                key = self.win.getch()
                self.win.clear()

                if key == curses.KEY_UP and current_idx > 0:
                    current_idx -= 1
                elif key == curses.KEY_DOWN and current_idx < len(tournament_list) - 1:
                    current_idx += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    curses.nocbreak()
                    self.win.keypad(False)
                    curses.echo()
                    curses.endwin()
                    
                    return tournament_list[current_idx]
                    
                print_list(current_idx)
                self.win.refresh()

        
        return navigate_menu(tournament_list)
    
    def show_players_list(self, players_list):

        def print_list(curr_row):
            for idx, p in enumerate(players_list):
                x = self.wid // 2 - len(f"{p.first_name} {p.last_name}") // 2
                y = self.hei // 2 - len(players_list) // 2 + idx

                if idx == curr_row:
                    self.win.addstr(y, x, f"{p.first_name} {p.last_name}", curses.color_pair(1))
                else:
                    self.win.addstr(y, x, f"{p.first_name} {p.last_name}")
                
            self.win.refresh()
        
        def navigate_menu(players_list):
            current_idx = 0
            print_list(current_idx)

            while True:
                
                if not players_list:
                    return 
                # otherwise keep navigating
                key = self.win.getch()
                self.win.clear()

                if key == curses.KEY_UP and current_idx > 0:
                    current_idx -= 1
                elif key == curses.KEY_DOWN and current_idx < len(players_list) - 1:
                    current_idx += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    curses.nocbreak()
                    self.win.keypad(False)
                    curses.echo()
                    curses.endwin()
                    
                    return players_list[current_idx]
                    
                print_list(current_idx)
                self.win.refresh()

        
        return navigate_menu(players_list)
    
    def show_player_infos(self, player):
        self.win.clear()
        self.win.addstr(f"Prénom: {player.first_name}, Nom:{player.last_name}\n\n")
        self.win.addstr(f"Date de naissance: {player.birthday}\n\n")
        self.win.addstr(f"Rank: {player.rank}")
        self.win.getch()
        