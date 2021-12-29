import random

random.seed(1348473)


def padded_to_bin(num):
    return bin(num)[2:].zfill(8)


nums = []

# "Neg nums": 128 <= x < 256
for i in range(235):
    nums.append(random.randrange(128, 256))

# Large positive nums: 64 <= x < 128
for i in range(458):
    nums.append(random.randrange(64, 128))

# Small nums: 0 <= x < 64
for i in range(1000 - 235 - 458):
    nums.append(random.randrange(0, 64))

random.shuffle(nums)
print(nums)
with open("input.txt", "w") as f:
    for num in nums:
        f.write(padded_to_bin(num) + "\n")