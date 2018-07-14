def getInput():
    word = raw_input("Please enter a string you want to reverse: ")
    return word

def reverseString(word):
    newString = ""
    for x in range(len(word)-1, -1, -1):
        newString+=word[x]
    return newString

def display(reversedString):
    print(reversedString)

def main():
    word = getInput()
    reversedString = reverseString(word)
    print(reversedString)

main()