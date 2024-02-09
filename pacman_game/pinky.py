from game_character import GameCharacter
from eyes import Eyes

# Magic number replacement
NUM_ZERO = 0


# The Pinky class extends GameCharacter, so methods defined in GameCharacter
# are inherited by objects of class Pinky.
class Pinky(GameCharacter):
    def __init__(self, maze, pacman, game_controller):
        self.CHAR_WIDTH = 100
        self.CHAR_HEIGHT = 100
        self.maze = maze
        self.pacman = pacman
        self.gc = game_controller
        self.x = maze.LEFT_VERT  # WIDTH/2
        self.y = maze.TOP_HORIZ
        self.velocity = 2
        self.x_add = self.velocity
        self.y_add = 0
        self.eyes = Eyes()
        self.looking = (0, 0)
        self.WIN_PROXIMITY = 80
        self.WALL_TOLERANCE = 2

    def draw_self(self, x, y):
        """Draw Pinky to the screen"""
        noStroke()
        fill(1.0, 0.5, 0.6)
        ellipse(x, y, 100, 100)
        bottom_half = createShape()
        bottom_half.beginShape()
        bottom_half.vertex(x, y)
        bottom_half.vertex(x+100, y)
        bottom_half.vertex(x+100, y+50)
        bottom_half.vertex(x+50, y+25)
        bottom_half.vertex(x, y+50)
        bottom_half.endShape()
        shape(bottom_half, -50, 0)

        self.eyes.display(x, y - 15, self.looking)

    def update(self):
        """Carry out necessary updates for each frame before
        drawing to screen"""
        # Check if Pinky is at an intersection
        on_vert = (
            (abs(self.x - self.maze.LEFT_VERT) < self.WALL_TOLERANCE) or
            (abs(self.x - self.maze.RIGHT_VERT) < self.WALL_TOLERANCE)
                   )
        on_horz = (
            (abs(self.y - self.maze.TOP_HORIZ) < self.WALL_TOLERANCE) or
            (abs(self.y - self.maze.BOTTOM_HORIZ) < self.WALL_TOLERANCE)
                   )

        # Check whether Pinky is up or down/left or right of Pacman
        up_down_part = self.pacman.y - self.y
        left_right_part = self.pacman.x - self.x

        # Update Pinky's eyes to look at Pacman
        self.update_eyes(up_down_part, left_right_part)

        # If Pinky gets close to Pacman, tell the GameController
        # that Pinky wins
        if (abs(up_down_part) < self.WIN_PROXIMITY and
                abs(left_right_part) < self.WIN_PROXIMITY):
            self.gc.pinky_wins = True

        # # Move Pinky
        self.x = self.x + self.x_add
        self.y = self.y + self.y_add

        # TODO:
        # PROBLEM 2: Make Pinky chase Pacman!
        # Study the code above and below these lines to understand how
        # Pinky's movements are calculated, and how Pinky's position with
        # respect to Pacman is represented.
        # Pinky should decide at each intersection whether to go left, right
        # up or down depending on which direction Pacman is further away in.
        # START CODE CHANGES

        # once the Pinky is at an intersection
        if on_vert or on_horz:
            # pacman is under pinky
            if up_down_part > NUM_ZERO:
                # pinky moves down (y increases)
                self.y_add = self.velocity
                self.y = self.y + self.y_add
                # pinky can only walk vertically or horizontally
                self.x_add = NUM_ZERO
            # pacman is above pinky
            elif up_down_part < NUM_ZERO:
                # pinky moves up (y decreases)
                self.y_add = -self.velocity
                self.y = self.y + self.y_add
                self.x_add = NUM_ZERO
            # pacman is on the right
            elif left_right_part > NUM_ZERO:
                # pink moves to the right
                self.x_add = self.velocity
                self.x = self.x + self.x_add
                self.y_add = NUM_ZERO
            # pacman is on the left
            elif left_right_part < NUM_ZERO:
                # pink moves to the left
                self.x_add = -self.velocity
                self.x = self.x + self.x_add
                self.y_add = NUM_ZERO

        # END CODE CHANGES

        # If the player wins, stop Pinky moving
        if self.gc.player_wins:
            self.x_add = 0
            self.y_add = 0

    def update_eyes(self, up_down_part, left_right_part):
        """Set self.looking value based on position of Pinky w/r/t Pacman"""
        if up_down_part and abs(up_down_part) > 5:
            y = up_down_part/abs(up_down_part)
        else:
            y = 0
        if left_right_part and abs(left_right_part) > 5:
            x = left_right_part/abs(left_right_part)
        else:
            x = 0
        self.looking = (x, y)
