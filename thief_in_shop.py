class Item:

    ekstensja = list()

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.we_va_relation = value / weight
        Item.ekstensja.append(self)

    def __str__(self):
        return f'name: {self.name}; weight: {self.weight}; value: {self.value}'


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
            Item(item[0], float(item[1]), float(item[2]))


load_file("shop.txt")

print("items in shop")
for i in sorted(Item.ekstensja, key=lambda x: x.value, reverse=False):
    print(i)
