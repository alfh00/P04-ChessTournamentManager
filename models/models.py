from datetime import datetime


class Tournament:
    def __init__(self, name, location, players, rounds_number=4):
        self.name = name
        self.location = location
        self.start_date = datetime.now()
        self.end_date = None
        self.rounds_number = rounds_number
        self.rounds_list = []
        self.players = players
        self.description = ""

    def __str__(self):
        return f"Tournament({self.name}, {self.location}, {self.start_date}, {self.end_date}, {self.rounds_number}, {self.rounds_list}, {self.players}, {self.description})"

    def __repr__(self):
        return self.__str__()


class Player:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ""
        self.birthday = ""
        self.points = 0
        self.rank = 0

        def __str__(self):
            return f"Player({self.first_name}, {self.last_name}, {self.birthday}, {self.points}, {self.rank})"

        def __repr__(self):
            return self.__str__()


# class Round:

# class Match:
#     def __init__(self):
#         self.player1 = Participant()
#         self.player2 = Participant()

#     def assign_color(self):
