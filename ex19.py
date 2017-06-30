#!/bin/python
# -*- coding: utf-8 -*-

# Exercise 19: Functions and Variables
# The variables in your function are not connected to the variables in your script.


# creates a function called cheese_and_crackers with two arguements:
# cheese_count, boxes_of_crackers)


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the value of "cheese_count" in a string
    print "You have %d cheeses!" % cheese_count
    # prints the value of boxes_of_crackers in a string
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints a string
    print "Man that's enough for a party!"
    # prints a string
    print "Get a blanket.\n"

    # prints a string
    print "We can just give the function numbers directly:"
    # calls the function cheese_and_crackers with arguement value of 20 and 30
    cheese_and_crackers(20,30)

    # prints a string
    print "OR, we can use variables from our script:"
    # creates variable amount_of_cheese with value "10"
    amount_of_cheese = 10
    # creates variable amount_of_crackers with value "50"
    amount_of_crackers = 50

    # calls the function cheese_and_crackers with arguements set to the variables
    # "amount_of_cheese" and "amount_of_crackers", whos values are set to "10"
    # and "50" respectivelly
    cheese_and_crackers(amount_of_cheese, amount_of_crackers)

    # prints a string
    print "We can even do math inside too:"
    cheese_and_crackers(10 + 20, 5 + 6)
    # calls the function "cheese_and_crackers" with the arguments "10+20" and "5+6"
    # which proves it's possible to do math on the arguments/values passed to the
    # function

    # prints a string
    print "And we can combine the two, variables and math:"
    # calls the function cheese_and_crackers with the arguements
    # "amount_of_cheese + 100", "amount_of_crackers + 1000"
    cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)





    # I only found 8 unique ways to call the function and they're listed below:

    # 1. Simple arguments passed directly
    # 2. Math(s)
    # 3. Variables
    # 4. Variables and math(s) (maybe this counts as a variation? I'll allow it)
    # 5. Assign the function to a variable and call the variable with arguments
    # 6. Variable number of arguments (using the asterisk method)
    # 7. Writing another function, then pass values to the original one within in it
    # 8. User input


def order_stats(total_orders, total_returns):
    print(f"You have {total_orders} orders")
    print(f"You have {total_returns} returns")
    print(f"Your net sales are {total_orders - total_returns}")
    print("Hopefully you had a good month!\n")

# Simple arguments
order_stats(4321, 1234)

# Math
order_stats(102+321, 456*4) # ouch, bad month

# Variables
jims_sales = 395
sally_sales = 72
joan_sales = 5481 # way to go Joan!
returns = 32
order_stats(jims_sales+sally_sales+joan_sales, returns)

# Variables and math
order_stats((jims_sales*4)+(sally_sales%4)+(joan_sales%4), returns)

# Assign the function to a variable? (it works!)
order_totals = order_stats
order_totals(30,1)

# With a variable number of arguments - a la *args? (it works!)
var_stats = (560, 42)
order_stats(*var_stats)

# function to function? (it works!)
def func_to_func():
    value1 = 20
    value2 = 30
    order_stats(value1, value2)
func_to_func()

# user input - Don't forget to specify a type of input! In this case an integer
print("how much did you sell this month?")
user_sales = int(input('>>>'))
order_stats(user_sales, returns)
