fs = open("day3.txt", "r")
house_map = list(fs.read())
fs.close()

santa_map = []
robot_map = []

santa_position = [0, 0]
robot_position = [0, 0]

santa_check = [(0, 0)]
robot_check = [(0, 0)]

for i in range(len(house_map)):
    if i % 2 == 0:
        santa_map.append(house_map[i])
    else:
        robot_map.append(house_map[i])


for direction in santa_map:
    if direction == "^":
        santa_position[1] += 1
    elif direction == "v":
        santa_position[1] -= 1
    elif direction == "<":
        santa_position[0] -= 1
    elif direction == ">":
        santa_position[0] += 1

    santa_check.append((santa_position[0], santa_position[1]))

for direction in robot_map:
    if direction == "^":
        robot_position[1] += 1
    elif direction == "v":
        robot_position[1] -= 1
    elif direction == "<":
        robot_position[0] -= 1
    elif direction == ">":
        robot_position[0] += 1

    santa_check.append((robot_position[0], robot_position[1]))

santa_check.extend(robot_check)
print(len(set(santa_check)))
