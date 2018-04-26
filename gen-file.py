#!/usr/bin/python3

from random import *

f = open("sortfile", "w")
numlines = randint(1, 10000000)
for x in range(1, numlines):
   num = randint(1, 100000000)
   f.write(str(num) + "\n") 

