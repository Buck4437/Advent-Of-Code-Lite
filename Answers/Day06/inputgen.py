import random

random.seed(59729)

nums = []

for i in range(1000):
    nums.append(",".join([str(random.randrange(1, 11)) for x in range(3)]))

random.shuffle(nums)

with open("input.txt", "w") as f:
    f.write(nums[0])
    for num in nums[1:]:
        f.write("\n" + num)
