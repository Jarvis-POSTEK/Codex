"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file is created to test the program. Commands are passed in directly
since voice recongization haven't been implemented

"""
from project_management import command_central
import file_io
import time
import fileinput
import platform
from file_io import listen


test = listen()
print test.autofill("mod")




