NICE_STRING = 0

fs = open('day5.txt', 'r')
string_collection = fs.read().split("\n")
fs.close()


def repeat_pair(s):
    ls = list(s)

    for i in range(len(ls) - 1):
        if s.count(str(ls[i] + ls[i + 1])) > 1:
            return 1

    return 0


def one_letter_between(s):
    ls = list(s)

    for i in range(len(ls) - 2):
        if ls[i] == ls[i + 2]:
            return 1

    return 0


for string in string_collection:
    if repeat_pair(string) == one_letter_between(string) == 1:
        NICE_STRING += 1

print(NICE_STRING)
