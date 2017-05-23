# Exercise 13: Parameters, Unpacking, Variables

# import = how you add features to your script from the Python feature set
from sys import argv
# argv = "argument variable", This variable holds the arguments you pass to your Python script when you run it. 

# this line "unpacks" argv, so that rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

