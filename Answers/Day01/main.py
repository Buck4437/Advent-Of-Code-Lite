with open("Day01.txt") as f:
    fts = [int(x) for x in f.readlines()]

print(sum(fts))

sm = el = 0
for f in fts:
    sm += f
    if sm % 10 == 0:
        el += 1
        sm //= 10
print(sm * el)
