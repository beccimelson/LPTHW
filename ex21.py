#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 21: Functions Can Return Something

# the function is called with two arguements, a & b
def add(a, b):
# print statement where a & b are added
# a & b are arguments
    print "ADDING %d + %d" % (a, b)
# returns a + b
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit
print "Here is a puzzle."

# taking the return value of one function and using it as the argument of another function
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
