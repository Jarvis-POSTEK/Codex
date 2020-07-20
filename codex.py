"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file is created to test the program. Commands are passed in directly
since voice recongization haven't been implemented

"""
from project_management import command_central
from file_io import commandBlock
import time
import fileinput
import platform


#lines 18 - 39 Rylee Bers

loop = 1
command = command_central.CommandCentral(platform.system())
audio = listen()

while loop == 1:
    userCommand = audio.listenToUser()

    if userCommand.action == "exit":
        loop = 0

    elif userCommand.action == "add_func":
        #pulling out the appropriate parameters from userCommand to add_func
        command.add_func(userCommand.name, userCommand.type, "declaration") #I'll figure out how to extract third paramter in listen class another time....
    
    elif userCommand.action == "add_to_func_body":
        pass

    #more elif statements.... hopefully you get the idea by now


    #so basically a bunch of if statements for each action so that the commandBlock parameters go into the
    #correct codex functions. Is there a better way to do this????







command = command_central.CommandCentral(platform.system())
#disable can be passed in to not add Onedrive if not desired
command.create_new_project(["Desktop", "test2","disable"])
# print("Please select a number:")
# computer_type = input("Please select your operating system:\n (1) Mac\n (2) Windows\n")

# if int(computer_type) == 1:
#     command.create_new_project(home + "/Desktop/test")
# else:
#     save_type = input("Would you like to save this document to OneDrive?\n (1) Yes\n (2) No\n")
#     if int(save_type) == 1:
#         command.create_new_project(home + "\\OneDrive\\Desktop\\test")
#     else:
#         command.create_new_project(home + "\\Desktop\\test")



command.add_file("hello_world.c")
command.add_include("stdio.h")
command.add_include("string.h")
command.add_func("main", "int", "definition")
commands_block = commandBlock.CommandBlock(action="add", name="call", value="printf")
command.add_to_func_body(commands_block)
commands_block = commandBlock.CommandBlock(action="modify", name="add", value= "\"Hello world! %d\\n\"")
command.add_to_func_body(commands_block)

# time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # time.sleep(1)
# command.add_to_func_body("modify", "add", value= "\"Hello world! %d\\n\"")
# # time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # time.sleep(1)
# command.add_to_func_body("modify", "add", value= "\"testing!!\\n\"")
# # time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # time.sleep(1)
# command.add_to_func_body("modify", "add", value= "\"One more\\n\"")
# # time.sleep(1)
# command.add_to_func_body("add", "variable", value= "yes")
# # time.sleep(1)
# command.add_to_func_body("modify", "type", value= "int")
# # time.sleep(1)
# command.add_to_func_body("modify", "value", value= 10)
# # time.sleep(1)
# command.add_to_func_body("add", "variable", value= "no")
# # time.sleep(1)
# command.add_to_func_body("modify", "type", value="int")
# command.add_to_func_body("add", "variable", value= "test")
# # time.sleep(1)
# command.add_to_func_body("modify", "type", value="int")
# # time.sleep(1)
# command.add_to_func_body("modify", "value", value= 20)
# command.add_to_func_body("add", "call", value="printf")
# command.add_to_func_body("modify", "add", value= "\"one and one more%d\\n\"")
# command.add_to_func_body("modify", "add", line= 11, value="yes")
# # time.sleep(2)
# # command.add_to_func_body("remove")

# # time.sleep(1)


# # test for loops/conditionals
# # time.sleep(1)
# command.add_to_func_body("add","if")
# # time.sleep(1)
# command.add_to_func_body("add","elif")
# # time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # command.add_to_func_body("add", "call", value = "printf")
# # command.add_to_func_body("add", "call", value = "printf", line= 13)
# # command.add_to_func_body("add", "elif")
# # command.add_to_func_body("add", "while")
# # time.sleep(1)
# # command.add_to_func_body("add","if")
# # time.sleep(1)
# # command.add_to_func_body("add", "for")
# # command.add_to_func_body("add", "do_while")
# # command.add_to_func_body("add", "call", value = "printf")

# time.sleep(2)

# command.add_to_func_body("remove")
# # command.add_to_func_body("remove")