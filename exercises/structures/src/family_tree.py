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

    def populate_family_tree(self):

        # ex: child = Node('Child Name', parent = parent_node)

        lucille = Node("lucille")
        george_oscar = Node("George Oscar", parent=lucille)
        michael = Node("Michael", parent=lucille)
        lindsay = Node("Lindsay", parent=lucille)
        buster = Node("Buster", parent=lucille)
        george_michael = Node("George Michael", parent=michael)
        maeby = Node("Maeby", parent=lindsay)

        return
