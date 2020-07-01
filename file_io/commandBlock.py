"""
    Author:Jarvis Lu
    Last modified: 6/17/2020

    This file contains the command_block calss, the class that contains all the information
that needs to be passed down to individual functions and sub-classes for actions to be performed.
"""


""" 
    Initialization of the CommandBlock class
    This is a test to see how fast the changes can be visualized 

    @instance type the type of value this variable will hold
    @instance name the name of the variable
    @instance value the value that this variable will hold, doesn't need to be specified
"""
class CommandBlock(object):
    def __init__(self, action = None, type = None, name = None, line = None, column = None, 
    value = None, func_name = None):
        self.action = action
        self.type = type
        self.name = name
        self.line = line
        self.column = column
        self.value = value
        self.func_name = func_name

    def modify_info(self, action = None, type = None, name = None, line = None, column = None, 
    value = None, func_name = None):
        self.action = action
        self.type = type
        self.name = name
        self.line = line
        self.column = column
        self.value = value
        self.func_name = func_name

# I added type and column number to each of these functions. Feel free to remove
# This is Rylee btw :)

