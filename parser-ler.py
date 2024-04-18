def get_cit(s):
    prev = []
    arr = []
    b = False
    cit = ""
    word = ""
    for c in s:
        if (c == '('):
            b = True
            cit += c
        elif (b):
            cit += c
            if (c == ')'):
                if (len(cit) == 6 and num_count(cit) == 4):
                    arr.append(prev[0]+prev[1]+prev[2]+cit)
                else:
                    arr.append(cit)
                cit = ""
                b = False
        else:
            word += c
            if (c == ' '):
                if (len(prev) < 3):
                    prev.append(word)
                else:
                    prev[0] = prev[1]
                    prev[1] = prev[2]
                    prev[2] = word
                word = ""

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

arr = get_cit(s)

i=0
print("------------------ LER'S CITATION ------------------")
for c in arr:
    if (num_count(c) >= 4):
        print(i,c)
        i += 1

