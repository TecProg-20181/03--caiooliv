import random
import string
import sys
import os
import logging


WORDLIST = "words.txt"
LOGLIST = "loglist.log"

logging.basicConfig(filename=LOGLIST,level=logging.DEBUG)
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
            answer.lower()
            while (answer != 'y' and answer != 'n'):
                answer = raw_input("Invalid answer, please use 'y' for yes and 'n' for no\n")
                answer.lower()
                logging.info("Validate answer to change word")

            if(answer == 'y'):
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

    inFile = fileChecker()

    # line: string
    line = inFile.readline()
    logging.info("Read file correctly")
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return random.choice(wordlist)


def fileChecker():
    try:
        inFile = open(WORDLIST, 'r', 0)
        logging.info("Try open file")

    except IOError:
        print("Error in open file, the program will close")
        logging.info("Failed to open file")
        sys.exit(0)

    if(os.path.getsize(WORDLIST) == 0):
        print("File is empty, the program will close")
        logging.info("File empty")
        sys.exit(0)

    return inFile


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
        while not letter.isalpha():
            letter = raw_input("Invalid character, Please use a letter: ")
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
