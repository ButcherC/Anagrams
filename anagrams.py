# anagrams.py
import sys
import random
import itertools

# must use command-line arguments
# no command line agrs, length of sys.argv is 1 (sys.argv[0])
# pick a random 6 letter word from dictionary
# ugly and inefficient but it works.
with open("words.txt") as f:
    wordList = [line.strip() for line in f]
threeL = []
fourLeft = []
fiveLeft = []
sixLeft = []
wordsGuessed = []
possibleWords = []

length = len(sys.argv)
if(length == 1):
    #get random word from list of len 6
    testWord = random.choice(wordList)
    while(len(testWord) != 6):
       testWord = random.choice(wordList)
    print("TEST: base word is ", testWord)
    str_var = list(testWord)
    random.shuffle(str_var)
    guessString = ''.join(str_var)

    three = map("".join, itertools.permutations(str_var, 3))
    for x in three:
        if((x in wordList) and (x not in threeL)):
            threeL.append(x)
            possibleWords.append(x)
    
    four = map("".join, itertools.permutations(str_var, 4))
    for x in four:
        if((x in wordList) and (x not in fourLeft)):
            fourLeft.append(x)
            possibleWords.append(x)
    five = map("".join, itertools.permutations(str_var, 5))
    for x in five:
        if((x in wordList) and (x not in fiveLeft)):
            fiveLeft.append(x)
            possibleWords.append(x)

    six = map("".join, itertools.permutations(str_var, 6))
    for x in six:
        if((x in wordList) and (x not in sixLeft)):
            sixLeft.append(x)
            possibleWords.append(x)
    guess = None
    while(guess != 'q'):
        print(guessString, ":")
        print(len(threeL), " 3-letter words left.")
        print(len(fourLeft), " 4-letter words left.")
        print(len(fiveLeft), " 5-letter words left.")
        print(len(sixLeft), " 6-letter words left.")
        print(" ")
        guess = input("Enter a guess: ")
        if((guess in wordList) and (guess not in wordsGuessed) and (guess in possibleWords) and (guess != "q")):
            print("Correct!")
            wordsGuessed.append(guess)
            for i in wordsGuessed:
                if(i in threeL):
                    threeL.remove(i)
                elif(i in fourLeft):
                    fourLeft.remove(i)
                elif(i in fiveLeft):
                    fiveLeft.remove(i)
                elif(i in sixLeft):
                    sixLeft.remove(i)
        elif((len(threeL) == 0) and (len(fourLeft) == 0) and (len(fiveLeft) == 0) and (len(sixLeft) == 0)):
            print("All possible words guessed!")
            guess = "q"
        else:
            print("Incorrect or already guessed.")
        print("Guessed Words: ", "\n", wordsGuessed, "\n")
    possibleWords.sort()
    possibleWords.sort(key=len)
    print("Possible words:", "\n",possibleWords)
    
# if one command line arg, length of sys.argv is 2 (sys.argv[1])
elif(length == 2):
    baseWord = sys.argv[1]
    print("TEST: base word is ", baseWord)
    str_var = list(baseWord)
    random.shuffle(str_var)
    guessString = ''.join(str_var)
    three = map("".join, itertools.permutations(str_var, 3))
    for x in three:
        if((x in wordList) and (x not in threeL)):
            threeL.append(x)
            possibleWords.append(x)
    
    four = map("".join, itertools.permutations(str_var, 4))
    for x in four:
        if((x in wordList) and (x not in fourLeft)):
            fourLeft.append(x)
            possibleWords.append(x)
    five = map("".join, itertools.permutations(str_var, 5))
    for x in five:
        if((x in wordList) and (x not in fiveLeft)):
            fiveLeft.append(x)
            possibleWords.append(x)

    six = map("".join, itertools.permutations(str_var, 6))
    for x in six:
        if((x in wordList) and (x not in sixLeft)):
            sixLeft.append(x)
            possibleWords.append(x)
    guess = None
    while(guess != 'q'):
        print(guessString, ":")
        print(len(threeL), " 3-letter words left.")
        print(len(fourLeft), " 4-letter words left.")
        print(len(fiveLeft), " 5-letter words left.")
        print(len(sixLeft), " 6-letter words left.")
        print(" ")
        guess = input("Enter a guess: ")
        if((guess in wordList) and (guess not in wordsGuessed) and (guess in possibleWords) and (guess != "q")):
            print("Correct!")
            wordsGuessed.append(guess)
            for i in wordsGuessed:
                if(i in threeL):
                    threeL.remove(i)
                elif(i in fourLeft):
                    fourLeft.remove(i)
                elif(i in fiveLeft):
                    fiveLeft.remove(i)
                elif(i in sixLeft):
                    sixLeft.remove(i)
        elif((len(threeL) == 0) and (len(fourLeft) == 0) and (len(fiveLeft) == 0) and (len(sixLeft) == 0)):
            print("All possible words guessed!")
            guess = "q"
        else:
            print("Incorrect or already guessed.")
        print("Guessed Words: ", "\n", wordsGuessed, "\n")
    possibleWords.sort()
    possibleWords.sort(key=len)
    print("Possible words:", "\n",possibleWords)
        
# sys.argv[1] is the base word to use for puzzle

