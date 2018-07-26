class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]

    def length(self):
        return len(self.items)

    def populate_list(self):
        self.add_item("milk")
        self.add_item("eggs")
        self.add_item("seltzer")
        self.add_item("honey")
        self.add_item("seltzer")

        return

