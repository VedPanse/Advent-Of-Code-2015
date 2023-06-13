fs = open("day2.txt", "r")
inventory = fs.read().split("\n")
fs.close()

total_area = 0

for box in inventory:
    dimensions = box.split("x")
    int_dimensions = []
    for items in dimensions:
        int_dimensions.append(int(items))

    dimensions = int_dimensions
    del int_dimensions

    l, w, h = dimensions[0], dimensions[1], dimensions[2]
    dimensions.sort()

    required_area = 2 * (l*w + w*h + l*h)
    extra_area = dimensions[0] * dimensions[1]

    total_area = required_area + extra_area + total_area

print(total_area)
