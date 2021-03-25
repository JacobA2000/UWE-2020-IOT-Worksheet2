#=====================================================================================================
# FILE:                         tree.py
# DATE LAST MODIFIED:           25/02/2021
# MODIFICATION DESCRIPTION:     Added Comments
#=====================================================================================================
# STUDENT NAME:                 JACOB ALLEN
# STUDENT NUM:                  19003931
#=====================================================================================================
# MODULE NAME:                  Internet Of Things
# MODULE CODE:                  UFCFVK-15-2
# WORKSHEET:                    2 (Part 1)
# WORKSHEET SPECIFICATION:      ../assets/Worksheet 2 Part 1.pdf
#=====================================================================================================
# GITLAB REPO:                  https://gitlab.uwe.ac.uk/j58-allen/iot-worksheet-2
#=====================================================================================================

class BinaryTree():
    #FUNCTION:      __init__(self, root)
    #PARAMS:        self, Any Type - root
    #DESCRIPTION:   The constructor for BinaryTree()
    #RETURNS:       void
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    #FUNCTION:      get_left_child(self)
    #PARAMS:        self
    #DESCRIPTION:   Will get the left branch of the tree.
    #RETURNS:       self.left - the tree instanse's left branch.
    def get_left_child(self):
        return self.left

    #FUNCTION:      get_right_child(self)
    #PARAMS:        self
    #DESCRIPTION:   Will get the right branch of the tree.
    #RETURNS:       self.left - the tree instanse's right branch.
    def get_right_child(self):
        return self.right

    #FUNCTION:      set_node(self, value)
    #PARAMS:        self, Any Type - value
    #DESCRIPTION:   Will set the root to the value parsed.
    #RETURNS:       void
    def set_node(self, value):
        self.root = value

    #FUNCTION:      get_node(self)
    #PARAMS:        self
    #DESCRIPTION:   Will get the root.
    #RETURNS:       self.root
    def get_node(self):
        return self.root

    #FUNCTION:      print_tree(tree, nest)
    #PARAMS:        BinaryTree - tree, Int - nest
    #DESCRIPTION:   Will print out the tree.
    #RETURNS:       void
    def print_tree(tree, nest):
        if tree != None:
            for i in range(nest):
                print(" ", end="")
            print(tree.root)
            BinaryTree.print_tree(tree.left, nest+1)
            BinaryTree.print_tree(tree.right, nest+1)

    #FUNCTION:      insert_search(tree, letter, morse)
    #PARAMS:        BinaryTree - tree, String - letter, String - morse
    #DESCRIPTION:   Will insert a value into the tree ordering based alphabetically.
    #RETURNS:       tree - The new BinaryTree with the new element inserted. 
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
    
    #FUNCTION:      insert_morse(tree, letter, morse, morseCopy)
    #PARAMS:        BinaryTree - tree, String - letter, String - morse
    #DESCRIPTION:   Will insert a value into the tree ordering based on morse symbol '.' and '-'.
    #RETURNS:       tree - The new BinaryTree with the new element inserted.
    def insert_morse(tree, letter, morse, morseCopy=""):
        if morseCopy == "":
            morseCopy = morse

        if tree == None:
            return BinaryTree((letter, morse))
        else:
            if morseCopy[0] == ".":
                tree.left = BinaryTree.insert_morse(tree.left, letter, morse, morseCopy[1:])
                return tree
            elif morseCopy[0] == "-":
                tree.right = BinaryTree.insert_morse(tree.right, letter, morse, morseCopy[1:])
                return tree
    
    #FUNCTION:      find_search(tree, letter)
    #PARAMS:        BinaryTree - tree, String - letter
    #DESCRIPTION:   Will find a specific letter in the given tree and return its morse.
    #RETURNS:       tree.root[1] - the morse value of the letter we are searching for.
    def find_search(tree, letter):
        if tree == None:
            raise Exception("Non Existant Letter.")
        else:
            if letter < tree.root[0]:
                return BinaryTree.find_search(tree.left, letter)
            elif letter > tree.root[0]:
                return BinaryTree.find_search(tree.right, letter)
            else:
                return tree.root[1]

    #FUNCTION:      find_morse(tree, morse)
    #PARAMS:        BinaryTree - tree, String - morse
    #DESCRIPTION:   Will find a specific morse in the given tree and return its letter.
    #RETURNS:       tree.root[0] - the morse value of the letter we are searching for.
    def find_morse(tree, morse):    
        if tree == None:
            raise Exception("Non Existant Morse.")
        elif len(morse) == 0:
            return tree.root[0]
        else:
            if morse[0] == ".":
                return BinaryTree.find_morse(tree.left, morse[1:])
            elif morse[0] == "-":
                return BinaryTree.find_morse(tree.right, morse[1:])         