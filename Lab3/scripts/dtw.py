# -*- coding: utf-8 -*

import numpy as np


class dtw(object):
    def __init__(self, model, test):
        self._model = model
        self._test = test
        self._dtw()

    def _dtw(self):
        model = self._model.copy()
        test = self._test.copy()

        l1 = len(model)
        l2 = len(test)

        distence = np.zeros((l1, l2))
        output = np.zeros((l1, l2))

        for i in range(l1):
            for j in range(l2):
                distence[i][j] = abs(model[i] - test[j])
        
        for i in range(1, l1):
            for j in range(1, l2):
                output[i][j] = np.min([distence[i - 1][j - 1], distence[i][j - 1], distence[i - 1][j]]) + distence[i][j]
        
        self._result = output[l1 - 1][l2 - 1]
        
    def returndata (self):
        return self._result
        
