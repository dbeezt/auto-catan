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
        
# Might need half hex tile for ports/edges
class Hex:
    def __init__(self, resource, number):
        self.resource = resource
        self.number = number
        self.n = ""
        self.ne = ""
        self.se = ""
        self.s = ""
        self.sw = ""
        self.nw = ""

# this needs to be a separate file maybe
class Structure:
    def __init__(self, type, owner):
        self.type = type
        self.owner = owner


board = Board()
print(f"""       
             |{board.map[0][0].resource[:2]}|{board.map[0][1].resource[:2]}|{board.map[0][2].resource[:2]}|
           |{board.map[1][0].resource[:2]}|{board.map[1][1].resource[:2]}|{board.map[1][2].resource[:2]}|{board.map[1][3].resource[:2]}|
         |{board.map[2][0].resource[:2]}|{board.map[2][1].resource[:2]}|{board.map[2][2].resource[:2]}|{board.map[2][3].resource[:2]}|{board.map[2][4].resource[:2]}|
           |{board.map[3][0].resource[:2]}|{board.map[3][1].resource[:2]}|{board.map[3][2].resource[:2]}|{board.map[3][3].resource[:2]}|
             |{board.map[4][0].resource[:2]}|{board.map[4][1].resource[:2]}|{board.map[4][2].resource[:2]}|
    """)
# print(Board().map)


