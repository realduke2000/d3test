#!/usr/bin/python
import sys
import random
import json

# 1GB = 1 * 1024 * 1024 * 1024
# Block = 1 GB / 512 Byte

MAX_BLOCK = 2097152
#MAX_BLOCK = 200
MAX_HIT = 100

MAX_X = 2048
MAX_Y = 1024

def createRandPoint():
    p = {'x': random.randint(0, 2047), 'y' : random.randint(0, 1023), 'value' : random.randint(0, MAX_HIT), 'radius' : 1 }
    return p

def main(args):
    l = []
    for i in range(0, MAX_BLOCK):
        l.append(createRandPoint())

    print(json.dumps(l))


if __name__=="__main__":
    main(sys.argv[:1])
