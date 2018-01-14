# File: Variables_and_Branching_in_Python.py
# Description: Variables and Branching in Python
# Environment: Spyder IDE in Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Variables and Branching in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Variables_and_Branching_in_Python (date of access: XX.XX.XXXX)

"""
Created on Sun Jan 07 00:05:15 2018

@author: Valentyn
"""
import os
import psutil
import sys

print("This is a Great Python Program!")
print("Hello there, programmer!")

name = input("What is your name? ")
print(name, ", Welcome!")

answer = input("Let's work? (Y/N)")

if answer == 'Y':
    print("Great choice!") # type "pass" for the empty construction
    print("I can do for you:")
    print("[1] - show list of files and folders in current directory")
    print("[2] - show information about System")
    print("[3] - show list of running tasks in the System")
    todo = int(input("Make your choice: "))    
    if todo == 1:
        print(os.listdir())
    elif todo == 2:
        print("Current directory: ", os.getcwd())
        print("Number of CPU: ", os.cpu_count())
        print("Operation System: ", sys.platform)
        print("File system encoding: ", sys.getfilesystemencoding())
    elif todo == 3:
        print("List of current running PIDs: ", psutil.pids())
    else: pass # for the empty construction        
elif answer == 'N':
    print("Good by, see you next time!")
else:
    print("Unknown input, try again")
