# 5 species (fox, elk, salmon, bear, hawk)
# 5 habitats (forest, deserts, mountains, plains, river)


import random
import networkx
from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import List
from typing import Optional


class Biome(Enum):
    TREE = auto()
    DESERT = auto()
    MOUNTAIN = auto()
    PLAIN = auto()
    RIVER = auto()

    def __str__(self):
        return self.name


class Animal(Enum):
    FOX = auto()
    ELK = auto()
    SALMON = auto()
    BEAR = auto()
    HAWK = auto()

    def __str__(self):
        return self.name


@dataclass
class Tile:
    biomes: List[Biome]
    animals: List[Animal]
    token: Optional[Animal] = None

    def __eq__(self, other):
        return all([
            self.biomes == other.biomes,
            self.animals == other.animals,
            self.token == other.token,
        ])

    def __hash__(self):
        return hash(
            tuple(tuple(x) if isinstance(x, list) else x)
            for x in [self.biomes, self.animals, self.token]
        )


class Board:
    def __init__(self, starting_graph):
        self.starting_graph = starting_graph



t = Biome.TREE
d = Biome.DESERT
m = Biome.MOUNTAIN
p = Biome.PLAIN
r = Biome.RIVER

f = Animal.FOX
e = Animal.ELK
s = Animal.SALMON
b = Animal.BEAR
h = Animal.HAWK


#t1 = Tile(biomes=[r], animals=[s])
#t2 = Tile(biomes=[d, t], animals=[s, e, b])
#t3 = Tile(biomes=[p, m], animals=[f, h])
#
#
#g = networkx.Graph()
#g.add_edge(t1, t2)
#g.add_edge(t2, t3)
#g.add_edge(t3, t1)



t1 = "R"
t2 = "PM"
t3 = "DT"


class Arrangement:

    def __init__(self):
        self.num = 0
        self.ids = {}

    def _id(self, t):
        if t not in self.ids:
            self.ids[t] = self.num
            self.num += 1
        return self.ids[t]

    def connect(t1, t2, edge_pairing):
        t1id = self._id(t1)
        t2id = self._id(t2)
        return (t1id, t2id)

    def set_token(t, animal):
        pass

    def animal_groups(animal):
        pass

    def terrain_groups(terrain):
        pass


# q.connect(t1, t2, "RM")
# q.connect(t2, t3, "TP")
# q.connect(t3, t1, "DR")
#
# q.token(t1, "H")
#
# q.animal_groups("H")
#
# q.terrain_groups("R")





game = {
    "players": [
        {
            "graph": graph1,
            "groups": {
                "fox": [],
                "hawk": [],
                "bear": [],
                "salmon": [],
                "elk": [],
            },
            "corridors": {
                "tree": [],
                "desert": [],
                "mountain": [],
                "plain": [],
                "river": [],
            },
            "tokens": 0,
        },
        {
            "graph": graph2,
            "groups": {
                "fox": [],
                "hawk": [],
                "bear": [],
                "salmon": [],
                "elk": [],
            },
            "corridors": {
                "tree": [],
                "desert": [],
                "mountain": [],
                "plain": [],
                "river": [],
            },
            "tokens": 0,
        },
    ],
}



