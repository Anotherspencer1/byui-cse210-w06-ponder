import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Dodgeball(Actor):
    """
    A dodgeball that the player needs to avoid.

    This class creates red dodgeballs at random positions, sizes, and velocities.
    """
    def __init__(self):
        "Constructs a new dodgeball."
        super().__init__()
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position, size, and velocity"""
        x = random.randint(1, constants.COLUMNS - 1)
        y = 1
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_font_size(random.randint(10, 20))
        self.set_velocity(Point(random.randint(-3, 3), random.randint(5, 15)))
        self.set_position(position)
