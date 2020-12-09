from runner import Runner

with open("input", "r") as fd:
    instructions = fd.read().split("\n")

for position, instruction in enumerate(instructions):
    [op, val] = instruction.split(' ')
    if op == 'nop':
        copy = instructions.copy()
        copy[position] = 'jmp' + ' ' + str(val)
        runner = Runner(copy)
        (exit_code, acc) = runner.run()
        if exit_code == 0:
            break
    elif op == 'jmp':
        copy = instructions.copy()
        copy[position] = 'nop' + ' ' + str(val)
        runner = Runner(copy)
        (exit_code, acc) = runner.run()
        if exit_code == 0:
            break
print(f'exit code: {exit_code}, acc: {acc}')