import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Player(Actor):
    """
    The player.

    Creates the player and handles player state to control direction player faces.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new player."
        super().__init__()
        self.set_color(constants.WHITE)
        self.set_font_size(20)
        self.set_text = "O"
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        self.position = Point(x, y)
        self.set_position(self.position)
        self.player_state = Point(0, 0)
    
    def turn_head(self, velocity):
        self.set_velocity(velocity)

    def set_player_state(self, state):
        self.player_state = state

    def get_player_state(self):
        return self.player_state

