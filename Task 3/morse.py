from tree import *

#The list of letters and morsecode to place into the trees.
morseLetters = [
    #Tree Level 1
    ("E", "."),
    ("T", "-"),
    #Tree Level 2
    ("I", ".."),
    ("A", ".-"),
    ("N", "-."),
    ("M", "--"),
    #Tree Level 3
    ("S", "..."),
    ("U", "..-"),
    ("R", ".-."),
    ("W", ".--"),
    ("D", "-.."),
    ("K", "-.-"),
    ("G", "--."),
    ("O", "---"),
    #Tree Level 4
    ("H", "...."),
    ("V", "...-"),
    ("F", "..-."),
    ("L", ".-.."),
    ("P", ".--."),
    ("J", ".---"),
    ("B", "-..."),
    ("X", "-..-"),
    ("C", "-.-."),
    ("Y", "-.--"),
    ("Z", "--.."),
    ("Q", "--.-"),

    #Tree Level 5
    ("5", "....."),
    ("4", "....-"),
    ("3", "...--"),
    ("2", "..---"),
    ("+", ".-.-."),
    ("1", ".----"),
    ("6", "-...."),
    ("=", "-...-"),
    ("/", "-..-."),
    ("7", "--..."),
    ("8", "---.."),
    ("9", "----."),
    ("0", "-----")
]

#CREATE THE TREES
letterTree = BinaryTree("START")
morseTree = BinaryTree("START")

#ADD THE LETTERS TO THE TREES
for letter in morseLetters:
    letterTree = BinaryTree.insert_search(letterTree, letter[0], letter[1])
    morseTree = BinaryTree.insert_morse(morseTree, letter[0], letter[1])

#FUNCTION:      encode(msg)
#PARAMS:        msg - String
#DESCRIPTION:   Will encode a msg into morse code using the letter tree.
#RETURNS:       morseString - the message encoded into morse.
def encode(msg):
    msg = msg.upper()
    msgWords = msg.split()

    morseString = ""

    for word in msgWords:
        wordMorse = ""
        for char in word:
            wordMorse += f"{BinaryTree.find_search(letterTree, char)} "
        
        if len(msgWords) > 1 and word != msgWords[(len(msgWords)-1)]:
            wordMorse = wordMorse[:-1]
            
        morseString += f"{wordMorse} / "

    morseString = morseString[:-4]
    return morseString

#FUNCTION:      decode(msg)
#PARAMS:        msg - String
#DESCRIPTION:   Will decode a msg from morse code to readable english.
#RETURNS:       morseString.lower() - the decoded message in lower case.
def decode(msg):
    msg = msg.upper()
    morseChars = msg.split()

    morseString = ""

    for char in morseChars:
        wordMorse = ""
        if char != "/" and char != " ":
            wordMorse += BinaryTree.find_morse(morseTree, char)
        else:
            wordMorse += " "

        morseString += wordMorse

    return morseString.lower()