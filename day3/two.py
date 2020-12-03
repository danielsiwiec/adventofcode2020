from map import Map
from navigator import Navigator
from functools import reduce

map = Map()
step = (1, 3)

steps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

navigators = [Navigator(map, *step) for step in steps]

trees_hit_multiplication = reduce(lambda x,y: x*y, [navigator.traverse() for navigator in navigators])

print(trees_hit_multiplication)