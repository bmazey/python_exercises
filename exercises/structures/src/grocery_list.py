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
        # TODO - implement this method!
        # makes the list of groceries
        groceries = ["milk","eggs","seltzer","honey","seltzer"]
        # loop to add the stuff in groceries to items list
        for stuff in groceries:
            self.items.append(stuff)
        return

