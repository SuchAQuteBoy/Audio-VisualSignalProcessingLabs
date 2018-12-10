# -*- coding: utf-8 -*-

import argparse
import numpy as np
from dtw import dtw
from reader import MFCCReader


class Main(object):
    def main(self):
        model_data = []
        test_data = []
        output = np.zeros((10, 10))
        for i in range(10):
            model_data.append(MFCCReader("resources/mfcc/" + "data" + str(i + 1) + ".mfc.txt").returndata())
        for i in range(10):
            for j in range(10):
                test_data.append(MFCCReader("resources/mfcc/" + "data" + str(i + 1) + "_" + str(j + 1) + ".mfc.txt").returndata())

                out = np.zeros(10)
                for k in range(10):
                    out[k] = dtw(model_data[k], test_data[j]).returndata()
                output[i][j] = out.index(min(out))
                out.clear()
                print(i, j)
            test_data.clear()
        cur = 0
        for i in range(10):
            for j in range(10):
                if output[i][j] == i:
                    cur += 1
        rate = cur / 100.
        print(rate)

if __name__ == "__main__":
    Main().main()