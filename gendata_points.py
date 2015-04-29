#!/usr/bin/python
import sys
import random

MAX_X = 2047
MAX_Y = 1023
MAX_LENGTH = 1024*2048

def main(args):
    for i in range(MAX_LENGTH):
        print(str(random.randint(0,MAX_X)) + " " + str(random.randint(0,MAX_Y)))

if __name__=="__main__":
    main(sys.argv[1:])
