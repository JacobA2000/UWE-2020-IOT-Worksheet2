class BinaryTree():
    def __init__(self, root):
        self.root = root
        self.left - None
        self.right = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node(self, value):
        self.root = value

    def get_node(self):
        return self.root

    def print_tree(tree, nest):
        if tree != None:
            for i in range(nest):
                print(" ", end="")
            print(tree.root)
            BinaryTree.print_tree(tree.left, nest+1)
            BinaryTree.print_tree(tree.right, nest+1)

    def insert_search(tree, letter, morse):
        if tree == None:
            return BinaryTree((letter, morse))
        else:
            if letter < tree.root[0]:
                tree.left = BinaryTree.insert_search(tree.left, letter, morse)
                return tree
            elif letter > tree.root[0]:
                tree.right = BinaryTree.insert_search(tree.right, letter, morse)
                return tree
            else:
                tree.root = (letter, morse)
                return tree
    
    def find_search(tree, letter)
        if tree == None:
            raise Exception("Non Existant Letter.")
        else:
            if letter < tree.root[0]:
                return BinaryTree.find_search(tree.left, letter)
            elif letter > tree.root[0]:
                return BinaryTree.find_search(tree.right, letter)
            #MAY BE WRONG
            else:
                return (letter, morse)