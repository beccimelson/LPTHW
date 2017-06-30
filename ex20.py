#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 20: Functions and Files

# imports the argv function (?) from the sys module
from sys import argv

# sets up the scrict for one parameter
script, input_file = argv

# creates a function print_all(f) that prints and reads the input
def print_all(f):
    print f.read()

# creates a function rewind(f) that sets the input file
# to 0 (bytes) via the 'seek()' function
def rewind(f):
    f.seek(0)

# defines the function to print the contents of a specific line of file object 'f', plus the line number or 'count'
def print_a_line(line_count, f):
    print line_count, f.readline()

# note: readline() reads a single line up to the \n character but leaves the \n character at the end of the line, so this automically advances the file position by 1 line for every time the function is called, leaving a new blank line in place. That's why there's a line break in the output code. That's how this script is reading, printing, and advancing each line in turn.

# sets 'current_file' to be the defined in the arguments when running the script
current_file = open(input_file)

# print a whole file on a newline under the print statement
print "First let's print the whole file:\n"

# calls the function 'print_all' with the parameter 'current_file'
print_all(current_file)

# print statement
print "Now let's rewind, kind of like a tape"

# calls the funtion 'rewind' with the parameter 'current_file'
rewind(current_file)

# print statement
print "Let's print three lines:"

# sets variable 'current_line' to 1
current_line = 1
# calls function print_a_line with current_line, current_file as parameters
print_a_line(current_line, current_file)

# 'current_line' is incremented by 1
current_line = current_line + 1
# calls function 'print_a_line' with current_line, current_file as parameters
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)




# exercise 2:
# The first time print_a_line() is called, current_line is equal to 1.
# The next time it's called, current_line is equal to current_line + 1 which is the same as 1 + 1 which is equal to 2.
# The third time simply advances by 1 again to make current_line equal to 3 (i.e. equal to 2 + 1).
# It becomes line_count because that's how the function is called. current_line is passed as the first argument to the function, which accepts that argument into the first parameter in the function which is was arbirtarily set to line_count.
