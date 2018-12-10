# -*- coding: utf-8 -*-

import numpy as np

class MFCCReader(object):
    def __init__(self, filepath):
        try:
            file = open(filepath, "r")
            self._datalist = file.read().split(" ")
            file.close()
        except IOError as e:
            print("something wrong:" + str(e))
            self._datalist = None
        

    def returndata (self):
        return self._datalist
    


