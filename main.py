from controller.controller import Controller


def app():
    controller = Controller()
    players = controller.collect_players_infos()
    tournament = controller.create_tournament(players)
    # print(tournament.__str__)
    for i in range(tournament.rounds_number):
        round = controller.create_round(tournament.players)
        matches = controller.create_matches(round.pairing)
        round.matches = matches
        matches_results = controller.collect_matches_results(matches)
        tournament.rounds_list.append(round)
    print(tournament)


if __name__ == "__main__":
    app()
