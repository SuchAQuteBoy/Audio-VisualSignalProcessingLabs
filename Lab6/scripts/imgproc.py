# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

class IMGProc(object):
    def __init__(self):
        self._sigma_d = 150
        self._sigma_r = [150, 150, 150]
        
    def BilateralFilters(self, filepath, d):
        try:
            img = cv.imread(filepath)
            cv.imshow("original", img)
            size_x, size_y = img.shape[:2]
            or_data = np.array(img)
            center = int(d / 2)
            for i in range(center, size_x - center):
                for j in range(center, size_y - center):
                    data = or_data[i - center:i + center + 1:1, j - center:j + center + 1:1]
                    img[i, j] = self._calculate(d, center, data)
            cv.imshow("new", img)
            cv.waitKey(0)
        except Exception as e:
            print("ERROR:\n" + str(e))
        finally:
            cv.destroyAllWindows()
    
    def _calculate(self, d, center, data):
        sigma_r = self._sigma_r
        sigma_d = self._sigma_d
        up = np.array([0, 0, 0])
        down = np.array([0, 0, 0])
        w = np.array([0, 0, 0])
        g = np.array([0, 0, 0])
        for i in range(d):
            for j in range(d):
                d0 = ((i - center) ^ 2 + (j - center) ^ 2) / (-2 * sigma_d)
                r = np.power((data[i, j] - data[center, center]), 2) / ([x * (-2) for x in sigma_r]) if 0 not in sigma_r else [0, 0, 0]
                for k in range(3):
                    w[k] = np.exp(d0 + r[k])
                up += data[i, j] * w
                down += w
        g = up / down
        return g
                

