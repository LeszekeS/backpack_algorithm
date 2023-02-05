class Item:

    ekstensja = list()

    def __init__(self, name, weight, value, quantity):
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = quantity
        self.we_va_relation = value / weight
        Item.ekstensja.append(self)

    def __str__(self):
        return f'name: {self.name}; weight: {self.weight}; quantity: {self.quantity}; value: {self.value}'


class Backpack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_weight = 0
        self.items = list()


def load_file(source):
    file = open(source, 'r')
    data = file.readlines()
    file.close()

    for row in data[1:]:
        if row != "/n":
            item = row.strip().split(';')
            Item(item[0], float(item[1]), float(item[2]), int(item[3]))


load_file("store.txt")

print("items in shop")
for i in sorted(Item.ekstensja, key=lambda x: x.value, reverse=False):
    print(i)

# backpack = Backpack(10)
#
# for i in sorted(Item.ekstensja, key=lambda x: x.we_va_relation, reverse=True):
#     if backpack.current_weight + i.weight <= backpack.capacity:
#         backpack.items.append(i)
#         backpack.current_weight += i.weight
#         Item.ekstensja.remove(i)
#         print(f'adding to backpack: {i}, value/kg: {i.we_va_relation}')
#
#
# print("Items in backpack")
# print(f"weight of backpack {backpack.current_weight}")
# for i in backpack.items:
#     print(i)
#
# print("Left in shop")
# for i in sorted(Item.ekstensja, key=lambda x: x.value, reverse=False):
#     print(i)
