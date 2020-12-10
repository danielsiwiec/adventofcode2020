import itertools


def valid(value, preamble):
    return any(
        (a, b) for (a, b) in itertools.combinations(preamble, 2) if a + b == value
    )


preable_size = 25
input = "input"

with open(input, "r") as fd:
    numbers = [int(line) for line in fd.read().split("\n")]

invalid = next(
    value
    for index, value in enumerate(numbers[preable_size:])
    if not valid(value, numbers[index : index + preable_size])
)

# ONE
print(invalid)

# TWO
for start in range(len(numbers)):
    try:
        set = next(
            numbers[start:end]
            for end in range(start + 1, len(numbers))
            if sum(numbers[start:end]) == invalid
        )
        break
    except StopIteration:
        continue

print(min(set) + max(set)) 