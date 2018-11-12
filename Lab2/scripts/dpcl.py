# -*- coding: utf-8 -*-

import numpy as np
import wave


class Dpcl(object):
    def __init__(self, data):
        self._data = data
        self._pro()
        self._calculate_snr()

    def _pro(self):
        data = self._data
        size = len(data)
        err = [0 for i in range(size)]
        rebuild = [0 for i in range(size)]

        for i in range(size):
            if i == 0:
                err[i] = (data[i] - 128)/2 + 128
                rebuild[i] = 128 + (err[i] - 128) * 2
            else:
                err[i] = (data[i] - rebuild[i - 1])/2 + 128
                rebuild[i] = rebuild[i - 1] + (err[i] - 128) * 2

        self._rebuild = rebuild
        self._err = err

    def _calculate_snr(self):
        rebuild = self._rebuild
        err = self._err
        up = np.sum(np.power(err, 2))
        down = np.sum(np.power(rebuild, 2))
        self._snr = 10 * np.log10(up / down)

    def return_data(self):
        return self._data, self._rebuild, self._err, self._snr
