with open("input.txt") as f:
    wds = f.read().split("-")

ct = 0
for wd in wds:
    if wd[-1] == "0":
        print(wd)
        ct += 1

print("Total:", ct)
