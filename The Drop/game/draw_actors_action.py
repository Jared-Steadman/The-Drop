from game.action import Action
from game import constants

import arcade


class DrawActorsAction(Action):
    """A code template for drawing actors.

    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.

        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        arcade.draw_lrwh_rectangle_textured(0, 0,constants.MAX_X,constants.MAX_Y,arcade.load_texture(constants.GAME_BACKGROUND))
        

        beats = cast["beats"]
        beats = beats[-35:]
        self._output_service.draw_actors(beats)

        players = cast["player"]
        self._output_service.draw_actors(players)
            
        drop_points = cast["drop_points"]
        self._output_service.draw_actors(drop_points)

        synchronizers = cast["synchronizer"]
        self._output_service.draw_actors(synchronizers)

        self._output_service.flush_buffer()