import re
from functools import reduce


def extract_bags(str):
    m = re.match("(\w* \w*) bags contain", str)
    uber_bag = m.group(1)
    bags = {m.group(2): int(m.group(1)) for m in re.finditer("(\d+) (\w* \w*) bag", str)}
    return {uber_bag: bags}


def count_bags(bags_dict, bag, count=0):
    if bag in bags_dict:
        for a_bag, inner_count in bags_dict[bag].items():
            count += inner_count * count_bags(bags_dict, a_bag, 1)
        return count
    else:
        return count


with open("input", "r") as fd:
    lines = fd.read().split("\n")

bags_dicts = [extract_bags(line) for line in lines]
bags_dict = reduce(lambda d1,d2: dict(d1, **d2), bags_dicts)

count = count_bags(bags_dict, "shiny gold")
print(count)
