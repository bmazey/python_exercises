
import anytree

class FamilyTree:

    def __init__(self):
        self.lucille = anytree.Node("")
        self.george_oscar = anytree.Node("")
        self.michael = anytree.Node("")
        self.buster = anytree.Node("")
        self.lindsay = anytree.Node("")
        self.george_michael = anytree.Node("")
        self.maeby = anytree.Node("")

    def populate_family_tree(self):
        self.lucille = anytree.Node("Lucille")
        self.george_oscar = anytree.Node("George Oscar", parent=self.lucille)
        self.lindsay = anytree.Node("Lindsay" , parent=self.lucille)
        self.michael = anytree.Node("Michael", parent=self.lucille)
        self.buster = anytree.Node("Buster", parent=self.lucille)
        self.george_michael = anytree.Node ("GeorgeMichael", parent=self.michael)
        self.maeby = anytree.Node("Maeby", parent=self.lindsay)

        # ex: child = Node('Child Name', parent = parent_node)

        # TODO - implement this method!

        return self.lucille

