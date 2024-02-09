

# Magic number replacement
INDEX_ZERO = 0


class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.players_on_bench = []

    def send_to_bench(self, player_name):
        # TODO: Put the player "onto the bench"
        # Checking input
        # if the player is already on the bench
        if player_name in self.players_on_bench:
            print(f"{player_name} is already on the bench.")
        else:
            self.players_on_bench.insert(INDEX_ZERO, player_name)

    def get_from_bench(self):
        """
        Return the name of the player who has
        been on the bench longest
        """
        if self.players_on_bench:
            return self.players_on_bench.pop()
        else:
            return None

    def show_bench(self):
        """
        The function that will display the
        current list of players on the bench
        """
        if self.players_on_bench:
            print("The bench currently includes:")
            for player in self.players_on_bench:
                print(player)
        else:
            print("The bench is empty.")  # checking input
