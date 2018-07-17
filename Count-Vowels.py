def getInput():
    phrase = raw_input("Please enter your phrase: ")
    return phrase

def vowelCount(phrase):
    count = 0
    for x in phrase:
        if x in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            count+=1
    display(count)

def vowelFrequency(phrase):
    freqDict = {"A":0, "E":0, "I":0, "O":0, "U":0}
    for x in phrase:
        if x in ["a", "A"]:
            freqDict["A"] += 1
        elif x in ["e", "E"]:
            freqDict["E"] += 1
        elif x in ["i", "I"]:
            freqDict["I"] += 1
        elif x in ["o", "O"]:
            freqDict["O"] += 1
        elif x in ["u", "U"]:
            freqDict["U"] += 1
    display(freqDict)
    
def display(count):
    print(count)

def main():
    phrase = getInput()
    vowelCount(phrase)
    vowelFrequency(phrase)


main()