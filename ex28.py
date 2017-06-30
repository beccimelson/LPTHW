#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 28: Boolean Practice

# ..Start Python in your Terminal and type each logic problem in to confirm your answers:

# TIP: Any and expression that has a False is immediately False, so you can stop there. Any or expression that has a True is immediately True, so you can stop there. But make sure that you can process the whole expression because later it becomes helpful.

# https://learnpythonthehardway.org/book/ex28.html

True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and (not ("testing" == 1 or 1 == 0))
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))


# Whenever you see these boolean logic statements, you can solve them easily by this simple process:

Find an equality test (== or !=) and replace it with its truth.
Find each and/or inside parentheses and solve those first.
Find each not and invert it.
Find any remaining and/or and solve it.
When you are done you should have True or False.
