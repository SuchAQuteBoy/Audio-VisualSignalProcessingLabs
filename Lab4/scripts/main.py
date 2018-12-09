# -*- codint: utf-8 -*-

from trans import Trans
from bmpreader import BmpReader
import argparse
import numpy as np 

class Main(object):
    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("filename")
        args = parser.parse_args()
        d = BmpReader(args.filename)
        data = d.return_data()
        s = Trans(data)
        data1 = s.hsi()
        data2 = s.yiq()
        data3 = s.ycbcr()
        
        d.rebuild(data1, ".hsi")
        d.rebuild(data2, ".yiq")
        d.rebuild(data3, ".ycbcr")


if __name__ == "__main__":
    Main().main()