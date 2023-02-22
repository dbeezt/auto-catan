import numpy

class Board:
    def __init__(self, size):
        self.resources = {"lumber": 4, "grain": 4, "brick": 3, "stone": 3, "sheep": 4, "desert": 1}

        self.map = [
            [Hex, Hex, Hex],
            [Hex, Hex, Hex, Hex],
            [Hex, Hex, Hex, Hex, Hex],
            [Hex, Hex, Hex, Hex],
            [Hex, Hex, Hex]
        ]

        def setup():
            pass

class Hex:
    def __init__(self, resource):
        self.resource = resource
        self.n = ""
        self.ne = ""
        self.se = ""
        self.s = ""
        self.sw = ""
        self.nw = ""

class Structure:
    def __init__(self, type, owner):
        self.resource = type
        self.owner = owner