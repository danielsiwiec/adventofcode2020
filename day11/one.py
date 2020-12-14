with open("input", "r") as fd:
    rows = fd.read().split("\n")


def is_occupied(row, col, map):
    if row >= 0 and row < len(map) and col >= 0 and col < len(map[0]):
        return map[row][col] == "#"
    else:
        return False


def adjacent_seats(row, col):
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]


def no_adjacent_occupied(row, col, map):
    indices = adjacent_seats(row, col)
    return len([index for index in indices if is_occupied(*index, map)]) == 0


def four_adjacent_occupied(row, col, map):
    indices = adjacent_seats(row, col)
    return len([index for index in indices if is_occupied(*index, map)]) >= 4


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


previous = rows
while True:
    new = transition(previous)
    if str(previous) == str(new):
        break
    previous = new

print("Finished")
print(len([seat for seat in str(previous) if seat == "#"]))
