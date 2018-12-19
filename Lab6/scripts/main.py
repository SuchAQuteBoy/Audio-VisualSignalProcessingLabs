# -*- coding:utf-8 -*-

from imgproc import IMGProc

class Main(object):
    def main(self):
        filepath = "resources/test.jpg"
        proc = IMGProc()
        proc.BilateralFilters(filepath, 3)

if __name__ == "__main__":
    Main().main()