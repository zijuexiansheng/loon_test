#!/usr/bin/env python

print "import test.py"

if __name__ == '__main__':
    a = (i * i for i in range(10))
    for each in a:
        print each

