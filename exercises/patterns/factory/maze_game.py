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
    room1 = Room(1)
    room2 = Room(2)
    thedoor = Door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, thedoor)
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, Wall())

    room2.set_side(Direction.NORTH, Wall())
    room2.set_side(Direction.EAST, Wall())
    room2.set_side(Direction.SOUTH, Wall())
    room2.set_side(Direction.WEST, thedoor)
    # TODO - implement this method!
    return maze


def create_enchanted_maze():
    """Series of operations which create our Maze."""
    maze = Maze()
    room1 = EnchantedRoom(1)
    room2 = EnchantedRoom(2)
    themagicdoor = EnchantedDoor(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, themagicdoor)
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, Wall())

    room2.set_side(Direction.NORTH, Wall())
    room2.set_side(Direction.EAST, Wall())
    room2.set_side(Direction.SOUTH, Wall())
    room2.set_side(Direction.WEST, themagicdoor)

    return maze

# these are the ones we care the most about!
def create_factory_maze_type_a(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    thedoor = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, thedoor)
    room1.set_side(Direction.SOUTH, factory.make_wall())
    room1.set_side(Direction.WEST, factory.make_wall())
    return maze


def create_factory_maze_type_b(factory):
    """Series of operations which create our Maze."""

    enchanted_maze = factory.make_maze()
    room1 = EnchantedRoom(1, "Wingardium Leviosa")
    room2 = EnchantedRoom(2, "Confundus")
    room3 = EnchantedRoom(3, "Expelliarmus")
    themagicdoor = EnchantedDoor(room1, room2)

    enchanted_maze.add_room(room1)
    enchanted_maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, Wall())
    room1.set_side(Direction.SOUTH, themagicdoor)
    room1.set_side(Direction.WEST, Wall())

    return enchanted_maze
    # TODO - implement this method!

if __name__ == "__main__":

    # tinker here?

    pass

