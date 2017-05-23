# Exercise 16: Reading and Writing Files

# LIST OF COMMANDS:

# close -- Closes the file. Like File->Save.. in your editor.

# read -- Reads the contents of the file. You can assign the result to a variable.

# readline -- Reads just one line of a text file.

# truncate -- Empties the file. Watch out if you care about the file.

# write('stuff') -- Writes "stuff" to the file.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^ C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()



# Study Drill 2: Write a script similar to the last exercise that uses read and argv to read the file you just created

from sys import argv
script, filename = argv
with open(filename) as f:
    output = f.read()

    
# Study Drill 3: There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.  
# http://stackoverflow.com/questions/8691311/python-how-to-write-multiple-strings-in-one-line

target.write('{}\n{}\n{}\n'.format(line1, line2, line3))







