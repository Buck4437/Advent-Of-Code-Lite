with open("input.txt") as f:
    cmds = [s.strip() for s in f.readlines()]

x = x2 = y2 = 0

for cmd in cmds:
    if cmd == ">":
        x += 1
        x2 += 1
    elif cmd == ">>":
        x += 5
        y2 += 1
    elif cmd == "<":
        x -= 1
        x2 -= 1
    elif cmd == "<<":
        x -= 5
        y2 -= 1

print(x, x2, y2)
print(abs(x), abs(x2) + abs(y2) * 1000)
