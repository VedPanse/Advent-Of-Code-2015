fs = open("day1.txt", "r")
data = list(fs.read())
fs.close()

current_floor = 0
positions = []

for i in range(len(data)):
    if current_floor == -1:
        positions.append(i)
    else:
        if data[i] == "(":
            current_floor += 1
        elif data[i] == ")":
            current_floor -= 1

print(positions[0])
