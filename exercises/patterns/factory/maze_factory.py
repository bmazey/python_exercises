# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.maze import Maze
from exercises.patterns.factory.wall import Wall
from exercises.patterns.factory.room import Room
from exercises.patterns.factory.door import Door
from exercises.patterns.factory.direction import Direction



class MazeFactory(object):

    """Factory producing basic Maze."""

    @staticmethod
    def make_maze():
        return Maze()

    @staticmethod
    def make_wall():
        return Wall()

    @staticmethod
    def make_room(room_number):
        return Room(room_number)

    @staticmethod
    def make_door(room1, room2):
        return Door(room1, room2)

    def create_room(self, wallDirection, wallDirection2, wallDirection3, doorDirection, roomNum, factory, roomNum2):
        room1 = Room(roomNum)
        room2 = Room(roomNum2)
        room1.set_side(Direction.wallDirection, factory.make_wall())
        room1.set_side(Direction.wallDirection2, factory.make_wall())
        room1.set_side(Direction.wallDirection3, factory.make_wall())
        room1.set_side(Direction.doorDirection, factory.make_door(room1, room2))
