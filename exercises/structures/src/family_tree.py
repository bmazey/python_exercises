import anytree


class FamilyTree:

    def __init__(self):
        self.lucille = anytree.Node("Lucille")
        self.george_oscar = anytree.Node("",parent=self.lucille)
        self.michael = anytree.Node("Michael",parent=self.lucille)
        self.lindsay = anytree.Node("Lindsay",parent=self.lucille)
        self.buster = anytree.Node("",parent=self.lucille)
        self.george_michael = anytree.Node("",parent=self.michael)
        self.maeby = anytree.Node("",parent=self.lindsay)

    def populate_family_tree(self):
        # ex: child = Node('Child Name', parent = parent_node)

        # TODO - implement this method!

        return
