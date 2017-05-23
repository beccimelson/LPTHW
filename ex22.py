# Exercise 22: What Do You Know So Far?

# Table of keyword/symbols:

#   print() The print function. Used to output text to a console.

#   '       Single quote. Used to encapsulate a single line string.

#   "       Double quote. Used to encapsulate a single line string.

#   "'      Triple quote. Used to encapsulate a multi-line string.

#   #       Hash/Octothorpe/Pound sign. Used to denote a comment.

#   %       Modulo sign/formatter. Used as modulo in mathmatical 
#           operations (returns remainder after division).
#           Also used as a formatter when using format strings.

#   *       Asterisk. Used for multiplication during mathmatical 
#           operations.
#           Also used when using *args in functions when there are an 
#           unknown/arbitrary number of arguments being passed to the 
#           function.

#   -       Hyphen. Used as a minus sign when performing subtraction in 
#           mathmatical operations.

#   /       Forward slash. Used as a division sign when performing 
#           mathmatical operations.

#   +       Plus sign. Used as an addition sign 

#   =       Equals sign. Used to create variables or to set a value to 
#           equal another.
#           Can be paired with other operations (like +)

#   >       Greater than sign. Returns TRUE if value on the left is 
#           greater.

#   >=      Greater than or equal to sign. Returns True if value on the 
#           left of the sign is greater than or equal to the right.

#   <=      Less than or equal to sign. 

#   ===     Comparison operator. Returns True if the value on the left is 
#           exactly the same as the value on the right. Else returns 
#           False. 
#           Can be used to compare strings, boolean operators, integers,etc

#   f""     f string. Python 3.6 syntax for handing format strings. Allows 
#           the inclusion of variables via the {} modifiers.

#   {}      Curly brackets. Used in positional formatting when using format 
#           strings.

#   .format() Python 3 replacement for the % used in format strings. Has 
#             form '{} {}'.format('one', 'two').

#   end=' ' Python 3 syntax for ending a line with a space rather than a 
#           linebreak. Python 2 would use ','

#   join()  The method join() returns a string in which the elements passed 
#           to the string have been joined by a str operator.

#   input() Python 3 version of raw_input().

#   from    Part of an import statement used to import external modules into 
#           a script (?).

#   import  Similar to from but is the 'meat' of the import statement. (?)

#   argv    Accepts a list of command line arguments passed to it when 
#           running a script. Must be imported from the sys module. 

#   open()  Opens a file and returns the corresponding file object.

#   read()  Reads the contents of a file object.

#   write() Writes the contents of a string to a file.

#   close() Closes an open file object. *Important to call this method 

#   os.path Module containing useful functions regarding pathnames.

#   exists  Method/Function that is part of the os.path module which returns 
#           True if path given refers to an existing path or an open file 
#           descriptor.

#   ;       Semi-colon. Allows for 'compound statements'.

#   def     Keyword meaning 'function definition' and used to create user 
#           defined function object.

#   *args   Allows a function to accept an arbitrary argument list.

#   seek()  The method seek() sets the file's current position at the 
#           offset. Default position is 0 but can be set in ().

#   readline()  Reads a single line from a file. A newline character is left 
#               at the end of the string so will automatically read the next 
#               line until the end of the file each time it's called. 


#   ——————————————————————————————————————————————————————


#   Escape sequences:


#       \\	Backslash ()
#       \'	Single-quote (')
#       \"	Double-quote (")
#       \a	ASCII bell (BEL)
#       \b	ASCII backspace (BS)
#       \f	ASCII formfeed (FF)
#       \n	ASCII linefeed (LF)
#       \N{name}	Character named name in the Unicode database (Unicode 
#       only)
#       \r	Carriage Return (CR)
#       \t	Horizontal Tab (TAB)
#       \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
#       \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
#       \v	ASCII vertical tab (VT)
#       \ooo	Character with octal value ooo
#       \xhh	Character with hex value hh



#   ——————————————————————————————————————————————————————

# function checklist:

# Did you start your function definition with def?
# Does your function name have only characters and _ (underscore) characters?
# Did you put an open parenthesis ( right after the function name?
# Did you put your arguments after the parenthesis ( separated by commas?
# Did you make each argument unique (meaning no duplicated names)?
# Did you put a close parenthesis and a colon ): after the arguments?
# Did you indent all lines of code you want in the function four spaces? No more, no less.
# Did you "end" your function by going back to writing with no indent (dedenting we call it)?
# When you run ("use" or "call") a function, check these things:

# Did you call/use/run this function by typing its name?
# Did you put the ( character after the name to run it?
# Did you put the values you want into the parenthesis separated by commas?
# Did you end the function call with a ) character?