ALHPHABET = [chr(i) for i in range(97, 123)]

notInLetters = {0: list(), 1: list(), 2: list(), 3: list()}
notInPlaces = {0: list(), 1: list(), 2: list(), 3: list()}
guessedWord = ['0', '0', '0', '0']


def feedbackAnalisys(guessedWord, remaningChances):
    feedback = input("Guessed Word: " + ''.join(guessedWord) +
                     '\nRemaining Chances: ' + str(remaningChances) + "\nFeedback: ")
    while len(feedback) != 4:
        feedback = input("Feedback must have 4 characters\nFeedback: ")
    if feedback == '====':
        return True
    for index in range(len(feedback)):
        if feedback[index] == '=':
            value = ALHPHABET.copy()
            value.remove(guessedWord[index])
            notInLetters[index] = value
        elif feedback[index] == '+':
            notInPlaces[index].append(guessedWord[index])
        elif feedback[index] == '-':
            for i in range(4):
                notInLetters[i] += guessedWord[index]
        else:
            print("Invalid Feedback")
            feedbackAnalisys(guessedWord, remaningChances)
    return False


def backtrackingWordle(index):
    global guessedWord
    if '0' not in guessedWord:
        return True
    for letter in ALHPHABET:
        if letter in guessedWord or letter in notInLetters[index] or letter in notInPlaces[index]:
            continue
        guessedWord[index] = letter
        if backtrackingWordle(index + 1):
            return True
        guessedWord[index] = '0'
    return False


def display():
    remaningChances = 9
    while remaningChances >= 0:
        global guessedWord
        guessedWord = ['0', '0', '0', '0']
        backtrackingWordle(index=0)
        if feedbackAnalisys(guessedWord, remaningChances):
            print("Word Guessed!")
            break
        remaningChances -= 1
    if remaningChances == 0:
        print("Can't guess the word")


if __name__ == '__main__':
    display()
