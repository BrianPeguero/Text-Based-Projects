def getInput():
    phrase = raw_input("Please enter you phrase: ")
    return phrase

def constant(word):
    return word[1:] + word[0] + "ay"

def twoConstants(word):
    index = 0
    while word[index] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        index+=1
    return word[index:] + word[0:index] + "ay"

def vowel(word):
    return word + "ay"


def translate(phrase):
    if " " in phrase:
        pigLatin = ""
        listOfWords = phrase.split(" ")
        for word in listOfWords:
            if word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                pigLatin += vowel(word) + " "
            elif word[0] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                pigLatin += constant(word) + " "
            else:
                pigLatin += twoConstants(word) + " "
        display(pigLatin)
    else:
        if phrase[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            newWord = vowel([hrase])
        elif phrase[0] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            newWord = constant(phrase)
        else:
            newWord = twoConstants(phrase)
        display(newWord)
    
    
def display(pigLatin):
    print(pigLatin)

def main():
    phrase = getInput()
    pigLatinList = translate(phrase)

main()