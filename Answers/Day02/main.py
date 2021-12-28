with open("input.txt") as f:
    vals = [int(x) for x in f.readlines()]

s1 = s2 = 0
for val in vals:
    # Does not ends with 0
    if val % 10 != 0:
        s1 += val
    tmp = val
    while tmp != 0:
        if tmp % 10 == 0:
            break
        tmp //= 10
    else:
        s2 += val
print(s1, s2)
