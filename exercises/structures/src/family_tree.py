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
        # ex: child = Node('Child Name', parent = parent_node)
        self.lucille = anytree.Node("Lucille", parent=self.lucille)
        self.george_oscar = anytree.Node("George Oscar", parent=self.lucille)
        self.michael = anytree.Node("Michael", parent=self.lucille)
        self.lindsay = anytree.Node("Lindsay", parent=self.lucille)
        self.buster = anytree.Node("Buster", parent=self.lucille)
        self.george_michael = anytree.Node("George Michael", parent=self.michael)
        self.maeby = anytree.Node("Maeby", parent=self.lindsay)

        # TODO - implement this method!
  # this tells the test to read the number of children branches
    def __len__(self):
        return len(self.lucille.children)