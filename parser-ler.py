def get_cit(s):
    arr = []
    b = False
    cit = ""
    for c in s:
        if (c == '('):
            b = True
            cit += c
        elif (b):
            cit += c
            if (c == ')'):
                arr.append(cit)
                cit = ""
                b = False
    return arr


def num_count(s):
    count = 0
    for c in s:
        if (c.isdigit()):
            count += 1
    return count


file = 'data.txt'

with open(file, 'r') as file:
    s = file.read()

s = "hi i am john (first citation, 1000) hi i am another john (second citation, 2000)"
arr = get_cit(s)

for c in arr:
    if (num_count(c) >= 4):
        print(c)

