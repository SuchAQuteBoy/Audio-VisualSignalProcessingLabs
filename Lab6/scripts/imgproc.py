# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

class IMGProc(object):
    def __init__(self):
        self._sigma_d = [0.22222222222222224, 2.7600000000000002, 2.4399092970521545, 6.65432098765432, 8.45421487603306, 24.784352399737024, 54.15836734693877, 60.1764705882353, 61.91012619267466]

    def BilateralFilters(self, filepath, d):
        try:
            img = cv.imread(filepath)
            cv.imshow("original", img)
            # n = img
            # cv.bilateralFilter(n, 5, 150, 150)
            # cv.imshow("right", n)
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
        new_data = data.reshape(d * d, 3)
        sigma_r = [np.var(new_data[:, 0]), np.var(new_data[:, 1]), np.var(new_data[:, 2])]
        sigma_d = self._sigma_d[center - 1]
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
                

                

                
        
        
        
        

        

    
        
        