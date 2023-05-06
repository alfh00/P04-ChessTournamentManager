from player import Player

class Participant(list):
    def append(self, object):
    """Append a player."""
    if not isinstance(object, Player):
        return ValueError("Vous ne pouvez ajouter que des joueurs !")
    return super().append(object)