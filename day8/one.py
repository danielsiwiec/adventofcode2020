from runner import Runner

with open("input", "r") as fd:
    instructions = fd.read().split("\n")

runner = Runner(instructions)
(exit_code, acc) = runner.run()
print(acc)