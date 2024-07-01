'''
CONSTANTS:
    ALPHABET = ['a', 'b', 'c', ..., 'z']

GLOBAL VARIABLES:
    notInPlaces = {0: [], 1: [], 2: [], 3: []}
    guessedWord = ['0', '0', '0', '0']

FUNCTION feedbackAnalysis(guessedWord, remainingChances):
    PRINT Guessed Word and Remaining Chances and ask for feedback

    IF feedback == '====':
        Word Guessed Successfully, return True

    FOR index FROM 0 TO 3:
        IF feedback[index] == '=':
            ADD all other letters to notInPlaces[index]
        ELSE IF feedback[index] == '+':
            Add the letter to the non promising letters in level index (notInPlaces[index])
        ELSE IF feedback[index] == '-':
            Add the letter to the non promising letters in all levels (notInPlaces[0..3])

    RETURN False cause word not guessed

FUNCTION backtrackingWordle(index):
    IF index == 4:
        RETURN True

    FOR letter IN ALPHABET:
        IF letter IN guessedWord OR letter IN notInPlaces[index]:
            CONTINUE

        guessedWord[index] = letter

        IF backtrackingWordle(index + 1):
        RETURN True

        guessedWord[index] = '0' 
    
    RETURN False

FUNCTION display():
    WHILE there are remaining chances:
        guessedWord = ['0', '0', '0', '0']
        CALL backtrackingWordle(0)

        IF feedbackAnalysis(guessedWord, remainingChances):
            PRINT "Word Guessed!"
            BREAK

        decrement remaining chances
    IF chances are over:
        PRINT "Can't guess the word"

MAIN:
    CALL display()
'''