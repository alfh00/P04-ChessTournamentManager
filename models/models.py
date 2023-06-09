import math
from datetime import datetime
import json
import jsonpickle


class Tournament:
    """Class representing a tournament."""
    def __init__(self, name, location, players, num_rounds=None):
        """
        Represents a tournament.

        Attributes:
            name (str): The name of the tournament.
            location (str): The location of the tournament.
            start_date (str): The start date of the tournament.
            end_date (str): The end date of the tournament.
            num_rounds (int): The number of rounds in the tournament.
            prev_pairs (list): List of previous player pairings.
            rounds (list): List of Round objects representing each round.
            players (list): List of Player objects participating in the tournament.
            description (str): Description of the tournament.
            PATH (str): Path to the tournament data file.

        Methods:
            calculate_rounds_number(num_rounds, players):\
            Calculates the number of rounds based on the number of players.
            load_data(): Loads tournament data from the data file.
            save_data(data): Saves tournament data to the data file.
            save(): Saves the tournament object to the data file.
        """
        self.name = name
        self.location = location
        self.start_date = datetime.now().strftime("%m/%d/%Y, %H:%M")
        self.end_date = None
        self.num_rounds = self.calculate_rounds_number(num_rounds, players)
        self.prev_pairs = []
        self.rounds = []
        self.players = players
        self.description = ""
        self.PATH = "./db/tournaments.json"

    def calculate_rounds_number(self, num_rounds, players):
        """
        Calculate the number of rounds in the tournament.

        If the number of rounds is not provided, it is calculated based on the number of players.

        Args:
            num_rounds (int): Number of rounds specified by the user.
            players (list): List of Player objects participating in the tournament.

        Returns:
            int: The calculated number of rounds.
        """
        if not num_rounds or num_rounds == "":
            return math.ceil(math.log2(len(players) - 1))
        else:
            return int(num_rounds)

    def load_data(self):
        """
        Load tournament data from a JSON file.

        Returns:
            dict: The loaded raw pickeled data.
        """
        with open(self.PATH, "r") as f:
            data = json.load(f)
        return data

    def save_data(self, data):
        """
        Save tournament data to a JSON file.

        Args:
            data : The data to be saved.
        """
        with open(self.PATH, "w") as f:
            json.dump(data, f, indent=4)

    def save(self):
        """Save the tournament object to the database."""
        data = self.load_data()
        tournaments = data["tournaments"]
        all_tournaments = [jsonpickle.decode(tournament) for tournament in tournaments]
        all_tournaments = list(filter(lambda x: x.name != self.name, all_tournaments))
        all_tournaments.append(self)
        sereilized_tournaments = {"tournaments": [jsonpickle.encode(tournament) for tournament in all_tournaments]}
        self.save_data(sereilized_tournaments)

    def __str__(self):
        return f"Tournament(name: {self.name},\nLocation: {self.location},\nStart: {self.start_date},\
            \nEnd: {self.end_date},\nRounds_num{self.num_rounds},\nprev_pairs{self.prev_pairs}\
            ,\nRounds{self.rounds},\nPlayers: {self.players},\nDescription: {self.description})"

    def __repr__(self):
        return self.__str__()


class Player:
    """Class representing a player."""
    def __init__(self, fname, lname, bday):
        """
        Represents a player.

        Attributes:
            first_name (str): The first name of the player.
            last_name (str): The last name of the player.
            birthday (str): The birthday of the player.
            rank (int): The rank of the player.
            score (int): The score of the player.
            PATH (str): Path to the player data file.

        Methods:
            load_data(): Loads player data from the data file.
            save_data(data): Saves player data to the data file.
            save(): Saves the player object to the data file.
            delete(): Deletes the player object from the data file.
        """
        self.first_name = fname
        self.last_name = lname
        self.birthday = bday
        self.rank = 0
        self.score = 0
        self.PATH = "./db/players.json"

    def load_data(self):
        """
        Load player data from a JSON file.

        Returns:
            dict: The loaded JSON data.
        """
        with open(self.PATH, "r") as f:
            data = json.load(f)
        return data

    def save_data(self, data):
        """
        Save player data to a JSON file.

        Args:
            data (dict): The data to be saved.
        """
        with open(self.PATH, "w") as f:
            json.dump(data, f, indent=4)

    def save(self):
        """Save the player object to the database."""
        data = self.load_data()
        serialized_tournament = jsonpickle.encode(self)
        data["players"].append(serialized_tournament)
        self.save_data(data)

    def delete(self):
        """Delete the player object from the database."""
        raw_players = self.load_data()["players"]
        players = [jsonpickle.decode(player) for player in raw_players]
        players = list(filter(lambda x: x.first_name != self.first_name, players))
        sereilized_players = {"players": [jsonpickle.encode(player) for player in players]}
        self.save_data(sereilized_players)

    def __str__(self):
        return f"Player({self.first_name}, {self.last_name}, {self.birthday}, {self.rank}, {self.score})"

    def __repr__(self):
        return self.__str__()


class Round:
    """
    Represents a round in a tournament.

    Attributes:
        number (int): The number of the round.
        matches (list): List of Match objects representing the matches in the round.
    """
    def __init__(self, number):
        self.number = number
        self.matches = []

    def __str__(self):
        return f"Round {self.number}: {len(self.matches)} matches"

    def __repr__(self):
        return f"Round(round_number={self.number}, matches={self.matches})"


class Match:
    """
    Represents a match between two players.

    Attributes:
        player_1 (Player): The first player.
        player_2 (Player): The second player.
        result (str or None): The result of the match.
    """
    def __init__(self, pair):
        self.player_1 = pair[0]
        self.player_2 = pair[1]
        self.result = None

    def __str__(self):
        return f"{self.player_1.first_name} vs {self.player_2.first_name}\n result {self.result}"

    def __repr__(self):
        return f"Match({self.player_1.first_name}, {self.player_2.first_name}, result={self.result})"


class Menu:
    """
    Represents a menu.

    Attributes:
        name (str): The name of the menu.
        submenus (list): List of submenus.
    """
    def __init__(self, name, submenus=None):
        self.name = name
        self.submenus = submenus if submenus else []
