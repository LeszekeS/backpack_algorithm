class Item:

    ekstensja = list()

    def __init__(self, name, weight, utility, quantity, n1utility):
        self.name = name
        self.weight = weight
        self.utility = utility
        self.quantity = quantity
        self.n1utility = n1utility
        Item.ekstensja.append(self)

    def __str__(self):
        return f'name: {self.name}; utility: {self.utility}'


class Backpack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_weight = 0
        self.items = dict()

    def asses_efficiency(self, item):
        if item not in self.items:
            return item.utility / item.weight
        else:
            return item.utility * item.n1utility ** self.items[item]


def load_file(source):
    file = open(source, 'r')
    data = file.readlines()
    file.close()

    for row in data[1:]:
        if row != "/n":
            item = row.strip().split(';')
            Item(item[0], float(item[1]), float(item[2]), int(item[3]), float(item[4]))


load_file("boat.txt")

print("items on boat")
for i in sorted(Item.ekstensja, key=lambda x: x.utility, reverse=True):
    print(i)

backpack = Backpack(10)


freespace = True
while freespace:
    freespace = False
    tmp_hierarchy = []
    for item in Item.ekstensja:
        if item.weight + backpack.current_weight <= backpack.capacity and item.quantity > 0:
            tmp_hierarchy.append([item, backpack.asses_efficiency(item)])
            freespace = True
    tmp_hierarchy.sort(key=lambda x: x[1], reverse=True)
    if tmp_hierarchy:
        if tmp_hierarchy[0][0] in backpack.items:
            backpack.items[tmp_hierarchy[0][0]] += 1
        else:
            backpack.items[tmp_hierarchy[0][0]] = 1
        tmp_hierarchy[0][0].quantity -= 1
        backpack.current_weight += tmp_hierarchy[0][0].weight
        print(f'adding to backpack: {tmp_hierarchy[0][0]}; current weight {backpack.current_weight}, efficiency: {tmp_hierarchy[0][1]}')


print("Items in backpack")
print(f"weight of backpack {backpack.current_weight}")
for i in backpack.items:
    print(f'{i}, taken: {backpack.items[i]}')

print("Left on boat")
for i in sorted(Item.ekstensja, key=lambda x: x.utility, reverse=False):
    if i.quantity > 0:
        print(i)
