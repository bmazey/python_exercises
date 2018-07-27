import anytree
from anytree import Node, RenderTree
class FamilyTree:

    def __init__(self):
        self.lucille = anytree.Node("Lucille")
        self.george_oscar = anytree.Node("George_Oscar", parent=self.lucille)
        self.michael = anytree.Node("Michael", parent=self.lucille)
        self.lindsay = anytree.Node("Lindsay", parent=self.lucille)
        self.buster = anytree.Node("Buster", parent=self.lucille)
        self.george_michael = anytree.Node("George_Michael", parent=self.michael)
        self.maeby = anytree.Node("Maeby", parent=self.lindsay)
# this names the parent branch of each branches
# lucille is the root branch

    def populate_family_tree(self):

        return
