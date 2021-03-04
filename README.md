# IOT-Worksheet-2

## Contents
1. [Task 1](#Task-1-Explanation)
1. [Task 2](#Task-2-Explanation)
1. [Task 3](#Task-3-Explanation)
1. [Task 4](#Task-4-Explanation)

## Task 1 Explanation
For this task I was required to convert the word "us" into morse using the webserver provided.

**The word us translated to morse code is ..- ...**

Here is a screenshot of the website running from the server via my machine.

<img src="./assets/img/morsewebsite.png" alt="Morse Website" width="400"/>

## Task 2 Explanation
Task 2 required me to use a binary tree (similar to the image below) to implement a morse code encoder/decoder.

<img src="./assets/img/morsecodetreetask2.png" alt="Morse Code Tree" width="600"/>

**To run task 2, run the "Task 2/main.py" file. Ensure both "tree.py" and "morse.py" are in the same directory as "main.py".**

Here is a screenshot of me running the file:

<img src="./assets/img/morsetask2results.png" alt="Morse Task 2 Results " width="600"/>

To test a different word alter any occurences of the word "us" and its morse code in "Task 2/main.py" file. An example cahange is below.
```py
e = morse.encode('them') 
#WAS PREVIOUSLY e = morse.encode('us')

assert morse.encode('them') == '- .... . --', "Should be - .... . --" 
#WAS PREVIOUSLY assert morse.encode('us') == '..- ...', "Should be ..- ..."

assert morse.decode('- .... . --') == 'them', "Should be them" 
#WAS PREVIOUSLY assert morse.decode('..- ...') == 'us', "Should be us"
```

## Task 3 Explanation
Task 3 required me to unit test the encode, decode and tree implementations. 

The tests I ran are as follows:
- Testing the encode & decode functions.
    1. Encoding the word "us"
    1. Decoding the word "us"
    1. Encoding the word "them"
    1. Decoding the word "them"
    1. Encoding the sentence "this is a test"
    1. Decoding the sentence "this is a test"
    1. Encoding the number "1"
    1. Decoding the number "1"
    1. Encoding the symbol "$" (Expected to fail)
    1. Decoding the symbol "$" (Expected to fail)
- Testing the tree.
    1. Checking an empty tree is correctly created.
    1. Checking a non empty tree is correctly created.
    1. Checking the insert function.
    1. Checking the find functions.

**To run the unit tests, run the "Task 3/morseunit.py" file. Ensure both "tree.py" and "morse.py" are in the same directory.**

Here is a screenshot of me running the file:

<img src="./assets/img/morseUnitTestingTask3.png" alt="Morse Task 3 Unit Testing" width="600"/>

As you can see all but two tests pass. These 2 tests were expected to fail as I have not implemented symbols into my tree yet. This will be implemented in the next task.

## Task 4 Explanation

Task 4 required me to implement symbols into my binary tree. To do this I first created a new diagram to help me visualise how the new tree would look:

<img src="./assets/img/morsecodetreetask4.png" alt="Morse Task 3 Unit Testing"/>

Using the diagram I identified that I would need to add elemtns for the empty nodes in the tree in order for symbols and some numbers to work.

I then updated my unit tests to test each symbol by creating the following tests:
```py
#TESTING THE SYMBOLS
def test_encode_symbols(self):
    self.assertEqual(morse.encode('.'), '.-.-.-')
    self.assertEqual(morse.encode('('), '-.--.')
    self.assertEqual(morse.encode('+'), '.-.-.')
    self.assertEqual(morse.encode('¿'), '..-.-')
    self.assertEqual(morse.encode(','), '--..--')
    self.assertEqual(morse.encode(')'), '-.--.-')
    self.assertEqual(morse.encode('-'), '-....-')
    self.assertEqual(morse.encode('¡'), '--...-')
    self.assertEqual(morse.encode('?'), '..--.')
    self.assertEqual(morse.encode('&'), '.-...')
    self.assertEqual(morse.encode('_'), '..--.-')
    self.assertEqual(morse.encode('\''), '.----.')
    self.assertEqual(morse.encode(':'), '---...')
    self.assertEqual(morse.encode('"'), '.-..-.')
    self.assertEqual(morse.encode('!'), '-.-.--')
    self.assertEqual(morse.encode(';'), '-.-.-.')
    self.assertEqual(morse.encode('$'), '...-..-')

def test_decode_symbols(self):
    self.assertEqual(morse.decode('.-.-.-'), '.')
    self.assertEqual(morse.decode('-.--.'), '(')
    self.assertEqual(morse.decode('.-.-.'), '+')
    self.assertEqual(morse.decode('..-.-'), '¿')
    self.assertEqual(morse.decode('--..--'), ',')
    self.assertEqual(morse.decode('-.--.-'), ')')
    self.assertEqual(morse.decode('-....-'), '-')
    self.assertEqual(morse.decode('--...-'), '¡')
    self.assertEqual(morse.decode('..--.'), '?')
    self.assertEqual(morse.decode('.-...'), '&')
    self.assertEqual(morse.decode('..--.-'), '_')
    self.assertEqual(morse.decode('.----.'), '\'')
    self.assertEqual(morse.decode('---...'), ':')
    self.assertEqual(morse.decode('.-..-.'), '"')
    self.assertEqual(morse.decode('-.-.--'), '!')
    self.assertEqual(morse.decode('-.-.-.'), ';')
    self.assertEqual(morse.decode('...-..-'), '$')
```
**To run the unit tests, run the "Task 4/morseunit.py" file. Ensure both "tree.py" and "morse.py" are in the same directory.**

All these tests successfullly pass meaning the implentation of symbols is correct.
<img src="./assets/img/morsetask4testing.png" alt="Morse Task 3 Unit Testing" width="600px"/>