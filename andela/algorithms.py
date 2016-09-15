#!/usr/bin/env python

def binary_converter(integer):
    if integer < 0 or integer > 255:
        return 'Invalid input'

    return bin(integer)[2:]

if __name__ == '__main__':
    print binary_converter(5)
