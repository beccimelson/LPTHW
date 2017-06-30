#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 15: Reading Files

# Lines 4 & 6 uses argv to get a filename.
from sys import argv

script, filename = argv

# Opens a file.
txt = open(filename)

# Dislays a message and prints the specific filename
print "Here's your file %r:" % filename
print txt.read()

# prompts the user to enter the filename again
print "Type the filename again:"
file_again = raw_input("> ")


txt_again = open(file_again)

print txt_again.read()


# from Stack Overflow:
# A better idea would be to use the with statement to have Python close files for you automatically; file objects are context managers:

# with open(filename) as txt:
#    print "Here's your file %r:" % filename
#    print txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")

# with open(file_again) as txt_again:
#     print txt_again.read()
