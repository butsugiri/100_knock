# -*- coding: utf-8 -*-
"""

"""
import sys

def main():
    text = "stressed"
    print text[::-1]
    print "".join([x for x in text[::-1]])

if __name__ == "__main__":
    main()
