#-*- coding:utf8 -*-

from atparser.parser import *

def main():
    p = Parser("agc")
    p.parse()

    print PROBS

if __name__ == "__main__":
    main()
