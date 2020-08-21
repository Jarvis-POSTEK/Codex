"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file contains the CommandCentral class.  
    Command central takes in command parse by voice recoginizer. The main
purpose command central is trying to serve is passing piping command down.
This will serve as a bridge between voice recoginizer and the file_i/o

"""

from .import proj_manage
from file_io import writer
from file_io import files
from os.path import expanduser
import time

""" 
    Initialization of the command central class

    @param platform The platform of the machine that is running this application
    @instance platform keeps track of the platform this program is running on
    @instance project points to the current project this program is working on
    @instance langauge determines which language the program should output 
    @instance current_file The last file the user was editing 
"""
class CommandCentral(object):
    def __init__(self, platform):
        self.platform = platform
        self.project = None
        self.language = None
        self.current_file = None

    """ 
        Create a new Project class object
        @param work_space_path The path passed in from the user. Passed in as a list of the name
            of the directories to change into.
    """
    def create_new_project(self, work_space_path):
        self.project = proj_manage.Project(work_space_path, self.platform)
        #Since creating a new project prompts visual studio code to open it
        #this program sleeps a second for visual studio code to load
        time.sleep(1)

    """ 
        This function is used to add a file to the project
        @param filename the name of the file to be created
    """
    def add_file(self, filename):
        self.project.create_new_file(filename)
        # self.project.open_file(filename)
        self.current_file = self.project.return_file(filename)
    
    """ 
        For the file that the user was editing, this function clears that file
    """
    def clear_file(self):
        self.current_file.clear()        

    """ 
        Remove a given file
        @param filename the name of the file to be removed
    """
    def remove_file(self, filename):
        self.project.remove_file(filename)
    
    """ 
        Add the includes at the top of the file
        @param include_name name of the header file that needs to be included
    """
    def add_include(self, include_name):
        self.current_file.add_std_include(include_name)
        self.current_file.write_output()

    """ 
        Add a function to the file the user was last editing
        @param func_name name of the function
        @param return_type what type of value would be returned by the function
        @param func_type whether it is a function definition or a declaration
    """
    def add_func(self, func_name, return_type, func_type):
        #file handles the command and implments the nesscary changes
        self.current_file.add_function(func_name, return_type, func_type)
        #after the changes have been implemented, write the output to file
        self.current_file.write_output()
        
    """ 
        Add content to the body of a function
        @param CommandBlock An instance of the CommandBlock class. This class
            is then used to pass information down the line
    """
    def add_to_func_body(self, command_line, func_name = None):
        self.current_file.add_to_function_body(command_line, func_name)
        self.current_file.write_output()

