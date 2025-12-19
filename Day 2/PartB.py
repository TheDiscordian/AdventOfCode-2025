inp = open("big_input.txt").read().split(",")

total = 0

def verify_pattern(code, pattern):
    d = int(len(code)/len(pattern))
    if d*len(pattern) != len(code):
        #print("Returning false because1: %d != %d" % (d*len(pattern), len(code)))
        return False
    for i in range(d-1):
        if code[i*len(pattern):i*len(pattern)+len(pattern)] != pattern:
            #print("Returning false because2: %s != %s" % (code[i*len(pattern):i*len(pattern)+len(pattern)], pattern))
            return False
    return True

def find_pattern(code):
    pattern = ""
    for i in range(int(len(code)/2)):
        if code[:i+1] == code[-i-1:]:
            pattern = code[:i+1]
            if verify_pattern(code, pattern):
                return True
    if pattern == "":
        return False
    return verify_pattern(code, pattern)

for r in inp:
    lower, upper = r.split("-")
    for code in range(int(lower), int(upper)+1):
        if find_pattern(str(code)):
            #print("True: %d" % code)
            total += code

print(total)