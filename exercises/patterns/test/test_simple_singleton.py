# TODO - figure out how to test singleton :D
from exercises.patterns.singleton.simple_singleton import Logger


def test_singleton():
    s1 = Logger()
    s2 = Logger()
    assert id(s1) == id(s2)

