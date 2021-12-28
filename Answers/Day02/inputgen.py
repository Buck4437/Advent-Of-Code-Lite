import random

random.seed(349734922020)

with open("input.txt", "w") as f:
    prev = set()
    for i in range(1000):
        while True:
            num = random.randrange(10000, 99999)
            if num not in prev:
                prev.add(num)
                break
        f.write(str(num) + "\n")
