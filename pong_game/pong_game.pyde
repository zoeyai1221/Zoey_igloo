import subprocess
from random import choice

# Constants
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
BALL_SIZE = 20
PADDLE_SPEED = 8
BALL_SPEED_X = 6
BALL_SPEED_Y = 6
WINNING_SCORE = 1

# Numeric Constants
TWO = 2
ONE = 1
ZERO = 0
NEGATIVE_ONE = -1
THREE = 3
FOUR = 4

# Variables
player1_score = ZERO
player2_score = ZERO
ball_x = WIDTH / TWO
ball_y = HEIGHT / TWO
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
player1_y = HEIGHT / TWO
player2_y = HEIGHT / TWO

# Sound file paths
ball_hit_sound = "path_to_ball_hit_sound.wav"
score_sound = "path_to_score_sound.wav"

# Variables to store key states
up_key_pressed = False
down_key_pressed = False

# Function to play sound
def play_sound(sound_file):
    """
    Plays the specified sound file.

    Args:
    sound_file (str): Path to the sound file.
    """
    subprocess.Popen(["afplay", sound_file])  # For macOS
    # For Windows, you might use: subprocess.Popen(["start", "path_to_sound_file.wav"], shell=True)

def setup():
    """
    Initializes the game environment.
    """
    size(WIDTH, HEIGHT)
    background(ZERO)  # Set background color to black
    noStroke()
    fill(255)  # Set fill color to white

def draw():
    """
    Main game loop.
    """
    global ball_x, ball_y, ball_speed_x, ball_speed_y, player1_y, player2_y, player1_score, player2_score

    background(ZERO)  # Clear the screen
    draw_paddles()  # Draw the paddles
    draw_ball()  # Draw the ball
    move_ball()  # Move the ball
    handle_player_movement()  # Handle player's paddle movement
    move_player2()  # Move player 2 (computer-controlled paddle)
    check_collision()  # Check collisions between objects
    display_scores()  # Display scores
    check_win()  # Check if there is a winner

def draw_paddles():
    """
    Draws the paddles on the screen.
    """
    rect(ZERO, player1_y - PADDLE_HEIGHT / TWO, PADDLE_WIDTH, PADDLE_HEIGHT)  # Left paddle
    rect(WIDTH - PADDLE_WIDTH, player2_y - PADDLE_HEIGHT / TWO, PADDLE_WIDTH, PADDLE_HEIGHT)  # Right paddle

def draw_ball():
    """
    Draws the ball on the screen.
    """
    ellipse(ball_x, ball_y, BALL_SIZE, BALL_SIZE)  # Draw the ball as a circle

def move_ball():
    """
    Moves the ball based on its speed.
    """
    global ball_x, ball_y

    ball_x += ball_speed_x
    ball_y += ball_speed_y

def handle_player_movement():
    """
    Handles the movement of the player's paddle.
    """
    global player1_y

    if up_key_pressed and player1_y > PADDLE_HEIGHT / TWO:
        player1_y -= PADDLE_SPEED
    elif down_key_pressed and player1_y < HEIGHT - PADDLE_HEIGHT / TWO:
        player1_y += PADDLE_SPEED

def move_player2():
    """
    Implements a simple AI to move player 2 (computer-controlled paddle).
    """
    global player2_y

    if ball_y > player2_y and player2_y < HEIGHT - PADDLE_HEIGHT / TWO:
        player2_y += PADDLE_SPEED
    elif ball_y < player2_y and player2_y > PADDLE_HEIGHT / TWO:
        player2_y -= PADDLE_SPEED

def check_collision():
    """
    Checks for collisions between the ball and paddles/walls, handles scoring.
    """
    global ball_speed_x, ball_speed_y, player1_score, player2_score

    # Collision with paddles
    if (ball_x - BALL_SIZE / TWO <= PADDLE_WIDTH and player1_y - PADDLE_HEIGHT / TWO < ball_y < player1_y + PADDLE_HEIGHT / TWO) or \
       (ball_x + BALL_SIZE / TWO >= WIDTH - PADDLE_WIDTH and player2_y - PADDLE_HEIGHT / TWO < ball_y < player2_y + PADDLE_HEIGHT / TWO):
        ball_speed_x *= NEGATIVE_ONE  # Reverse ball's horizontal direction
        play_sound(ball_hit_sound)

    # Collision with top and bottom walls
    if ball_y - BALL_SIZE / TWO <= ZERO or ball_y + BALL_SIZE / TWO >= HEIGHT:
        ball_speed_y *= NEGATIVE_ONE  # Reverse ball's vertical direction
        play_sound(ball_hit_sound)

    # Scoring
    if ball_x - BALL_SIZE / TWO <= ZERO:
        player2_score += ONE  # Player 2 scores
        play_sound(score_sound)
        reset_ball()
    elif ball_x + BALL_SIZE / TWO >= WIDTH:
        player1_score += ONE  # Player 1 scores
        play_sound(score_sound)
        reset_ball()

def display_scores():
    """
    Displays the scores on the screen.
    """
    textSize(32)
    textAlign(CENTER)
    text(player1_score, WIDTH / FOUR, 50)  # Display player 1's score
    text(player2_score, WIDTH * THREE / FOUR, 50)  # Display player 2's score

def check_win():
    """
    Checks if either player has won the game.
    """
    global player1_score, player2_score

    if player1_score == WINNING_SCORE or player2_score == WINNING_SCORE:
        game_over("Game Over!")  # Display "Game Over!" message

def game_over(message):
    """
    Displays the game over message.

    Args:
    message (str): The game over message to be displayed.
    """
    background(ZERO)  # Clear the screen
    fill(255)  # Set fill color to white
    textSize(50)
    textAlign(CENTER)
    text(message, WIDTH / TWO, HEIGHT / TWO)  # Display game over message
    noLoop()

def reset_ball():
    """
    Resets the ball to the center of the screen with random speed.
    """
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    ball_x = WIDTH / TWO
    ball_y = HEIGHT / TWO
    ball_speed_x = choice([NEGATIVE_ONE * BALL_SPEED_X, BALL_SPEED_X])
    ball_speed_y = choice([NEGATIVE_ONE * BALL_SPEED_Y, BALL_SPEED_Y])

def keyPressed():
    """
    Handles key press events.
    """
    global up_key_pressed, down_key_pressed

    if keyCode == UP:
        up_key_pressed = True
    elif keyCode == DOWN:
        down_key_pressed = True

def keyReleased():
    """
    Handles key release events.
    """
    global up_key_pressed, down_key_pressed

    if keyCode == UP:
        up_key_pressed = False
    elif keyCode == DOWN:
        down_key_pressed = False
