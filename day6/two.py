def all_yes(group_answers):
    answers = group_answers.split('\n')
    return [ letter for letter in answers[0] if all(letter in answer for answer in answers) ]


with open("input", "r") as fd:
    groups = fd.read().split("\n\n")

all_yeses = [all_yes(answers) for answers in groups]
counts = [len(unique_answers) for unique_answers in all_yeses]

print(sum(counts))
