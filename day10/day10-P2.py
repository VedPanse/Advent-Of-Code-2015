PUZZLE_INPUT = 1321131112
next_input = 0

def lookAndSay(num):
    text = str(num)
    parent_string = ''

    from itertools import groupby
    raw_list = ["".join(g) for k, g in groupby(text) if k != '-' and k != '/']
    
    for item in raw_list:
        parent_string += str(len(item)) + str(item[0])

    return int(parent_string)


for i in range(50):
    if i == 0:
        next_input = lookAndSay(PUZZLE_INPUT)
    else:
        next_input = lookAndSay(next_input)

print(len(str(next_input)))