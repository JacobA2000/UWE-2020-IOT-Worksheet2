from tree import *

morseLetters = [
    ("E", "."),
    ("T", "-"),
    ("I", ".."),
    ("A", ".-"),
    ("N", "-."),
    ("M", "--"),
    ("S", "..."),
    ("U", "..-"),
    ("R", ".-."),
    ("W", ".--"),
    ("D", "-.."),
    ("K", "-.-"),
    ("G", "--."),
    ("O", "---"),
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

letterTree = BinaryTree("START")

morseTree = BinaryTree("START")
#morseTree.left = BinaryTree(("E", "."))
#morseTree.right = BinaryTree(("T", "-"))

for letter in morseLetters:
    letterTree = BinaryTree.insert_search(letterTree, letter[0], letter[1])
    morseTree = BinaryTree.insert_morse(morseTree, letter[0], letter[1])

def encode(msg):
    msg = msg.upper()
    msgWords = msg.split()

    morseString = ""

    for word in msgWords:
        wordMorse = ""
        for char in word:
            wordMorse += f"{BinaryTree.find_search(letterTree, char)} "
            
        morseString += f"{wordMorse} / "

    morseString = morseString[:-4]
    return morseString

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

#morse = encode("us test")
#print(morse)
#decodedMorse = decode(morse)
#print(decodedMorse)

