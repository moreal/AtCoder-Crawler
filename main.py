#-*- coding:utf8 -*-

from atparser.parser import *
from datetime import *

def main():
    p = Parser(["agc","arc","abc"])
    p.parse()

    f = open("AtCoderProbs.csv","w")
    for data in PROBS:
        f.write(data.toExcel())
        

if __name__ == "__main__":
    main()
