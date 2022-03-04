import random

random.seed(59729)

directions = []

for i in range(340):
    directions.append("U")

for i in range(126):
    directions.append("D")

for i in range(397):
    directions.append("R")

for i in range(1000 - 340 - 126 - 397):
    directions.append("L")

random.shuffle(directions)

with open("input.txt", "w") as f:
    f.write(directions[0])
    for direction in directions[1:]:
        f.write("\n" + direction)
