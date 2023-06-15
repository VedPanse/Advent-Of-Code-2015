fs = open("day14.txt", "r")
data = fs.read().split("\n")
fs.close()

print(f"{data[0]}\n__________")

distances_covered = []

for sentence in data:
    name = sentence.split(" can fly")[0]
    velocity = int(sentence.split(" can fly ")[1].split(" km/s")[0])
    go_time = int(sentence.split(" can fly ")[1].split(" km/s for ")[1].split(" seconds")[0])
    rest_time = int(sentence.split(" can fly ")[1].split(" km/s for ")[1].split(" seconds")[1].split(", but then must "
                                                                                                     "rest for ")[1])
    time_limit = 2503
    time_used = 0
    distance = 0

    while time_used < time_limit:
        distance += velocity * go_time
        time_used += go_time + rest_time

    distances_covered.append(distance)

print(max(distances_covered))
