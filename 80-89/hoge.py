# -*- coding: utf-8 -*-
"""

"""
import sys
import argparse

def main(args):
    print args.foo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "KaiBun generator")
    parser.add_argument('foo', type=argparse.FileType("w"))
    parser.parse_args()
    args = parser.parse_args()
    main(args)
