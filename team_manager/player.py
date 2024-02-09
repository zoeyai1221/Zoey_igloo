

class Player:
    """A class representing a dodgeball player"""
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position

    def __str__(self):
        return f"{self.number}\t{self.name}\t{self.position}"
