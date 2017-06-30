#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 5: More Variables and Printing

name = 'Elisabeth aka Becci'
age = 28 # not a lie
height = 54 # inches
weight = 130 # lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)


# Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.

pounds = 180
kilos = pounds * 0.45359237
print "%r pounds equals %r kilos." % (pounds, kilos)
