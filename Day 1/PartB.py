rots = open("big_input.txt").read().split()

val = 50
zeros = 0
wasZero = False

def getRots(n, wasZero):
    if n < 0:
        return int(abs(n) / 100) + (0 if wasZero else 1)
    return int(n / 100)

for rot in rots:
    change = int(rot[1:]) * (-1 if rot[0] == "L" else 1)
    print("Val: %d Rot: %s Change: %d" % (val, rot, change))
    val += change
    if val >= 100 or val < 0:
        zeros += getRots(val, wasZero)
        wasZero = False
    elif val == 0 and change != 0:
        zeros += 1
        wasZero = True
    else:
        wasZero = False
    val = val % 100
    if val == 0:
        wasZero = True
    print("Zeros:", zeros)
print(zeros)