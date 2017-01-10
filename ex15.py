from sys import argv

# unpack commandline arguments to the variables 'script' and 'filename'
script, filename = argv

# open the file 'filename' and assign the file object returned by open
# to the variable 'txt'
txt = open( filename )

print "Here's your file %r:" % filename

# call the method 'read' on the file object 'txt' and pass the result to
# the print function
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input( "> " )

txt_again = open( file_again )

print txt_again.read()
txt_again.close()
