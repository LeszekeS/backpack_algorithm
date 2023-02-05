class Item():

    ekstensja = list()

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.we_va_relation = value / weight
        Item.ekstensja.append(self)


class Backpack():

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_weight = 0
        self.items = list()
