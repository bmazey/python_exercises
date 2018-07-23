import anytree
from anytree import Node


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

        # TODO - implement this method!
        # sets Lucille as tree root
        self.lucille = Node('Lucille')
        # sets Lindsay, George Oscar, Buster, and Michael as Lindsay's children
        self.lindsay = Node('Lindsay', parent=self.lucille)
        self.george_oscar = Node('George Oscar', parent=self.lucille)
        self.buster = Node('Buster', parent=self.lucille)
        self.michael = Node('Michael', parent=self.lucille)
        # sets Maeby as Lindsay's child
        self.maeby = Node('Maeby', parent=self.lindsay)
        # sets George Michael as Michael's child
        self.george_michael = Node('George Michael', parent=self.michael)

        return
