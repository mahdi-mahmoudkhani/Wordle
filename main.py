allLetters = {'a': [0, 1, 2, 3], 'b': [0, 1, 2, 3], 'c': [0, 1, 2, 3], 'd': [0, 1, 2, 3], 'e': [0, 1, 2, 3], 'f': [0, 1, 2, 3], 'g': [0, 1, 2, 3], 'h': [0, 1, 2, 3], 'i': [0, 1, 2, 3], 'j': [0, 1, 2, 3], 'k': [0, 1, 2, 3], 'l': [0, 1, 2, 3], 'm': [0, 1, 2, 3], 'n': [0, 1, 2, 3], 'o': [0, 1, 2, 3], 'p': [0, 1, 2, 3], 'q': [0, 1, 2, 3], 'r': [0, 1, 2, 3], 's': [0, 1, 2, 3], 't': [0, 1, 2, 3], 'u': [0, 1, 2, 3], 'v': [0, 1, 2, 3], 'w': [0, 1, 2, 3], 'x': [0, 1, 2, 3], 'y': [0, 1, 2, 3], 'z': [0, 1, 2, 3]}

def feedbackAnalisys(guessedWord, remaningChances):
    feedback = input("Guessed Word: "+  guessedWord + '\nRemaining Chances: ' + str(remaningChances) + "\nFeedback: " )
    while len(feedback) != 4:
        feedback = input("Feedback must have 4 characters\nFeedback: ")
    if feedback == '====':
        print("Word Guessed!")
        return True
    for index in range(len(feedback)):
        if feedback[index] == '=':
            allLetters[guessedWord[index]] = [index]
        elif feedback[index] == '+':
            allLetters[guessedWord[index]].remove(index)
        elif feedback[index] == '-':
            allLetters[guessedWord[index]] = [-1 for _ in range(5)]
        else:
            print("Invalid Feedback")
            feedbackAnalisys(guessedWord, remaningChances)

def backtrackingWordle(guessedWord):
    remaningChances = 9
    while (not feedbackAnalisys(guessedWord, remaningChances) and remaningChances > 0):
        global allLetters
        allLetters = {k: v for k, v in sorted(allLetters.items(), key=lambda item: len(item[1]))}
        remaningChances -= 1
        guessedWord = '0123'
        guessed = 0
        while not guessed:
            for letter in allLetters:
                if guessed == 4:
                    guessed = True
                    break
                if allLetters[letter] == [-1 for _ in range(5)]:
                    continue
                elif len(allLetters[letter]) == 1:
                    guessedWord = guessedWord.replace(str(allLetters[letter][0]), letter, 1)
                    guessed += 1
                else:
                    for int in allLetters[letter]:
                        if guessedWord[int].isdigit():
                            guessedWord = guessedWord.replace(str(int), letter, 1)
                            guessed += 1
                            break
    if remaningChances == 0:
        print("Can't guess the word")
                    
if __name__ == '__main__':
    firstGuess = 'abcd'
    backtrackingWordle(firstGuess)
