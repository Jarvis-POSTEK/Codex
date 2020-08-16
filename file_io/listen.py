"""
    Author: Rylee Bers
    Last modified: 8/2/2020

    This file contains the listen class. It's purpose is to listen for a command from the user,
    then pass back to codex functions
"""

import copy

class Listen(object):
    """
    Initialization of listen class

    @instance wordbank the list of words that can be converted to commands
    """
    def __init__(self):
        self.wordbank = ['add', 'delete', 'undo','modify']




    """
    Autofills a word as user is typing by process of elimination
    Future use might involve giving the user the option to click the word instead of have it autofill

    @instance letters the substring of the word the user has typed so far
    """
    def auto_fill(self, letters):
        potentialwords = self.wordbank.copy()
        wrong_words = []

        #Check potential word letter by letter. If there is any irregularity remove the word from potential
        #list and move on to next word
        for word in potentialwords:
            for c in range(len(letters)):
                if letters[c] != word[c]:
                    wrong_words.append(word)
                    break
        
        for words in wrong_words:
            potentialwords.remove(words)
        wrong_words.clear()
        
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

    @testedword the word the user has typed
    @potentialword the word we are determining if there is a match or not
    """
    def percentage(self, testedword, potentialword):
        looprange = len(testedword)
        if len(potentialword) < looprange:
            looprange = len(potentialword)

        correct = 0
        for n in range(looprange):
            if testedword[n] == potentialword[n]:
                correct += 1

        return correct/len(potentialword)





    """
    If autofill could not find a match, autocorrect chooses a word based on the user's fully typed command
    The word that is chosen will be closest in match to the misspelled word
    If there are two words that are both equal in percentage accuracy to the misspelled word, the first one
    found will be chosen

    @instance letters the text the user has typed that needs to be matched with a word
    """
    def auto_correct(self, letters):
        maxpercentword = ""
        maxpercent = 0
        for word in self.wordbank:
            percentmatch = self.percentage(letters, word)
            if percentmatch > maxpercent:
                maxpercent = percentmatch
                maxpercentword = word

        return maxpercentword








    



        


