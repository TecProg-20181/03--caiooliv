import random
import string


WORDLIST = "words.txt"


class Word():

    def isWordGuessed(self, secretWord, lettersGuessed):
        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):

        self.guessed = ''

        return self.guessed

    def getAvailableLetters(self):

        self.available = string.ascii_lowercase

        return self.available

    def getDifferentLetters(self, secretWord):

        differentLetters = set(secretWord)
        print'Number of different letters in tha word', len(differentLetters)

    def changeWord(self, secretWord):

        if(len(secretWord) > 8):
            answer = raw_input("The word has more than 8 letters, do you want to change the secret word ? [Y/N]\n")
            if(answer == 'y' or answer == 'S'):
                secretWord = loadWords().lower()
                self.changeWord(secretWord)
                return secretWord
            else:
                return secretWord
        else:
            return secretWord


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return random.choice(wordlist)


def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    word = Word()

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    word.getDifferentLetters(secretWord)
    print '-------------'

    while word.isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        available = word.getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = word.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = word.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = word.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if word.isWordGuessed(secretWord, lettersGuessed) is True:
            print 'Congratulations, you won!'
        else:
            print "Sorry, you ran out of guesses."\
                  + "The word was ", secretWord, "."


def main():
    word = Word()
    secretWord = loadWords().lower()
    hangman(word.changeWord(secretWord))


main()
