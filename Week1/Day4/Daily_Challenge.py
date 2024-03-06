from string import ascii_letters

matrix = [
    [7,"i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i"," ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

def decoding_message():
    '''Decodes the message from the matrix'''
    message_for_neo = ''
    index = 0
    last_latter = ""
    for _ in range(0, 3):
        for item in matrix:
            letter = item[index]

            # check if string and alpha letter to avoid int values
            if isinstance(letter, str) and letter in ascii_letters:
                message_for_neo += letter
            elif last_latter not in ascii_letters:
                message_for_neo += " "

            last_latter = letter

        index += 1
    # removes and trim double spaces
    return " ".join(message_for_neo.split())


print(decoding_message())
