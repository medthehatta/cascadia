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

    def __repr__(self):
        return self.name


class Animal(Enum):
    FOX = auto()
    ELK = auto()
    SALMON = auto()
    BEAR = auto()
    HAWK = auto()

    def __repr__(self):
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


t1 = Tile(biomes=[r], animals=[s])
t2 = Tile(biomes=[d, t], animals=[s, e, b])
t3 = Tile(biomes=[p, m], animals=[f, h])


g = networkx.Graph()
g.add_edge(t1, t2)
g.add_edge(t2, t3)
g.add_edge(t3, t1)

