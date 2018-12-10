# -*- coding: utf-8 -*-

import argparse
import numpy as np
from dtw import dtw
from reader import MFCCReader


class Main(object):
    def main(self):
        model_data = np.array(10)
        test_data = np.zeros((10, 10))
        output = np.zeros((10, 10))
        for i in range(10):
            model_data[i] = MFCCReader("resources/mfcc/" + "data" + str(i + 1) + ".wav.txt").returndata()
        for i in range(10):
            for j in range(10):
                test_data[i][j] = MFCCReader("resources/mfcc/" + "data" + str(i + 1) + "_" + str(j + 1) + ".wav.txt").returndata()

                out = np.zeros(10)
                for k in range(10):
                    out[k] = dtw(model_data[k], test_data[i][j]).returndata()
                output[i][j] = out.index(min(out))
                out.clear()
        cur = 0
        for i in range(10):
            for j in range(10):
                if output[i][j] == i:
                    cur += 1
        rate = cur / 100.

if __name__ == "__main__":
    Main().main()