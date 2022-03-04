with open("input.txt") as f:
    steps = f.read().split("\n")

s1, s2 = 20202, 110283739274082

x, y = 0, 0
for i in range(s1):
    step = steps[i % len(steps)]
    if step == "U":
        y += 1
    if step == "D":
        y -= 1
    if step == "R":
        x += 1
    if step == "L":
        x -= 1
print(x, y, abs(x) + abs(y))


baseX, baseY = 0, 0
for step in steps:
    if step == "U":
        baseY += 1
    if step == "D":
        baseY -= 1
    if step == "R":
        baseX += 1
    if step == "L":
        baseX -= 1
x, y = baseX * s2 // len(steps), baseY * s2 // len(steps)

for i in range(s2 % len(steps)):
    step = steps[i]
    if step == "U":
        y += 1
    if step == "D":
        y -= 1
    if step == "R":
        x += 1
    if step == "L":
        x -= 1

print(x, y, abs(x) + abs(y))