"""
    Author:Jarvis Lu
    Date: 3/2/2020
    This file contains the Funtion class. The function class can be used write
functions to the file. Functions will contain sub classes such as if_else statements
or variables or includes etc
"""

from .import variable
from .import calls
from .import loops_and_conditionals

action_words = ["add", "modify", "remove"]

""" 
    Initialization of the Function class
    @param file_path path to the file that this writer class is going to write to 
    @instance function_dict a dictionary to keep all functions so a specifc func can be 
        returned given a func name
    @instance current_action the last sub-class the user was editing. This is implemented 
        so the user can edit the same func without the need to specify it again
    @instance argument_dict a dictionary containing all the arguments that will be
        passed into this function. The keys will be the name of the argument and the value
        would be the type of the argument(e.g. {example:int})
    @instance variable_dict a dictionary containing all the variables that this function
    @instance output the content of this file. Changes will be made to the self.output list
        then it would be passed to writer to write to file
    @instance tracker keeps track of everything within the file. Whenever a new object is created
        it is placed in the tracker depending on its position in the file. When the output is 
        being generated, output will be generated sequencially from the first item in tracker 
        to the last 
"""
class Function_definition(object):
    def __init__(self, func_name, return_type):
        self.current_action = None
        self.argument_dict = {}
        self.variable_dict = {}
        self.return_type = return_type
        self.func_name = func_name
        self.output = []
        self.tracker =[]

    """ 
        Generate the output base on the content within this function class.  
        @return return the output generated
        @return a buffer containing the output of the function with its body 
    """ 
    def generate_output(self, output):
        arguments = self.argument_dict.keys()
        temp_out = self.return_type + " " + self.func_name + "("
        if arguments:
            for arg in arguments:
                output += self.argument_dict.get(arg) + " " + arg + ","     
            temp_out = output[:-1]
        temp_out += "){"
        self.output.clear()
        self.output.append(temp_out)
        for token in self.tracker:
            token.generate_output(self.output, 1)
        self.output.append("}")
        for token in self.output:
            output.append(token)
        return output

    """ 
        Return just the output generated since function declaration have
    no body
        @return just the function header (e.g. int example ();)
    """ 
    def return_func_declaration(self):
        return self.generate_output(self) + ";"

    """ 
        return the output with the format for a function body
        @param output the output of the file passed in for this class to 
            add content
        @param starting_index the index in which the function can start adding
            its information 
    """ 
    def return_func_definition(self, output, starting_index):
        temp_output = self.generate_output(self)
        while(len(output) <= starting_index):
            output.append("")
        output.insert(starting_index, (temp_output + "{"))
        output.insert(starting_index + 1, "")
        output.insert(starting_index + 2, "}")

    """ 
        Returns the number of lines this function class is taking up within
    the file. 
        @param line if no specific line is passed in, the function will return 
            the number of lines this functino will take up. If a line number is 
            specified, then the class at that line number will be returned.
        @return returns the number of lines this class will be or if line parameter
            is specified then return the object at line
    """ 
    def return_num_lines(self):
        num_line = 0
        for token in self.tracker:
            num_line = num_line + token.return_num_lines()
        return num_line + 2

    """ 
        Parse the command line to simply the command passing process and provide 
    information to add_to_function_body so further action can be taken
        @param command_line the string of command pass by the user
        @param line Use this parameter if a specific item at a line needs to be modified
    """
    def parse_command(self, command_line):
        command_line = command_line.split(",")
        for item in command_line:
            if len(command_line) == 0:
                    break
            elif item in action_words:
                one_command = [None, None, None, None]
                print(command_line)
                index = command_line.index(item)
                next_index = 0
                if len(command_line) > index + 3:
                    for items in command_line[index + 2:]:
                        if items in action_words:
                            next_index = command_line[index + 2:].index(items) + 2
                            break
                length = next_index - index
                if length == 0:
                        length = len(command_line)
                i = 0
                while i < length: 
                    one_command[i] = command_line[index + i]
                    i = i + 1
                # print(one_command)
                if one_command[3] != None:
                    one_command[3] = int(one_command[3])
                self.add_to_function_body(one_command[0], name=one_command[1], value=one_command[2], line=one_command[3])
                command_line = command_line[index + length:]


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
    def add_to_function_body(self, action_type, name= None, line= None, value= None):
        if line != None:
            print(line)
            line = line - self.return_action_at_line(line)
        if isinstance(self.current_action, loops_and_conditionals.loops_and_conditionals_parent):
            self.current_action.add_to_body(action_type, name, line, value)
        else: 
            if action_type == "add":
                self.set_current_action(name, value)
            elif action_type == "modify":
                if self.variable_dict.get(value) != None:
                    self.current_action.handle_command(name, self.variable_dict.get(value).name)
                else:
                    self.current_action.handle_command(name, value)
            elif action_type == "remove":
                self.tracker.remove(self.current_action)

    """ 
        Return the function that contains the given line. 
        @param line The line requested by the user. 
    """ 
    def return_action_at_line(self, line):
        current_line = 1
        last_line = 0
        if self.tracker:
            for token in self.tracker:
                current_line = current_line + token.return_num_lines()
                if line < current_line and line >= last_line:
                    self.current_action = token
                    return last_line
                last_line = current_line

    """ 
        This function can be used to add classes such as the calls class or
    variable class or if else or loop etc.
        @param name when used in this function, it should only be the name of one of 
            the classes stated above
        @param value in this case would be the name that you wish to give to the
            class 
    """ 
    def set_current_action(self, names, values):
        if names == "call":
            self.current_action = calls.Calls(self)
        elif names == "variable":
            self.current_action = variable.Variable(self)
            self.variable_dict.update({values:self.current_action})
        elif names == "if":
            self.current_action = loops_and_conditionals.If(self)
        elif names == "elif":
            self.current_action = loops_and_conditionals.Elif(self)
        elif names == "else":
            self.current_action = loops_and_conditionals.Else(self)
        elif names == "while":
            self.current_action = loops_and_conditionals.While(self)
        elif names == "for":
            self.current_action = loops_and_conditionals.For(self)
        elif names == "do_while":
            self.current_action = loops_and_conditionals.Do_while(self)      
        self.current_action.name = values
        self.tracker.append(self.current_action)