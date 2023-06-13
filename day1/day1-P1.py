fs = open("day1/day1.txt", "r")
data = list(fs.read())
fs.close()

current_floor = 0

for items in data:
    if items == "(":
        current_floor += 1
    elif items == ")":
        current_floor -= 1

print(current_floor)
