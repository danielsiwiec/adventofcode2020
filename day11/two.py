with open("input", "r") as fd:
    rows = fd.read().split("\n")


def is_occupied(row, col, map):
    if row >= 0 and row < len(map) and col >= 0 and col < len(map[0]):
        return map[row][col] == "#"
    else:
        return False


def visible_index_in_direction(row, col, direction, map):
    while True:
        (row, col) = [sum(x) for x in zip((row, col), direction)]
        if row >= 0 and row < len(map) and col >= 0 and col < len(map[0]):
            if map[row][col] != ".":
                return (row, col)
        else:
            return (row, col)


def visible_indices(row, col, map):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [
        visible_index_in_direction(row, col, direction, map) for direction in directions
    ]


def no_adjacent_occupied(row, col, map):
    indices = visible_indices(row, col, map)
    return len([index for index in indices if is_occupied(*index, map)]) == 0


def four_adjacent_occupied(row, col, map):
    indices = visible_indices(row, col, map)
    return len([index for index in indices if is_occupied(*index, map)]) >= 5


def transition_seat(row, col, map):
    if map[row][col] == ".":
        return "."
    elif no_adjacent_occupied(row, col, map):
        return "#"
    elif four_adjacent_occupied(row, col, map):
        return "L"
    else:
        return map[row][col]


def transition(current_map):
    new_map = []
    for row_num, row in enumerate(current_map):
        new_map.append(
            [
                transition_seat(row_num, col_num, current_map)
                for col_num, _ in enumerate(row)
            ]
        )
    # print_map(new_map)
    return new_map


def print_map(map):
    for row in map:
        print("".join(row))
    print("\n\n")


# test_map = [".............", ".L.L.#.#.#.#.", "............."]
# print(visible_index_in_direction(1, 1, (0, 1), test_map))

previous = rows
while True:
    new = transition(previous)
    if str(previous) == str(new):
        break
    previous = new

print("Finished")
print(len([seat for seat in str(previous) if seat == "#"]))