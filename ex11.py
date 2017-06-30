#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 11: Asking Questions

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


print "What's your name?",
name = raw_input()
print "Can I call you Bill?",
bill = raw_input()

print "Wait, %r, I won't take %r for an answer" % (
    name, bill)
