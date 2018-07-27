import anytree


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

        # TODO - implement this method!self.george_oscar = anytree.Node("George_oscar,", parent=lucille)
        self.lucille = anytree.Node("Lucille")
        self.george_oscar = anytree.Node("george oscar", parent=self.lucille)
        self.michael = anytree.Node("michael", parent=self.lucille)
        self.lindsay = anytree.Node("lindsay", parent=self.lucille)
        self.buster = anytree.Node("buster", parent=self.lucille)
        self.george_michael = anytree.Node("george michael", parent=self.michael)
        self.maeby = anytree.Node("maeby", parent=self.lindsay)

        return
