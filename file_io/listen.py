"""
    Author: Rylee Bers
    Last modified: 7/12/2020

    This file contains the listen class. It's purpose is to listen for a command from the user,
    then convert the command in a CommandBlock object
"""

#need to edit later
from gtts import gTTS
import speech_recognition as sr
import os
import re
import smtplib
import sphinx
import smtplib
import pocketsphinx



#some thoughts for future edits of commandBlock class and this class:

#In the future, I think these two classes should take into account the user wanting 
#to add non variable or function things such as "|, &, ==, ect..."
#I also think that the commandBlock paramters such as "type" and "name" should also be associated with
#functions too, since the user will probably create their own function eventually and need to give it
#a return type and name




class listen:
    def __init__(self):
        #directory to find potential parameters for commandBlock

        #dictionaries are used so that multiple phrases could point to the same meaning
        #dictionaries are used when there is a predefined list of options the user can choose from

        #a list is used when the commandBlock parameter is made up by the user and not from a predefined list


        #directory of user actions
        self.actiondict = {"add function"         : "add",
                           "add variable"         : "add",
                           "remove"               : "delete",
                           "delete"               : "delete",
                           "get rid of"           : "delete",
                           "take away"            : "delete",
                           "change"               : "modify",
                           "modify"               : "modify",
                           "adjust"               : "modify",
                           "undo"                 : "undo",
                           "exit"                 : "exit"
            #more to come... maybe add #include or a create new function action, or add parameters to function
                           }


        #directory of varibale types                   
        self.typedict = {"integer"                : "int",
                         "int"                    : "int",
                         "double"                 : "double",
                         "character"              : "char",
                         "char"                   : "char",
                         "string"                 : "string",
                         "unsigned integer"       : "unsigned int",
                         "unsigned int"           : "unsigned int"
                         #more to come.... 
                        }


        #directory of existing c functions
        self.funcdict = {"for loop"               : "for",
                         "for"                    : "for",
                         "while loop"             : "while",
                         "while"                  : "while",
                         #more to come....
                        }
        

              
        #list with phrases that indicate the following number, string, char, ect. is a value to a variable
        self.valuelist = ['equals', 'with value of', 'set value to']


        #list with phrases that indicate the following number represents what line to modify
        self.linelist = ['line', 'on', 'at']

    
        #list with phrases that indicate the following word is the name of a variable 
        #I might add some more flexability in the future so that the user can give a variable
        #a name without using a keyword
        self.namelist = ['named', 'called']

        #self.columnlist = []





    """
        When the user creates a new function, it can be added to the directory of existing c functions

        @instance function the function the user created
        @instance funcname the name of the function that will be linked with the function (the key in the directory)
    """
    def addToFuncdict(self, function, funcname):
        self.funcdict[funcname] = function





    """ 
        The end goal for this function in the future is that it will be able to speak to the user
        This was taken directly from desktopAssistant

        @instance audio what the computer will speak to the user
    """
    def talkToUser(self, audio):
        "speaks audio passed as argument"

        print(audio)
        for line in audio.splitlines():
            os.system(audio)

        #  use the system's inbuilt say command instead of mpg123
        #  text_to_speech = gTTS(text=audio, lang='en')
        #  text_to_speech.save('audio.mp3')
        #  os.system('mpg123 audio.mp3')






    """ 
        Function that converts audio into a single string of the user's command
        command is then pushed to parseCommand and the interpreted command is returned
    """
    def listenToUser(self):
        #listening to the user
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")     # it might be annoying hearing "listening" a million times a day so just print it
            audio = r.listen(source)
        command = r.recognize_sphinx(audio)

        try:
            # recognize speech using Sphinx
            # benefit: Sphinx does not require internet connection
            # drawback: Sphinx is not consistently accurate, and appears to not listen while interpretting audio 
            print("We heard: " + command)
        except sr.UnknownValueError:
            talkToUser("Audio was misunderstood. Please repeat.")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        return parseCommand(command) 





    """ 
        Function that converts a single string to a CommandBlock object
        helper function for listenToUser()

        @instance command the string of the user's command to be parsed into a CommandBlock object
    """
    def parseCommand(self, command):
        #initialize commandBlock object
        parsedCommand = commandBlock()

        #extract the needed information from the command
        for key in self.actiondict.keys():
            if key in command:
                parsedCommand(action = self.actiondict[key])

        for key in self.typedict.keys():
            if key in command:
                parsedCommand(type = self.typedict[key])

        for key in self.funcdict:
            if key in command:
                parsedCommand(func_name = self.funcdict[key])

        for key in self.valuelist:
            if key in command:
                parsedCommand(value = extractWord(command, key))

        for key in self.linelist:
            if key in command:
                parsedCommand(line = extractWord(command, key))

        for key in self.namelist:
            if key in command:
                parsedCommand(name = extractWord(command, key))



        #return commandBlock object to be used by Jarvis's code
        return parsedCommand





    """
        Helper function for parseCommand()
        uses a keyword in the user's command and extracts the word directly after 

        Example: "Add function to line four"
                 This is the user's command. The keyword is "line"
                 We want to extract "four" from this phrase and add it to line parameter of commandBlock object

        @instance command the user's spoken command
        @instance keyword the word or phrase that precedes the word we need to extract
    """
    def extractWord(self, command, keyword):
        extracted = command.split(keyword)
        del extracted[0]
        extracted.split(" ")

        return extracted[0]





