NICE_STRINGS = 0

fs = open("day5.txt", "r")
string_collection = fs.read().split("\n")
fs.close()


def check_vowels(s):
    vowels = "aeiou"

    if len([k for k in list(s) if k in list(vowels)]) >= 3:
        return 1
    return 0


def invalidate_strings(s):
    invalid_strings = ["ab", "cd", "pq", "xy"]

    for item in invalid_strings:
        if item in s:
            return 0

    return 1


def consecutive_strings(s):
    s = list(s)

    for index in range(len(s) - 1):
        if s[index] == s[index + 1]:
            return 1
    return 0


def is_nice(s):
    if check_vowels(s) == invalidate_strings(s) == consecutive_strings(s) == 1:
        return True
    return False


for string in string_collection:
    if is_nice(string):
        NICE_STRINGS += 1


print(NICE_STRINGS)
