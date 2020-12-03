# Part 1
with open('p02.txt') as f:
    for line in f:
        prog = [int(x) for x in line.split(',')]
        break


prog[1] = 12
prog[2] = 2

pos = 0

while True:
    opcode = prog[pos]

    if opcode == 99:
        break

    pos1, pos2, pos3 = prog[pos+1:pos+4]

    if opcode == 1:
        res = prog[pos1] + prog[pos2]
    if opcode == 2:
        res = prog[pos1] * prog[pos2]

    prog[pos3] = res

    pos += 4

print(prog[0])

# Part 2
with open('p02.txt') as f:
    for line in f:
        prog = [int(x) for x in line.split(',')]
        break


def exe(prog, noun, verb):
    pos, prog[1], prog[2] = 0, noun, verb

    while True:
        opcode = prog[pos]

        if opcode == 99:
            break

        pos1, pos2, pos3 = prog[pos+1:pos+4]

        if opcode == 1:
            res = prog[pos1] + prog[pos2]
        if opcode == 2:
            res = prog[pos1] * prog[pos2]

        prog[pos3] = res

        pos += 4

    return prog[0]


for n in range(100):
    for v in range(100):
        res = exe(list(prog), n, v)

        if res == 19690720:
            print(100 * n + v)
            break