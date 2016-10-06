# assign the result of a string with a format foo to x
x = "There are %d types of people." % 10

# assign another string
binary = "binary"

# assign another string
do_not = "don't"

# assing the result of a string with multiple format specifiers to y
# 1st and 2nd
y = "Those who know %s and those who %s." % (binary, do_not)

# print the previously assigned strings
print x
print y

# play with different format stuff
# 3rd
print "I said: %r." % x
# 4th
print "I also said: '%s'." % y

# well, boolean
hilarious = False
joke_evaluation = "Isn't the joke so funny?! %r"

# so you can put a not evaluated format specifier in a string and
# evaluate later I guess
print joke_evaluation % hilarious

# assign more strings
w = "This is the left side of..."
e = "a string with a right side."

# and this is string concatenation, with a +
print w + e
