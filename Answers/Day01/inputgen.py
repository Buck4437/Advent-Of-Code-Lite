import random

random.seed(349843094)

with open("Day01.txt", "w") as f:
    for i in range(1000):
        f.write(str(random.randrange(1, 10)) + "\n")
