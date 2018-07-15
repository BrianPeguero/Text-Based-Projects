def getInput():
    phrase = raw_input("Please enter you phrase: ")
    return phrase

def constant(word):

def twoConstants(word):

def vowel(word):


def translate(phrase):
    listOfWords = phrase.split(" ")
    for word in listOfWords:
        if word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vowel(word)
        elif word[0] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            constant(word)
        else:
            twConstants(word)
    

def main():
    phrase = getInput()


main()