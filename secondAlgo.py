firstLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
secondLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
thirdLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
fourthLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def feedbackAnalisys(guessedWord, remaningChances):
    feedback = input("Guessed Word: "+ ''.join(guessedWord) + '\nRemaining Chances: ' + str(remaningChances) + "\nFeedback: " )
    while len(feedback) != 4:
        feedback = input("Feedback must have 4 characters\nFeedback: ")
    if feedback == '====':
        print("Word Guessed!")
        return True
    for index in range(len(feedback)):
        if feedback[index] == '=':
            continue
        elif feedback[index] == '+':
            if index == 0:
                firstLetter.remove(guessedWord[index])
            elif index == 1:
                secondLetter.remove(guessedWord[index])
            elif index == 2:
                thirdLetter.remove(guessedWord[index])
            elif index == 3:
                fourthLetter.remove(guessedWord[index])
            guessedWord[index] = '0'
        elif feedback[index] == '-':
            firstLetter.remove(guessedWord[index])
            secondLetter.remove(guessedWord[index])
            thirdLetter.remove(guessedWord[index])
            fourthLetter.remove(guessedWord[index])
            guessedWord[index] = '0'
        else:
            print("Invalid Feedback")
            feedbackAnalisys(guessedWord, remaningChances)
    return guessedWord

def backtrackingWordle(guessedWord):
    remaningChances = 9
    while (True and remaningChances >= 0):
        result = feedbackAnalisys(guessedWord,remaningChances)
        if result == True:
            break
        guessedWord = result
        remaningChances -= 1
        for index in range(4):
            if guessedWord[index] == '0':
                if index == 0:
                    i = 0
                    while firstLetter[i] in guessedWord:
                        i+=1
                    guessedWord[index] = firstLetter[i]
                elif index == 1:
                    i = 0
                    while secondLetter[i] in guessedWord:
                        i+=1
                    guessedWord[index] = secondLetter[i]
                elif index == 2:
                    i = 0
                    while thirdLetter[i] in guessedWord:
                        i+=1
                    guessedWord[index] = thirdLetter[i]
                elif index == 3:
                    i = 0
                    while fourthLetter[i] in guessedWord:
                        i+=1
                    guessedWord[index] = fourthLetter[i]
    if remaningChances == 0:
        print("Can't guess the word")
                    
if __name__ == '__main__':
    firstGuess = ['a', 'b', 'c', 'd']
    backtrackingWordle(firstGuess)
