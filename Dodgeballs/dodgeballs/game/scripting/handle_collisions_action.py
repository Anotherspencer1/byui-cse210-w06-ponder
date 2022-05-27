import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color
import math

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the player collides
    with a dodgeball

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_dodgeball_collision(cast)
            self._handle_game_over(cast)

    def _handle_dodgeball_collision(self, cast):
        dodgeballs = cast.get_actors("dodgeballs")
        player = cast.get_first_actor("players")

        for dodgeball in dodgeballs:
            dodgeball_point = dodgeball.get_position()
            player_point = player.get_position()
            dodgeball_distance = dodgeball.get_font_size() + 10
            
            if math.dist([dodgeball_point.get_x(), dodgeball_point.get_y()],
                         [player_point.get_x(), player_point.get_y()]) < dodgeball_distance:
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message if player loses, or adds points if player is still alive.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
        else:
            score = cast.get_first_actor("scores")
            score.add_points(1)
