import pyray
import constants
import random
from game.shared.point import Point


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor, centered)
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)

    def draw_polygons(self, actors):
        for actor in actors:
            self.draw_polygon(actor)
    
    def draw_polygon(self, actor):
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        vector2 = (x, y)
        color = actor.get_color().to_tuple()
        radius = actor.get_font_size()
            
        pyray.draw_poly(vector2, 5, radius, 0.0, color)

    def draw_triangle(self, actor):
        player = actor
        center = actor.get_position()
        center_x = center.get_x()
        center_y = center.get_y()
        velocity = actor.get_velocity()
        state = player.get_player_state()
        color = actor.get_color().to_tuple()
        if state.equals(Point(0, 0)):
            v1 = (center_x + 10, center_y + 10)
            v2 = (center_x, center_y - 15)
            v3 = (center_x - 10, center_y + 10)
        elif state.equals(Point(0, 10)):
            v1 = (center_x - 10, center_y - 10)
            v2 = (center_x, center_y + 15)
            v3 = (center_x + 10, center_y - 10)
        elif state.equals(Point(0, -10)):
            v1 = (center_x + 10, center_y + 10)
            v2 = (center_x, center_y - 15)
            v3 = (center_x - 10, center_y + 10)
        elif state.equals(Point(10, 0)):
            v1 = (center_x - 10, center_y + 10)
            v2 = (center_x + 15, center_y)
            v3 = (center_x - 10, center_y - 10)
        elif state.equals(Point(-10, 0)):
            v1 = (center_x + 10, center_y - 10)
            v2 = (center_x - 15, center_y)
            v3 = (center_x + 10, center_y + 10)
        elif state.equals(Point(-10, -10)):
            v1 = (center_x - 17, center_y - 17)
            v2 = (center_x, center_y + 8)
            v3 = (center_x + 10, center_y - 10)
        elif state.equals(Point(10, 10)):
            v1 = (center_x + 17, center_y + 17)
            v2 = (center_x, center_y - 8)
            v3 = (center_x - 10, center_y + 10)
        elif state.equals(Point(10, -10)):
            v1 = (center_x + 17, center_y - 17)
            v2 = (center_x - 10, center_y - 10)
            v3 = (center_x, center_y + 8)
        elif state.equals(Point(-10, 10)):
            v2 = (center_x - 17, center_y + 17)
            v1 = (center_x, center_y - 8)
            v3 = (center_x + 10, center_y + 10)
        else:
            v1 = (center_x + 10, center_y + 10)
            v2 = (center_x, center_y - 10)
            v3 = (center_x - 10, center_y + 10)
        
        pyray.draw_triangle(v1, v2, v3, color)