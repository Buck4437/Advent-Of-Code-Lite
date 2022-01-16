import random

random.seed(442110)


cmds = []
dashes = random.randrange(50, 1001 - 550)
cmds += [">>"] * dashes
front = random.randrange(50, 1000 - len(cmds) + 1 - 100)
cmds += [">"] * front
backdashes = random.randrange(50, 1000 - len(cmds) + 1 - 50)
cmds += ["<<"] * backdashes
back = 1000 - len(cmds)
cmds += ["<"] * back
print(dashes, front, backdashes, back, len(cmds))

random.shuffle(cmds)
with open("input.txt", "w") as f:
    for cmd in cmds:
        f.write(cmd + "\n")