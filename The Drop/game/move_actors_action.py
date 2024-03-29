from game import constants
from game.action import Action
from game.point import Point


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast, delta_time):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if cast["synchronizer"][0].is_synchronized():
            for group in cast.values():
                for actor in group:
                    # It would be nice to add something to a base Actor class
                    # to detect is_zero()...
                    # if not actor.get_velocity().is_zero():

                    # If zeros are falsey, might be able to replace this with
                    # if not(actorx and actory)
                    if actor.change_y or actor.change_x:
                        self._move_actor(actor, delta_time)
        else:
            cast["synchronizer"][0].synchronize()

    def _move_actor(self, actor, delta_time):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.

        Args:
            actor (Actor): The actor to move.
        """

        actor.center_x = actor.center_x + actor.change_x * delta_time
        actor.center_y = actor.center_y + actor.change_y * delta_time