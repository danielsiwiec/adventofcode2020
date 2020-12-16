def can_bus_go_generator(buses, timestamp):
    for bus in buses:
        yield can_bus_go(bus, timestamp)


def can_bus_go(bus, timestamp):
    return (timestamp + bus["offset"]) % bus["bus"] == 0


def find_max_bus(buses):
    return max([int(bus) for bus in buses if bus != "x"])

with open("input", "r") as fd:
    lines = fd.read().split("\n")

buses = lines[1].split(",")
max_bus = find_max_bus(buses)

timestamp = -buses.index(str(max_bus))
increment = int(max_bus)

# fast forward
timestamp += (100000000000000 // increment) * increment

buses_with_offsets = [
    {"bus": int(bus), "offset": offset}
    for offset, bus in enumerate(buses)
    if bus != "x"
]

found = False
while not found:
    timestamp += increment
    found = all(can_bus_go_generator(buses_with_offsets, timestamp))

print(timestamp)