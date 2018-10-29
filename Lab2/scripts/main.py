# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt 
from ReadWAVFile import rwf

def read_file(filename):
    file = rwf(filename)
    raw_data = file.getRawData()


def main():
    print("Hello World!")

if __name__ == '__main__':
    main()