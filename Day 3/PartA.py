inp = open("big_input.txt").read().split()

def find_largest(line, offset=-1):
    if offset < 0:
        largest = (0, 0)
        for i in range(len(line)+offset):
            n = int(line[i])
            if n > largest[0]:
                largest = (n, i+1)
                if largest[0] == 9:
                    return largest
        return largest
    largest = 0
    for i in range(len(line)-offset):
        n = int(line[i+offset])
        if n > largest:
            largest = n
    return largest

total = 0
for line in inp:
    first = find_largest(line)
    second = find_largest(line, first[1])
    total += int("%d%d" % (first[0], second))

print(total)