fs = open("day3.txt", "r")
santa_map = list(fs.read())
fs.close()

position = [0, 0]
visited_positions = [(0, 0)]

for direction in santa_map:
    if direction == "^":
        position[1] += 1
    elif direction == "v":
        position[1] -= 1
    elif direction == "<":
        position[0] -= 1
    elif direction == ">":
        position[0] += 1
    visited_positions.append((position[0], position[1]))

print(len(set(visited_positions)))
