import random

class Board:
    def __init__(self):
        # Can work out non-random board setup later. Random's good for now.
        self.resources = { "wood": 4, "grain": 4, "brick": 3, "stone": 3, "sheep": 4, "desert": 1 }
        self.numbers = {"2": 1, "3": 2, "4": 2, "5": 2, "6": 2, "8": 2, "9": 2, "10": 2, "11": 2, "12": 1 }

        #       |   |   |
        #     |   |   |   |
        #   |   |   |   |   |
        # |   |   |   |   |   |
        #   |   |   |   |   |
        #     |   |   |   |
        #       |   |   |
        self.map = [
                ['', '', ''],
              ['', '', '', ''],
            ['', '', '', '', ''],
              ['', '', '', ''],
                ['', '', '']
        ]

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                resource, number = self.populate_hex()
                self.map[row][col] = Hex(resource, number)

    def setup(self):
        return self.map

    def retrieve_random_and_pop(self, a_dict):
        # List because of "DeprecationWarning: Sampling from a set deprecated since Python 3.9 and will be removed in a subsequent version."
        element = random.sample(list(a_dict.keys()), 1)[0]
        a_dict[element] -= 1
        if a_dict[element] == 0: 
            a_dict.pop(element) 
        return element

    def populate_hex(self):
        resource = self.retrieve_random_and_pop(self.resources)
        if resource == 'desert': 
            number = 7
        else: 
            number = self.retrieve_random_and_pop(self.numbers)
        return resource, number

    def build_structure(self, location, structure):
        location = structure
        
# Might need half hex tile for ports/edges
class Hex:
    def __init__(self, resource, number):
        self.resource = resource
        self.number = number
        # instead of nesw, should it be coord-based?
        self.n = ""
        self.ne = ""
        self.se = ""
        self.s = ""
        self.sw = ""
        self.nw = ""

    def build(self, location, structure):
        pass

# this needs to be a separate file maybe
class Structure:
    def __init__(self, structure, owner):
        self.structure = structure
        # owner can be players or bank (for port)?
        self.owner = owner

# when building structures, need to check if there are any parallel hex edges to update simultaneously

class Port(Structure):
    def __init__(self, resource):
        self.resource = resource
        super(Port, self).__init__('port', self.owner)

    def trade(self, resource, amount):
        if self.resource == resource:
            print("trading")
        else:
            print("not trading")

        return (resource/2)

class Settlement(Structure):
    def __init__(self, owner):
        # {"wood": 1, "grain": 1, "brick": 1, "sheep": 1}
        self.owner = owner
        super(Settlement, self).__init__('settlement', self.owner)

class City(Structure):
    def __init__(self, owner):
        # {"grain": 2, "stone": 3}
        self.owner = owner
        super(City, self).__init__('city', self.owner)

class Road(Structure):
    def __init__(self, owner):
        # {"wood": 1, "brick": 1}
        self.owner = owner
        super(Port, self).__init__('road', self.owner)


board = Board()
print(f"""       
             |{board.map[0][0].resource[:2]}|{board.map[0][1].resource[:2]}|{board.map[0][2].resource[:2]}|
           |{board.map[1][0].resource[:2]}|{board.map[1][1].resource[:2]}|{board.map[1][2].resource[:2]}|{board.map[1][3].resource[:2]}|
         |{board.map[2][0].resource[:2]}|{board.map[2][1].resource[:2]}|{board.map[2][2].resource[:2]}|{board.map[2][3].resource[:2]}|{board.map[2][4].resource[:2]}|
           |{board.map[3][0].resource[:2]}|{board.map[3][1].resource[:2]}|{board.map[3][2].resource[:2]}|{board.map[3][3].resource[:2]}|
             |{board.map[4][0].resource[:2]}|{board.map[4][1].resource[:2]}|{board.map[4][2].resource[:2]}|
    """)

# board.build_structure(board.map[0][0].n, City('dan'))
board.map[0][0].n = City('dan')
print(board.map[0][0].n.structure)


