# -*- coding: utf-8 -*

import numpy as np


class dtw(object):
    def __init__(self, model, test):
        self._model = model
        self._test = test
        self._dtw()

    def _dtw(self):
        model = self._model
        test = self._test

        l1 = len(model)
        l2 = len(test)

        distence = np.zeros(4)
        output = 0

        # for i in range(l1):
        #     for j in range(l2):
        #         distence[i][j] = abs(model[i] - test[j])
        
        for i in range(1, l1):
            for j in range(1, l2):
                distence[3] = abs(model[i-1] - test[j-1])
                distence[0] = abs(model[i] - test[j])
                distence[2] = abs(model[i] - test[j - 1])
                distence[1] = abs(model[i-1] - test[j])
                output = np.min([distence[3], distence[2], distence[1]]) + distence[0]
        
        self._result = output
        
    def returndata (self):
        return self._result
        
