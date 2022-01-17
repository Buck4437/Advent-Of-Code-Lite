import random

random.seed(5979)

nums = []


def gen_chunk(lng):
    wd = ""
    for i in range(lng):
        wd += str(random.randrange(0, 10))
    return wd


for i in range(1000 - 858):
    nums.append(gen_chunk(4) + "0")


for i in range(858):
    nums.append(gen_chunk(5))

random.shuffle(nums)

with open("input.txt", "w") as f:
    f.write(nums[0])
    for num in nums[1:]:
        f.write("-" + num)
