# -*- coding:utf-8 -*-

import struct
import numpy as np 

class Trans(object):
    def __init__(self, data):
        self.data = data
        self.shape_x = np.shape(data)[0]
        self.shape_y = np.shape(data)[1]

    def yiq(self):
        mat = np.array([0.114, 0.587, 0.299, 0, -0.321, -0.275, 0.596, 0, 0.311,
         -0.523, 0.212, 0, 0, 0, 0, 1]).reshape(4, 4).T
        data = np.dot(self.data, mat)
        return data

    def hsi(self):
        data = self.data.copy() / 255.0
        for i in range(self.shape_x):
            B = data[i][0]
            G = data[i][1]
            R = data[i][2]
            theta = np.arccos(((R - G) + (R - B)) /
             (2 * np.sqrt((R - G) * (R - G) + (R - B) * (G - B))))
            H = theta if G >= B else 2.0 * np.pi - theta
            S = 1.0 - (3.0 * np.min((R, G, B)) / (R + B + G))
            I = (R + B + G) / 3.0
            data[i][0] = H * 255
            data[i][1] = S * 255
            data[i][2] = I * 255
        return data
                
    def ycbcr(self):
        mat = np.mat([[0.098, 0.564, 0.257, 0], [0.439, -0.291, -0.148, 0],
        [-0.071, -0.368, 0.439, 0], [0, 0, 0, 1]]).T
        print(np.shape(mat))
        data = np.dot(self.data, mat)
        for i in range(self.shape_x):
            data[i] = data[i] + np.mat([16, 128, 128, 0])
        return data

    
