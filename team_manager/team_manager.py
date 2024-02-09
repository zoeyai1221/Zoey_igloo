from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            # call a function that calls the appropriate method on the team
            # object to cut the player
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            # call a function to call the necessary bench method to show the
            # names of the players who are currently on the bench.
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    """
    Call the method on team to set team name
    """
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    """
    Call the method on the team object that displays the roster
    """
    team.show_roster()


def do_check_position_filled(team):
    """
    Call the method on the team object that determines
    whether a given position has at least one player filling it
    """
    position = input("What position are you checking for?\n")
    # then print the appropriate message:
    # "Yes, the", position, "position is filled"
    # or
    # "No, the", position, "position is not filled"
    if team.is_position_filled(position):
        print(f"Yes, the {position} position is filled.")
    else:
        print(f"No, the {position} position is not filled.")


def do_add_player_to_team(team):
    """
    Call the method on team that creates a new player and
    adds the player to the team
    """
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    # the if statement here is for checking input
    # in add_player section in Class "Team"
    if team.add_player(player_name, player_number, player_position):
        print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    """
    Call the method on bench to send player to bench
    """
    name = input("Who do you want to send to the bench?\n")
    # make sure that the player is actually on the team first,
    # and then call a method on the bench object to place the player
    # "on the bench". If this is accomplished successfully, print
    # "Sent", name, "to bench."
    # otherwise print
    # name, "isn't on the team."
    if name in [player.name for player in team.players]:
        print("Sent", name, "to bench.")
        bench.send_to_bench(name)
    else:
        print(name, "isn't on the team.")


def do_get_player_from_bench(bench):
    """
    Function to get the best-rested player by name from the bench
    # (i.e. the player who has been on the bench longest)
    """
    # Print to the screen the name of the player who was retrieved
    # from the bench. If the bench is empty, print to the screen that
    # the bench is empty.
    player = bench.get_from_bench()
    if player:
        print("Got", player, "from the bench.")
    else:
        print("The bench is empty.")


def do_cut_player(team, bench):
    """
    Function that calls the method on the team and bench
    object to cut the player
    """
    name = input("Who do you want to cut?\n")
    # if player is currently on bench, do not allow to cut
    if name in bench.players_on_bench:
        print(name, "hasn't been cut for currenlty sitting in bench.")
    else:
        team.cut_player(name)


def do_show_bench(bench):
    """
    Function to call the method on bench to show the
    names of the players who are currently on the bench
    """
    bench.show_bench()


def do_not_understand():
    print("I didn't understand that command")


main()
