#!/usr/bin/env python3

def main():
    for i in inclusive_range(20):
        print(i, end = ' ')
    print()
    
    for i in inclusive_range(3,16):
        print(i, end = ' ')
    print()
    
    for i in inclusive_range(5,30,3):
        print(i, end = ' ')
    

def inclusive_range(*args):
    numberOfArgs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    if numberOfArgs < 1:
        raise TypeError(f'Expected at least 1 argument, but received {numberOfArgs}!')
    elif numberOfArgs == 1:
        stop = args[0]
    elif numberOfArgs == 2:
        (start, stop) = args
    elif numberOfArgs == 3:
        (start, stop, step) = args
    else: raise TypeError('Expected at most 3 arguments, but received {}!'.format(numberOfArgs))

    # generator
    i = start
    while i <= stop:
        yield i # yield is like return, but for generators. It yield the number and continues to the end of block.
        i += step

if __name__ == '__main__': main()
