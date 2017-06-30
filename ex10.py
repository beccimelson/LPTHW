#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 10: What Was That?

"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Combine escape sequences and format strings to create a more complex format.

x = "There are %d types of people." % 10
y = "Those who know %s and those who \"%s."" % (binary, do_not)

print x
print y
