tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "backslash (\\)"
print 'quotes, single (\'), double (\")'
print "quotes, single (\'), double (\")"
print "ASCII bell (\a)"
print "ASCII backspace (\b)"
print "ASCII formfeed (\f)"
print "ASCII linefeed (\n)"
print u"Character named name in the Unicode database (Unicode only): \N{GREEK CAPITAL LETTER OMEGA}"
print "Carriage Return (\r)"
print "Horizontal Tab (\t)"
print u'Char with 16-bit hex value 03A9 (u" string only): \u03A9'
print u'Char with 32-bit hex value 000003A9 (u" string only): \U000003A9'
print "ASCII vertical tab (\v)"
print "Character with octal value 67: \067"
print "Character with octal value 67: \o67"
print "Character with hex value 67: \x67"

print '''
What can we do?
Inside of triple single quotes?

while True:
    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
'''

print "Bye."
