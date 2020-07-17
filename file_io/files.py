"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file contains the File class. The majority of editing of a file's
content happens within the file class

"""
from .import include
from .import function
from .import variable
from file_io import writer

""" 
    Initialization of the File class

    @param file_path path to the file that this writer class is going to write to 
    @instance function_dict a dictionary to keep all functions so a specifc func can be 
        returned given a func name
    @instance current_function the last function the user was editing. This is implemented
        so the user can edit the same function without the need to specify it again
    @instance writer the writer class this file class uses to modify the actual file
    @instance include the include class that will host all the different includes needed 
        by this file
    @instance output the content of this file. Changes will be made to the self.output list
        then it would be passed to writer to write to file
    @instance tracker keeps track of everything within the file. Whenever a new object is created
        it is placed in the tracker depending on its position in the file. When the output is 
        being generated, output will be generated sequencially from the first item in tracker 
        to the last 
"""
class File(object):
    def __init__(self, file_path):
        self.function_dict = {}
        self.current_function = None
        self.writer = writer.Writer(file_path)
        self.include = include.Include()   
        self.output = []
        self.tracker = []
        
    def generate_output(self):
        del self.output[:]
        for token in self.tracker:
            token.generate_output(self.output)
            self.output.append("")

    """ 
        Writes the content of self.output to the file
    """  
    def write_output(self):
        self.generate_output()
        self.writer.write(self.output)

    """ 
        Adds include to output
        @param include the name fo the library to be included 
    """
    def add_std_include(self, include):
        if self.include not in self.tracker:
            self.tracker.append(self.include)
        self.include.add_std_include(include, self.output)

        
    """ 
        Add a function to the file
        @param func_name name of the function to be added
        @param return_type type of value the function will return
        @param func_type is the function a definition or a declaration
    """
    def add_function(self, func_name, return_type, func_type):
        
        if(func_type == "definition"):
            new_func = function.Function_definition(func_name, return_type)
        elif(func_type == "declaration"):
            new_func.return_func_declaration(self.output, self.return_write_line())
        self.function_dict.update({new_func.func_name:new_func})
        self.tracker.append(new_func)
        self.current_function = new_func


    """ 
        Add content to the body of a function
        @param action_type can be either add or modify 
        @param name can be add for adding content to a line inside a function
            or modify for change the content of an existing line inside a function
            or Variable to add a variable inside the function
            or call to add a call inside the function
        @param line Use this parameter if a specific item at a line needs to be modified
        @param func_name this paramter can be used to change a function by its name 
    """
    def add_to_function_body(self,command_block):
        print("here")
        if command_block.func_name != None:
            self.current_function = self.function_dict.get(command_block.func_name)
        ##if the user specificed a line
        elif command_block.line != None:
            command_block.line = command_block.line - self.return_action_at_line(command_block.line)
        self.current_function.add_to_function_body(command_block)

    """ 
        Return the function that contains the given line. 
        @param line The line requested by the user. 
    """ 
    def return_action_at_line(self, line):
        current_line = 0
        last_line = 0
        if self.tracker:
            for token in self.tracker:
                # adds one to compensate for the empty line between functions
                current_line = current_line + token.return_num_lines() + 1
                if line <= current_line and line >= last_line:
                    self.current_function = token
                    return last_line
                last_line = current_line
                
            
    