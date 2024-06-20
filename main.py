# const value for the all english alphabets
ALHPHABET = [chr(i) for i in range(97, 123)]

# global variables
# list of alphabets that are not in the word
notInLetters = {0: list(), 1: list(), 2: list(), 3: list()}
# list of alphabets that are not in the correct place
notInPlaces = {0: list(), 1: list(), 2: list(), 3: list()}
# list of the guessed letters
guessedWord = ['0', '0', '0', '0']


def feedbackAnalisys(guessedWord, remaningChances):
    '''
    Function to get the feedback from the user and update the notInLetters and notInPlaces
    :param guessedWord: list of the guessed word
    :param remaningChances: number of remaning chances
    :return: True if the word is guessed, False otherwise
    '''
    feedback = input("Guessed Word: " + ''.join(guessedWord) +
                     '\nRemaining Chances: ' + str(remaningChances) + "\nFeedback: ")
    # check if the feedback is valid, if not then ask again
    while len(feedback) != 4:
        feedback = input("Feedback must have 4 characters\nFeedback: ")
    if feedback == '====':
        return True
    for index in range(len(feedback)):
        if feedback[index] == '=':
            # only this letter can be in this place, add all other letters from the notInLetters for this place
            value = ALHPHABET.copy()
            value.remove(guessedWord[index])
            notInLetters[index] = value
        elif feedback[index] == '+':
            # the letter is not in this place, but in the word,
            notInPlaces[index].append(guessedWord[index])
        elif feedback[index] == '-':
            # the letter is not in any place
            for i in range(4):
                notInLetters[i] += guessedWord[index]
        else:
            print("Invalid Feedback")
            feedbackAnalisys(guessedWord, remaningChances)
    return False


def backtrackingWordle(index):
    '''
    Recursive function to guess the word using backtracking algorithm
    :param index: index of the current letter
    :return: True if the all letters are guessed, False otherwise
    '''
    global guessedWord

    if index == 4:
        # all letters are guessed
        return True
    for letter in ALHPHABET:
        # check if the letter is already exist in previous guesses, 
        # check if the letter is in notInLetters or notInPlaces based on the index
        # find the first suitable letter for the current index from the ALHPHABET
        if letter in guessedWord or letter in notInLetters[index] or letter in notInPlaces[index]:
            continue
        guessedWord[index] = letter
        if backtrackingWordle(index + 1):
            return True
        # if the word is not guessed, then reset the guessedWord[index] to 0
        guessedWord[index] = '0'
    # if the word is not guessed, then return False
    return False


def display():
    '''
    Main function to display the wordle game
    It calls the backtrackingWordle function and feedbackAnalisys function in a loop until the word is guessed or the chances are over'''
    remaningChances = 9
    # the game will continue until the 10 chances are over
    while remaningChances >= 0:
        global guessedWord
        # reset the guessedWord to 0000 to start the new game
        guessedWord = ['0', '0', '0', '0']
        # call the backtrackingWordle function to guess the word based on the feedbacks (if any)
        backtrackingWordle(index=0)
        # check if the word is guessed or not
        if feedbackAnalisys(guessedWord, remaningChances):
            print("Word Guessed!")
            break
        remaningChances -= 1
    if remaningChances == 0:
        # chances are over
        print("Can't guess the word")


if __name__ == '__main__':
    display()
