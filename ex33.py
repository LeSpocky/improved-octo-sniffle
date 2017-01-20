#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_loop( limit ):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append( i )

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


print "The numbers: "

for num in my_loop( 6 ):
    print num
