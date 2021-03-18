#=====================================================================================================
# FILE:                         morseunit.py
# DATE LAST MODIFIED:           25/02/2021
# MODIFICATION DESCRIPTION:     Added More Tests
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
import unittest
import morse
from tree import BinaryTree

class TestMorse(unittest.TestCase):
#TESTING MORSE ENCODE AND DECODE.
    #ALL OF THESE SHOULD PASS
    def test_encode_us(self):
        self.assertEqual(morse.encode('us'), '..- ...')
    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'), 'us')
    
    def test_encode_them(self):
        self.assertEqual(morse.encode('them'), '- .... . --')
    def test_decode_them(self):
        self.assertEqual(morse.decode('- .... . --'), 'them')

    def test_encode_sentence(self):
        self.assertEqual(morse.encode('this is a test'), '- .... .. ... / .. ... / .- / - . ... -')
    def test_decode_sentence(self):
        self.assertEqual(morse.decode('- .... .. ... / .. ... / .- / - . ... -'), 'this is a test')

    def test_encode_number(self):
        self.assertEqual(morse.encode("1"), ".----")
    def test_decode_number(self):
        self.assertEqual(morse.decode(".----"), "1")

    #THIS IS EXPECTED TO FAIL
    def test_encode_symbol(self):
        self.assertEqual(morse.encode('$'), '...-..-')
    def test_decode_symbol(self):
        self.assertEqual(morse.decode('...-..-'), '$')

    
#TESTING THE TREE.
    def test_empty_tree(self):
        empty_tree = BinaryTree("")
        self.assertEqual(empty_tree.root, "")
        self.assertEqual(empty_tree.left, None)
        self.assertEqual(empty_tree.right, None)

    def test_non_empty_tree(self):
        non_empty_tree = BinaryTree("Test")
        non_empty_tree.left = "A"
        non_empty_tree.right = "B"

        self.assertEqual(non_empty_tree.root, "Test")
        self.assertEqual(non_empty_tree.left, "A")
        self.assertEqual(non_empty_tree.right, "B")

    def test_insert_tree(self):
        test_tree = BinaryTree("Start")
        BinaryTree.insert_search(test_tree, "A", ".-")

        self.assertEqual(test_tree.root, "Start")
        self.assertEqual(test_tree.left.root, ("A", ".-"))

    def test_find_search_tree(self):
        test_tree = morse.letterTree

        self.assertEqual(BinaryTree.find_search(test_tree, "A"), ".-")
    
    def test_find_morse_tree(self):
        test_tree = morse.morseTree

        self.assertEqual(BinaryTree.find_morse(test_tree, ".-"), "A")

if __name__ == '__main__':
    unittest.main()