from map import Map
from navigator import Navigator

map = Map()
step = (1, 3)
navigator = Navigator(map, *step)

trees_hit = navigator.traverse()

print(trees_hit)