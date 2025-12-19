inp = open("big_input.txt").read().split(",")

total = 0

for r in inp:
    lower, upper = r.split("-")
    for code in range(int(lower), int(upper)+1):
        strcode = str(code)
        if len(strcode)%2 == 0 and strcode[:int(len(strcode)/2)] == strcode[int(len(strcode)/2):]:
            total += code

print(total)