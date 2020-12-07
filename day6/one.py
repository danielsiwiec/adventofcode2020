def unique(answers):
    return {answer for answer in answers.replace("\n", "")}


with open("input", "r") as fd:
    groups = fd.read().split("\n\n")

uniques = [unique(answers) for answers in groups]
unique_counts = [len(unique_answers) for unique_answers in uniques]

print(sum(unique_counts))
