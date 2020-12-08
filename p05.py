# Part 1
with open('p05.txt') as f:
    prog = [int(x) for x in f.read().split(',')]


def parse(i):
    i = str(i)
    opcode = int(i[-1])
    mode1 = int(i[-3]) if len(i) > 2 else 0
    mode2 = int(i[-4]) if len(i) > 3 else 0

    return opcode, mode1, mode2


def read(op, mode):
    return prog[op] if mode == 0 else op


pos, input_ = 0, 1

while prog[pos] != 99:
    opcode, mode1, mode2 = parse(prog[pos])

    if opcode == 1:
        param1, param2, param3 = prog[pos + 1], prog[pos + 2], prog[pos + 3]
        prog[param3] = read(param1, mode1) + read(param2, mode2)
        pos += 4
    elif opcode == 2:
        param1, param2, param3 = prog[pos + 1], prog[pos + 2], prog[pos + 3]
        prog[param3] = read(param1, mode1) * read(param2, mode2)
        pos += 4
    elif opcode == 3:
        prog[prog[pos + 1]] = input_
        pos += 2
    elif opcode == 4:
        val = read(prog[pos + 1], mode1)
        print(val)
        pos += 2

# Part 2
with open('p05.txt') as f:
    prog = [int(x) for x in f.read().split(',')]

pos, input_ = 0, 5

while prog[pos] != 99:
    opcode, mode1, mode2 = parse(prog[pos])
    param1, param2, param3 = prog[pos + 1], prog[pos + 2], prog[pos + 3]

    if opcode == 1:
        prog[param3] = read(param1, mode1) + read(param2, mode2)
        pos += 4
    elif opcode == 2:
        prog[param3] = read(param1, mode1) * read(param2, mode2)
        pos += 4
    elif opcode == 3:
        prog[param1] = input_
        pos += 2
    elif opcode == 4:
        val = read(param1, mode1)
        print(val)
        pos += 2
    elif opcode == 5:
        if read(param1, mode1) != 0:
            pos = read(param2, mode2)
        else:
            pos += 3
    elif opcode == 6:
        if read(param1, mode1) == 0:
            pos = read(param2, mode2)
        else:
            pos += 3
    elif opcode == 7:
        prog[param3] = 1 if read(param1, mode1) < read(param2, mode2) else 0
        pos += 4
    elif opcode == 8:
        prog[param3] = 1 if read(param1, mode1) == read(param2, mode2) else 0
        pos += 4
