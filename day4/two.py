import re

required_fileds = [
    {
        "pattern": "byr:(\d{4})",
        "value": lambda match: int(match.group(1)) <= 2002
        and int(match.group(1)) >= 1920,
    },
    {
        "pattern": "iyr:(\d{4})",
        "value": lambda match: int(match.group(1)) <= 2020
        and int(match.group(1)) >= 2010,
    },
    {
        "pattern": "eyr:(\d{4})",
        "value": lambda match: int(match.group(1)) <= 2030
        and int(match.group(1)) >= 2020,
    },
    {
        "pattern": "hgt:(\d+)(cm|in)",
        "value": lambda match: int(match.group(1)) >= 150 and int(match.group(1)) <= 193
        if match.group(2) == "cm"
        else (
            int(match.group(1)) >= 59 and int(match.group(1)) <= 76
            if match.group(2) == "in"
            else False
        ),
    },
    {"pattern": "hcl:#[0-9a-f]{6}"},
    {"pattern": "ecl:(amb|blu|brn|gry|grn|hzl|oth)"},
    {"pattern": "pid:\d{9}(?!\d)"},
]


def matches(passport, field):
    match = re.search(field["pattern"], passport)
    print(passport)
    print(field["pattern"])
    print(match)
    return match and (field["value"](match) if "value" in field else True)


def is_valid(passport):
    return all(matches(passport, field) for field in required_fileds)


with open("input", "r") as fd:
    passports = fd.read().split("\n\n")

valid = [passport for passport in passports if is_valid(passport)]
print(len(valid))