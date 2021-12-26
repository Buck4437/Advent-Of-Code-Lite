for c in "INTCODE":
    print(ord(c))

f = open("Day03.txt", "w")


def inc(val):
    for i in range(val):
        f.write("inc\n")


def dec(val):
    for i in range(val):
        f.write("dec\n")


def dbl(val):
    for i in range(val):
        f.write("dbl\n")


def hlf(val):
    for i in range(val):
        f.write("hlf\n")


def out(val = 1):
    for i in range(val):
        f.write("out\n")


inc(7) # 7
dbl(1) # 14
dec(4) # 10
dbl(3) # 80
dec(7) # 73
out() # I
hlf(2) # 73 -> 36 -> 18
dec(10) # 8
inc(11) # 19
dbl(2) # 76
inc(2) # 78
out() # N
dec(3) # 75
inc(9) # 84
out()
hlf(1) # 42
inc(22) # 64
hlf(1) # 32
inc(35) # 67
out() # C
dec(17) # 50
dbl(1) # 100
dec(21) # 79
out() # O
dec(70) # 9
dbl(3) # 72
hlf(5) # 72 -> 36 -> 18 -> 9 -> 4 -> 2
dbl(5) # 2 -> 4 -> 8 -> 16 -> 32 -> 64
inc(4) # 68
out() # D
inc(33) # 101
hlf(2) # 101 -> 50 -> 25
dec(24) # 1
inc(59) # 60
dbl(1) # 120
inc(18) # 138
hlf(1) # 69
out() # E
dbl(2)
inc(6)
dbl(1)

f.close()
