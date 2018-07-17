def getInput():
    phrase = raw_input("Please enter the phrase you would like to check is a palindrome: ")
    return phrase

def reversePhrase(phrase):
    reversedPhrase = ""
    for x in range(len(phrase)-1, -1, -1):
        reversedPhrase += phrase[x]
    return reversedPhrase

def checkIfPalindrome(phrase, reversedPhrase):
    return phrase == reversedPhrase

def display(validate):
    print(validate)

def main():
    phrase = getInput()
    reversedPhrase = reversePhrase(phrase)
    validate = checkIfPalindrome(phrase, reversedPhrase)
    display(validate)

main()