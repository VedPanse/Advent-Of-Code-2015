AUNT_DATA = {

}

fs = open("day16.txt", "r")
data = fs.read().split("\n")
fs.close()

for item in data:
    name = item.split(" ")[1][:-1]
    sub_dict = {

    }
    property_1 = item.split(" ")[2][:-1]
    property_2 = item.split(" ")[4][:-1]
    property_3 = item.split(" ")[6][:-1]
    sub_dict[property_1] = item.split(" ")[3][:-1]
    sub_dict[property_2] = item.split(" ")[5][:-1]
    sub_dict[property_3] = item.split(" ")[7][:-1]

    AUNT_DATA[name] = sub_dict

AUNT_SENT = {
    'children': '3',
    'cats': '7',
    'samoyeds': '2',
    'pomeranians': '3',
    'akitas': '0',
    'vizslas': '0',
    'goldfish': '5',
    'trees': '3',
    'cars': '2',
    'perfumes': '1'
}


for name, property in AUNT_DATA.items():
    truethy = []
    for item, quantity in property.items():
        if property[item] == AUNT_SENT[item] or property[item] == '':
            truethy.append(True)
        else:
            truethy.append(False)

    if False not in truethy:
        print(name)
