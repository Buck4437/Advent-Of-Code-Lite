with open("input.txt") as f:
    nums = [s.strip() for s in f.readlines()]

sm = ct = 0
for num in nums:
    if num[0] == "0":
        ct += 1
        sm += int(num, 2)
print(ct, sm)
