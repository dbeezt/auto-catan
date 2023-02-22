import random

class Actor:
    def __init__(self, name, role, colour):
        self.name = name
        self.role = role
        self.colour = colour

class Player(Actor):
    def __init__(self, name, role, colour):
        self.settlements = 5
        self.cities = 4
        self.roads = 15
        self.resources = {"lumber": 0, "grain": 0, "brick": 0, "stone": 0, "sheep": 0}
        self.development_cards = {"knight": 0, "monopoly": 0, "road_building": 0, "victory_point": 0, "year_of_plenty": 0}
        super(Player, self).__init__(name, role, colour)

        def roll():
            return random.randint(1, 12)

        def build():
            pass
        
        def trade():
            pass

        def robbable(resources):
            cards_in_hand = 0
            for resource in resources:
                cards_in_hand += resources[resource]
            if cards_in_hand > 7:
                return True
            return False

class Robber(Actor):
    def __init__(self, name, role, colour):
        self.position = 'tbc'
        super(Player, self).__init__(name, role, colour)

        def rob(player):
            if player.robbable(player.resources):
                pass
            pass