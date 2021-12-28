with open("input.txt") as f:
    ins = f.readlines()

pt1 = val = 0
for i in ins:
    i = i.strip()
    if i == "out":
        print(chr(val), end="")
    elif i == "inc":
        val += 1
        pt1 += 1
    elif i == "dec":
        val -= 1
    elif i == "hlf":
        val //= 2
    elif i == "dbl":
        val *= 2
        pt1 *= 2

print("\n" + str(pt1))
