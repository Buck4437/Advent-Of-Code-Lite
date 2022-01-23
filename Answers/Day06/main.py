with open("input.txt") as f:
    fmlas = f.read().split("\n")

sm = tot = 0
for fmla in fmlas:
    nums = fmla.split(",")
    sm += int(nums[2])
    tmp = 1
    for num in nums:
        tmp *= int(num)
    tot += tmp
print(sm, tot)
