class Runner:
    def __init__(self, instructions):
        self.pointer = 0
        self.history = []
        self.acc = 0
        self.instructions = instructions

    def run(self):
        while self.pointer < len(self.instructions):
            if self.pointer in self.history:
                return (1, self.acc)
            else:
                self.history.append(self.pointer)
                instruction = self.instructions[self.pointer]
                [op, val] = instruction.split(" ")
                if op == "nop":
                    self.pointer += 1
                elif op == "acc":
                    self.pointer += 1
                    self.acc += int(val)
                elif op == "jmp":
                    self.pointer += int(val)
        return (0, self.acc)