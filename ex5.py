name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %g cm tall." % (height * 2.54) # 1" = 2.54cm
print "He's %d pounds heavy." % weight
print "He's %.2f kg heavy." % (weight * 0.45359237) # 1 lbs = 0.45359237 kg
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (
        age, height, weight, age + height + weight)
