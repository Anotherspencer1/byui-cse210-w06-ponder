import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlPlayer1sAction(Action):
    """
    An input action that controls the player.
    
    The responsibility of ControlActorsAction is to get the direction and move the players head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)
        self._x = 0
        self._y = 0

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player = cast.get_first_actor("players")
        
        # left
        if self._keyboard_service.is_key_down('a'):
            #self._direction = Point(-constants.CELL_SIZE, 0)
            self._x -= 10


        # right
        if self._keyboard_service.is_key_down('d'):
            #self._direction = Point(constants.CELL_SIZE, 0)
            self._x += 10
        
        # up
        if self._keyboard_service.is_key_down('w'):
            #self._direction = Point(0, -constants.CELL_SIZE)
            self._y -= 10
        
        # down
        if self._keyboard_service.is_key_down('s'):
            #self._direction = Point(0, constants.CELL_SIZE)
            self._y += 10

        self._direction = Point(self._x, self._y)

        
        player.turn_head(self._direction)
        if self._direction.equals(Point(0, 0)):
            return
        else:
            player.set_player_state(self._direction)
        self._x = 0
        self._y = 0