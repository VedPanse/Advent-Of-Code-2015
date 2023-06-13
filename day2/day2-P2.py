fs = open("day2.txt", "r")
inventory = fs.read().split("\n")
fs.close()

total_ribbon = 0

for box in inventory:
    dimensions = box.split("x")
    int_dimensions = [int(k) for k in dimensions]

    dimensions = int_dimensions
    del int_dimensions
    dimensions.sort()

    total_ribbon += (dimensions[0] * dimensions[1] * dimensions[2]) + 2 * (dimensions[0] + dimensions[1])

print(total_ribbon)