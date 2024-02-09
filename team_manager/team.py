from player import Player
import re


class Team:
    """A class representing a dodgeball team"""

    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []
        # dodgeball positions list
        self.positions = ['catcher', 'corner', 'sniper', 'thrower']

    def set_team_name(self, name):
        # Checking input
        # if the team's name is made up of alphanumeric characters and spaces
        if self.is_alphanumeric_with_spaces(name):
            self.name = name
        else:
            print("Team name can only contain alphanumeric characters"
                  "and spaces.")

    def add_player(self, player_name, player_number, player_position):
        """
        Call the Player class constructor with the appropriate
        values to create a new player object, then add that
        player object to the team's players list
        """
        # Checking input
        # I assume the player's name can only contain alphanumeric characters
        # and spaces, and player's number can only be an actual numerical value
        if (
            self.is_alphanumeric_with_spaces(player_name) and
            player_number.isdigit() and
            # if the player position is in the positions list
            player_position.lower() in self.positions and
            # if the player is new to the player list
            player_name not in [player.name for player in self.players] and
            # if the number is not used in the player list
            player_number not in [player.number for player in self.players]
        ):
            # if all meet, we add the player to the player list, and
            # print out the statement
            player = Player(player_name, player_number, player_position)
            self.players.append(player)
            return True
        else:
            # otherwise, do not add it, and prompt the corresponding warning
            if not self.is_alphanumeric_with_spaces(player_name):
                print("Player's name can only contain alphanumeric"
                      "characters and spaces.")
            if not player_number.isdigit():
                print("Player number must be a numerical value.")
            if player_position.lower() not in self.positions:
                print("We do not have such player's position.")
            if player_name in [player.name for player in self.players]:
                print(player_name, "is already on the team.")
            if player_number in [player.number for player in self.players]:
                print("Number", player_number, "is already been used.")
            return False

    def cut_player(self, player_name):
        """
        Remove the player with the name player_name
        from the players list
        """
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

        if player_name not in [player.name for player in self.players]:
            print(f"{player_name} is not on the team.")

    def is_position_filled(self, position):
        """
        The method that checks whether
        there is currently at least one player on the team
        occupying the requested position
        """
        for player in self.players:
            if player.position == position:
                return True
        return False

    def show_roster(self):
        """
        Method that will display (print to screen)
        the full team roster in the following format:
           The lineup for Seattle Scorpions is:
           15       Garcia          catcher
           55       Wiggins         corner
           99       McCann          sniper
        """
        print(f"The lineup for {self.name} is:")
        if self.players:
            for player in self.players:
                print(player)
        else:
            print("The team currently has no players.")

    def is_alphanumeric_with_spaces(self, input_string):
        """
        Function create to Use a regular expression to check if
        the string contains only alphanumeric characters and spaces
        """
        pattern = r'^[a-zA-Z0-9 ]*$'
        return bool(re.match(pattern, input_string))
