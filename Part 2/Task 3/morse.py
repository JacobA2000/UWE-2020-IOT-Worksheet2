#=====================================================================================================
# FILE:                         morse.py
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
from tree import *
import asyncio
import websockets
import json

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
    ("", "..--"),
    ("L", ".-.."),
    ("", ".-.-"),
    ("P", ".--."),
    ("J", ".---"),
    ("B", "-..."),
    ("X", "-..-"),
    ("C", "-.-."),
    ("Y", "-.--"),
    ("Z", "--.."),
    ("Q", "--.-"),
    ("", "---."),
    ("", "----"),

    #Tree Level 5
    ("5", "....."),
    ("4", "....-"),
    ("", "...-."),
    ("3", "...--"),
    ("", "..-.."),
    ("¿", "..-.-"),
    ("?", "..--."),
    ("2", "..---"),
    ("&", ".-..."),
    ("", ".-..-"),
    ("+", ".-.-."),
    ("", ".-.--"),
    ("", ".--.."),
    ("", ".--.-"),
    ("", ".---."),
    ("1", ".----"),
    ("6", "-...."),
    ("=", "-...-"),
    ("/", "-..-."),
    ("", "-..--"),
    ("", "-.-.."),
    ("", "-.-.-"),
    ("(", "-.--."),
    ("", "-.---"),
    ("7", "--..."),
    ("", "--..-"),
    ("", "--.-."),
    ("", "--.--"),
    ("8", "---.."),
    ("", "---.-"),
    ("9", "----."),
    ("0", "-----"),

    #Tree Level 6
    ("", "...-.."),
    ("_", "..--.-"),
    ("\"", ".-..-."),
    (".", ".-.-.-"),
    ("'", ".----."),
    ("-", "-....-"),
    (";", "-.-.-."),
    ("!", "-.-.--"),
    (")", "-.--.-"),
    ("¡", "--...-"),
    (",", "--..--"),   
    (":", "---..."),

    #Tree Level 7
    ("$", "...-..-")
]

#BINARY HEAP OF LETTERS
letters_bh = "|ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3*¿?2&*+****16=/***(*7***8*90*************_****\"**.********'**-********;!*)***¡*,****:****************$**********************************************************************************************************************"

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

#FUNCTION:      decode_bt(msg)
#PARAMS:        msg - String
#DESCRIPTION:   Will decode a msg from morse code to readable english using a binary heap data structure.
#RETURNS:       morseString.lower() - the decoded message in lower case.
def decode_bt(msg):   
    msg = msg.upper()
    morseChars = msg.split()

    morseString = ""

    for char in morseChars:
        i = 1
        if char != "/" and char != " ":
            for morseChar in char:        
                if morseChar == ".":
                    i = 2 * i
                elif morseChar == "-":
                    i = 2 * i + 1

            morseString += letters_bh[i-1]

        else:
            morseString += " "

    return morseString.lower()

#FUNCTION:      encode_ham(sender, reciever, msg)
#PARAMS:        sender - String, reciever - String, msg - String
#DESCRIPTION:   Will encode a msg to morse code from readable english using the ham radio conversation standard.
#RETURNS:       encode(f"{reciever}de{sender}={msg}=(") - the encoded message.
def encode_ham(sender, reciever, msg):
    return encode(f"{reciever}de{sender}={msg}=(")

#FUNCTION:      encode_ham(sender, reciever, msg)
#PARAMS:        msg - String
#DESCRIPTION:   Will decode morse code to readable english using the ham radio conversation standard.
#RETURNS:       (sender, reciever, msg) - a tuple contianing the sender, reciever and decoded message.
def decode_ham(msg):
    decoded_morse = decode_bt(msg)
    sender = decoded_morse.split("=")[0].split("de")[1]
    reciever = decoded_morse.split("=")[0].split("de")[0]
    msg = decoded_morse.split("=")[1]
    return (sender, reciever, msg)

async def send_echo(sender, msg):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())
        # Get the client_id from the join message
        if message['type'] == 'join_evt':
            client_id = message['client_id']
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message")

        async def send_message(websocket, message, client_id):
            outward_message = {
                'client_id': client_id,
                'type': 'morse_evt',
                'payload': message
            }
            await websocket.send(json.dumps(outward_message))

        async def recv_message(websocket):
            message = json.loads(await websocket.recv())
            return message['payload']

        # Send a ping to the server
        await send_message(websocket, encode_ham(sender, 'echo', msg), client_id)
        # Wait for the 'ping' response from the server
        response = await recv_message(websocket)

        return decode_ham(response)

async def send_time(sender):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())
        # Get the client_id from the join message
        if message['type'] == 'join_evt':
            client_id = message['client_id']
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message")

        async def send_message(websocket, message, client_id):
            outward_message = {
                'client_id': client_id,
                'type': 'morse_evt',
                'payload': message
            }
            await websocket.send(json.dumps(outward_message))

        async def recv_message(websocket):
            message = json.loads(await websocket.recv())
            return message['payload']

        # Send a ping to the server
        await send_message(websocket, encode_ham(sender, 'time', 'hello world'), client_id)
        # Wait for the 'ping' response from the server
        response = await recv_message(websocket)
        
        return decode_ham(response)