import constants

from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.dodgeball import Dodgeball
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_player1s_action import ControlPlayer1sAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    
    #cast.add_actor("cycles", Cycle(2))
    cast.add_actor("players", Player())
    cast.add_actor("scores", Score())
    for i in range(constants.DODGEBALLS):
        cast.add_actor("dodgeballs", Dodgeball())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlPlayer1sAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()