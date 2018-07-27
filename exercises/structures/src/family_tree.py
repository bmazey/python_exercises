import anytree
from anytree import Node, RenderTree


class FamilyTree:

    def __init__(self):
        self.lucille = anytree.Node("")
        self.george_oscar = anytree.Node("")
        self.michael = anytree.Node("")
        self.lindsay = anytree.Node("")
        self.buster = anytree.Node("")
        self.george_michael = anytree.Node("")
        self.maeby = anytree.Node("")
# this names the parent branch of each branches
# lucille is the root branch

    def populate_family_tree(self):
        self.lucille = Node("Lucille")
        self.george_oscar = Node("George Oscar", parent=self.lucille)
        self.michael = Node("Michael", parent=self.lucille)
        self.lindsay = Node("Lindsay", parent=self.lucille)
        self.buster = Node("Buster", parent=self.lucille)
        self.george_michael = Node("George Michael", parent=self.michael)
        self.maeby = Node("Maeby", parent=self.lindsay)

# this tells the test to read the number of children branches
    def __len__(self):
        return len(self.lucille.children)

        # ex: child = Node('Child Name', parent = parent_node)
        return
