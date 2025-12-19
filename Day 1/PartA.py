rots = open("big_input.txt").read().split()

val = 50
zeros = 0

for rot in rots:
    val += int(rot[1:]) * (-1 if rot[0] == "L" else 1)
    zeros += 1 if val % 100 == 0 else 0
print(zeros)