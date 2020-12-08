def fetch_instruction(instruction):
    c, n = instruction.split(" ")
    n = int(n)
    return c, n


def console(instruction):
    accum = 0
    i = 0
    instructions_run = []
    finished = False
    while i < len(instruction):
        code, num = fetch_instruction(instruction[i])
        if i in instructions_run:
            return (finished, accum)
        instructions_run.append(i)
        if code == "nop":
            i += 1
            continue
        elif code == "acc":
            accum += num
            i += 1
            continue
        elif code == "jmp":
            i += num
            continue
    finished = True
    return (finished, accum)


def part_two(data):
    for i in range(len(data)):
        code, num = fetch_instruction(data[i])
        result = [False, 0]
        if code == "jmp":
            prog = data.copy()
            prog[i] = f"nop {num}"
            result = console(prog)
        elif code == "nop":
            prog = data.copy()
            prog[i] = f"jmp {num}"
            result = console(prog)
        if result[0]:
            return result


data = []
with open("./input.txt") as f:
    data = f.read().split("\n")
print(f"Part One: {console(data)[1]}")
print(f"Part Two: {part_two(data)}")
