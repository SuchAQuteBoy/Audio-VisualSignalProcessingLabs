# -*- coding: utf-8 -*-

import numpy as np

class MFCCReader(object):
    def __init__(self, filepath):
        try:
            file = open(filepath, "r")
            data = file.read().replace("\n", "")
            data = data.split(" ")
            data = [i for i in data if i != ""]
            self._datalist = []
            for f in data:
                self._datalist.append(eval(f))
            file.close()
        except Exception as e:
            print("something wrong:" + str(e))
            self._datalist = None
        

    def returndata (self):
        return self._datalist
    


