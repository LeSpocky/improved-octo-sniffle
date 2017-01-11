#!/usr/bin/env python
import sys
import os.path

scrip,from_file, to_file = sys.argv

print "Copying from %s to %s" % ( from_file, to_file )

# we could do these on one line, how?
#in_file = open( from_file )
#in_data = in_file.read()
in_data = open( from_file ).read()

print "The input file is %d bytes long" % len( in_data )

print "Does the output file exist? %r" % os.path.exists( to_file )
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open( to_file, 'w' )
out_file.write( in_data )

print "Alright, all done."

out_file.close()
#in_file.close()
