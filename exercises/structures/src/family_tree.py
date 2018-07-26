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

        # TODO - implement this method!
        self.lucille = Node('Lucille')
        self.lindsay = Node('lindsay', parent = self.lucille)
        self.michael = Node('Michael', parent = self.lucille)
        self.buster = Node('buster', parent = self.lucille)
        self.george_oscar = Node('george_oscar', parent = self.lucille)
        self.george_michael = Node('george_michale', parent = self.michael)
        self.maeby = Node('maeby', parent = self.lindsay)


        return self
