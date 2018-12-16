# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


class IMGProc(object):
    def brightness(self, filepath, change):
        try:
            img = cv.imread(filepath)
            rows, cols = img.shape[:2]
            if change >= 255 or change < -255:
                print("illegal!")
                exit(0)
            for i in range(rows):
                for j in range(cols):
                    for k in range(3):
                        img[i, j][k] += change
                        if img[i, j][k] > 255:
                            img[i, j][k] = 255
                        elif img[i, j][k] < 0:
                            img[i, j][k] = 0
            cv.imshow("brightness", img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))

    def contrast(self, filepath, change):
        try:
            img = cv.imread(filepath)
            rows, cols = img.shape[:2]
            if change < 0:
                print("illegal!")
                exit(0)
            for i in range(rows):
                for j in range(cols):
                    for k in range(3):
                        img[i, j][k] = int(change * img[i, j][k])
                        if img[i, j][k] > 255:
                            img[i, j][k] = 255
                        elif img[i, j][k] < 0:
                            img[i, j][k] = 0
            cv.imshow("contrast", img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))

    def histogram(self, filepath):
        try:
            img = cv.imread(filepath)
            data = np.asarray(img)
            data = data.flatten()
            plt.hist(data, bins=256)
            plt.show()
        except IOError as e:
            print("ERROR: " + str(e))

    def median(self, filepath):
        try:
            img = cv.imread(filepath)
            cv.imshow("original_median", img)
            rows, cols = img.shape[:2]
            d = np.asarray(img)
            data = []
            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    data = d[i - 1:i + 2:1, j - 1:j + 2:1].reshape(9, 3)
                    img[i, j] = np.median(data, axis=0)
            cv.imshow("median", img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))

    def mean(self, filepath):
        try:
            img = cv.imread(filepath)
            cv.imshow("original_mean", img)
            rows, cols = img.shape[:2]
            d = np.asarray(img)
            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    data = d[i - 1:i + 2:1, j - 1:j + 2:1].reshape(9, 3)
                    img[i, j] = np.mean(data, axis=0)
            cv.imshow("mean", img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))


    def edge_reberts(self, filepath):
        try:
            img = cv.imread(filepath, 0)
            rows, cols = img.shape[:2]
            new_img = np.zeros((rows, cols), np.uint8)
            d = np.asarray(img)
            for i in range(rows - 1):
                for j in range(cols - 1):
                    data = d[i:i + 2:1, j:j + 2:1]
                    g_x = abs(int(data[1, 1]) - int(data[0, 0]))
                    g_y = abs(int(data[1, 0]) - int(data[0, 1]))
                    M = g_x + g_y
                    if M >= 100:
                        new_img[i:i + 2:1, j:j + 2:1] = d[i:i + 2:1, j:j + 2:1]
            cv.imshow("reberts_img", img)
            cv.imshow("reberts_new_img", new_img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))


    def edge_sobel(self, filepath):
        try:
            img = cv.imread(filepath, 0)
            rows, cols = img.shape[:2]
            new_img = np.zeros((rows, cols), np.uint8)
            d = np.asarray(img)
            for i in range(rows - 2):
                for j in range(cols - 2):
                    data = d[i:i + 3:1, j:j + 3:1]
                    g_x = abs((int(data[2, 0]) + 2 * int(data[2, 1]) + int(data[2, 2])) - (int(data[0, 0]) + 2 * int(data[0, 1]) + int(data[0, 2])))
                    g_y = abs((int(data[0, 2]) + 2 * int(data[1, 2]) + int(data[2, 2])) - (int(data[0, 0]) + 2 * int(data[1, 0]) + int(data[2, 0])))
                    M = g_x + g_y
                    if M >= 300:
                        new_img[i:i + 3:1, j:j + 3:1] = d[i:i + 3:1, j:j + 3:1]
            cv.imshow("reberts_img", img)
            cv.imshow("reberts_new_img", new_img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))


    def fast_median(self, filepath):
        try:
            img = cv.imread(filepath)
            rows, cols = img.shape[:2]
            d = np.asarray(img)
            data = []
            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    if j == 1:
                        data = d[i - 1:i + 2:1, j - 1:j + 2:1]
                    elif i == 1 and j != cols - 2:
                        data[:, 0] = data[:, 1]
                        data[:, 1] = data[:, 2]
                        data[:, 2] = d[i - 1:i + 2:1, j + 1]
                    elif i != 1 and j != cols - 2:
                        data[0, 2] = data[1, 2]
                        data[1, 2] = data[2, 2]
                        data[2, 2] = d[i + 1, j + 1]
                        data[:, 0] = data[:, 1]
                        data[:, 1] = data[:, 2]
                        data[:, 2] = d[i - 1:i + 2:1, j + 1]
                    data0 = data.reshape(9, 3)
                    img[i, j] = np.mean(data0, axis=0)

            cv.imshow("mean", img)
            cv.waitKey(0)
        except IOError as e:
            print("ERROR: " + str(e))

    def stop(self):
        cv.destroyAllWindows()
