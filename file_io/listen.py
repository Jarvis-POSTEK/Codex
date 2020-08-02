"""
    Author: Rylee Bers
    Last modified: 8/2/2020

    This file contains the listen class. It's purpose is to listen for a command from the user,
    then pass back to codex functions
"""

import copy

class listen(object):
    """
    Initialization of listen class

    @instance wordbank the list of words that can be converted to commands
    """
    def __init__(self, wordbank):
        self.wordbank = ['add', 'modify', 'delete', 'undo']




    """
    Autofills a word as user is typing by process of elimination
    Future use might involve giving the user the option to click the word instead of have it autofill

    @instance letters the substring of the word the user has typed so far
    """
    def autofill(self, letters):
        potentialwords = self.wordbank.copy()

        #Check potential word letter by letter. If there is any irregularity remove the word from potential
        #list and move on to next word
        for word in potentialwords:
            for c in range(len(letters)):
                if letters[c] != word[c]:
                    del word
                    break

        #return word if there is only one choice left
        if len(potentialwords) == 1:
            return potentialwords[0]
        else:
            return -1


    
    """
    Adds new word to wordbank list. 

    @instand neword the word to add to list
    """
    def add_word(self, newword):
        self.wordbank.insert(newword)




    """
    Helper function for function that will autocorrect if a word is a certain percentage match of a word from wordbank

    @instance correct number of characters that match word
    @instance numletters the total number of characters in the word that is being analyzed
    """
    def percentage(self, correct, numletters):
        pass

    



        


