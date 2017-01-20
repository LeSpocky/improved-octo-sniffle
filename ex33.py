#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_loop( limit, inc ):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append( i )

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


def my_other_loop( limit, inc ):
    numbers = []

    for i in range( 0, limit, inc ):
        print "Appending %d" % i
        numbers.append( i )

        print "Numbers now: ", numbers

    return numbers


print "The numbers: "

for num in my_loop( 6, 1 ):
    print num

print( "\n" )

for num in my_other_loop( 6, 1 ):
    print num
