# -*- coding: utf-8 -*-

import numpy as np
import struct

class BmpReader(object):
    def __init__(self, filePath):
        self.path = filePath
        try:
            file = open(filePath, "rb")
            
            self.bfType = file.read(2)          # 文件类型
            self.bfSize = file.read(4)          # 文件大小
            self.bfReserved1 = file.read(2)     # 文件保留字
            self.bfReserved2 = file.read(2)     # 文件保留字
            self.bfOffBits = file.read(4)       # 数据开始偏移位置
            self.biSize = file.read(4)          # 位图数据文件头占据的字节数
            self.biWidth = file.read(4)         # 图片宽度
            self.biHeight = file.read(4)        # 图片长度
            self.biPlanes = file.read(2)        # 目标设备级别
            self.biBitCount = file.read(2)      # 像素点需要的位数
            self.biCompression = file.read(4)   # 压缩类型
            self.biSizeImage = file.read(4)     # 位图大小
            self.biXPelsPerMeter = file.read(4) # 水平分辨率
            self.biYPelsPerMeter = file.read(4) # 纵向分辨率
            self.biClrUsed = file.read(4)       # 实际使用的颜色表个数
            self.biClrImportant = file.read(4)  # 重要颜色个数
            
            offset = struct.unpack("<I", self.bfOffBits)[0]
            imgsize = struct.unpack("<I", self.bfSize)[0]
            bitCount = struct.unpack("<H", self.biBitCount)[0]
            width = struct.unpack("<I", self.biWidth)[0]
            heigh = struct.unpack("<I", self.biHeight)[0]
            self.size = width * heigh
            if bitCount == 32:
                self.count = 4
            elif bitCount == 24:
                self.count = 3
            self.data = np.zeros((self.size, self.count))
            for i in range(self.size):
               for j in range(self.count):
                    self.data[i][j] = struct.unpack("<B", file.read(1))[0]

            file.close()
        except IOError as e:
            print("something wrong:" + str(e))
            self.data = None
    def return_data(self):
        return self.data

    def rebuild(self, data, filename):
        file = open(self.path + filename, "wb")
        file.write(self.bfType)
        file.write(self.bfSize)
        file.write(self.bfReserved1)
        file.write(self.bfReserved2)
        file.write(self.bfOffBits)
        file.write(self.biSize)
        file.write(self.biWidth)
        file.write(self.biHeight)
        file.write(self.biPlanes)
        file.write(self.biBitCount)
        file.write(self.biCompression)
        file.write(self.biSizeImage)
        file.write(self.biXPelsPerMeter)
        file.write(self.biYPelsPerMeter)
        file.write(self.biClrUsed)
        file.write(self.biClrImportant)
        
        for i in range(self.size):
            for j in range(self.count):
                a = data[i][j]
                # print(i, j)
                # print(a)
                file.write(struct.pack("<f", float(a)))
        file.close()
        
        


        
        
