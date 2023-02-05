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

backpack = Backpack(12)


for item in Item.ekstensja:
    print(f'{item}, efficiency of item: {backpack.asses_efficiency(item)}')



# idx = 0
# freespace = True
# Item.ekstensja.sort(key=lambda x: x.we_va_relation, reverse=True)
#
# while freespace:
#     while idx < len(Item.ekstensja):
#         if backpack.current_weight + Item.ekstensja[idx].weight <= backpack.capacity and Item.ekstensja[idx].quantity > 0:
#             if Item.ekstensja[idx] in backpack.items:
#                 backpack.items[Item.ekstensja[idx]] += 1
#             else:
#                 backpack.items[Item.ekstensja[idx]] = 1
#             Item.ekstensja[idx].quantity -= 1
#             backpack.current_weight += Item.ekstensja[idx].weight
#             print(f'adding to backpack: {Item.ekstensja[idx]}; '
#                   f'current weight {backpack.current_weight}, '
#                   f'value/kg: {Item.ekstensja[idx].we_va_relation}')
#             idx -= 1
#         idx += 1
#     freespace = False
#
# print("Items in backpack")
# print(f"weight of backpack {backpack.current_weight}")
# for i in backpack.items:
#     print(f'{i}, stolen: {backpack.items[i]}')
#
# print("Left in store")
# for i in sorted(Item.ekstensja, key=lambda x: x.value, reverse=False):
#     if i.quantity > 0:
#         print(i)
