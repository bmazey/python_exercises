# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.maze import Maze
from exercises.patterns.factory.direction import Direction
from exercises.patterns.factory.room import Room
from exercises.patterns.factory.door import Door
from exercises.patterns.factory.wall import Wall
from exercises.patterns.factory.player import Player
from exercises.patterns.factory.wizard import Wizard
from exercises.patterns.factory.enchanted_room import EnchantedRoom
from exercises.patterns.factory.enchanted_door import EnchantedDoor
from exercises.patterns.factory.maze_factory import MazeFactory
from exercises.patterns.factory.enchanted_maze_factory import EnchantedMazeFactory


def create_maze():
    """Series of operations which create our Maze."""
    maze = Maze()

    # TODO - implement this method!

    return maze


def create_enchanted_maze():
    """Series of operations which create our Maze."""
    maze = Maze()

    # TODO - implement this method!

    return maze


# these are the ones we care the most about!
def create_factory_maze_type_a(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = Room(1)
    room2 = Room(2)
    the_door = Door(room1, room2)
    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.EAST, the_door)

    # TODO - implement this method!

    return maze


def create_factory_maze_type_b(factory):
    """Series of operations which create our Maze."""
    maze = factory.make_maze()
    room1 = Room(1)
    room2 = Room(2)
    the_door = Door(room1, room2)
    maze.add_room(room1)
    maze.add_room(room2)
    room1.set_side(Direction.SOUTH, the_door)

    # TODO - implement this method!

    return maze


if __name__ == "__main__":

    # tinker here?

    pass

