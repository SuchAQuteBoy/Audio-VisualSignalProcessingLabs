# -*- coding: utf-8 -*-

"""
读取.wav文件的所有数据，获取文件的头部信息和采样点。

所有的数据为内部变量，无法直接访问，请使用相应的函数来进行使用。

需要的包:
    wave
    numpy
    
所有的类:
    class rwf(self, filename) -- 主要类，唯一类。读取所有的wav文件数据。
"""

import wave
import numpy as np 

class rwf(object):
    """
    rwf 获取wav文件的所有内容。

    所有的数据为内部变量，无法从外部进行调用，请直接使用函数获取。

    所有函数:
        ref(self, filename) {filename:String} -- 构造器，传入文件名获取所有的数据，必须先行使用。
        getFrameListData(self) {} -- 获取显式的取样点数据。
        getFrameData(self) {} -- 获取隐式的取样点数据。
        getNchannel(self) {} -- 获取声道数。
        getSampwidth(self) {} -- 获取宽度。
        getFrameRate(self) {} -- 获取采样率。
        getRawData(self) {} -- 获取所有的原始字节数据。
    """

    def __init__(self, filename):
        """
        __init__ rwf的构造器
        
        [description]
        
        Arguments:
            filename {[type]} -- [description]
        """

        try:
            file = wave.open(filename, 'rb')
        except FileNotFoundError as e:
            print('Exception', e)
        else:
            parameters = file.getparams()
            self.__nchannels, self.__sampwidth, self.__framerate, self.__nframes = parameters[:4]
            str_data = file.readframes(self.__nframes)
            self.__wave = np.fromstring(str_data, dtype=np.short)
            self.__data_size = len(self.__wave)
    
    def getFrameListData(self):
        return self.__wave
    
    def getFrameData(self):
        return self.__nframes
    
    def getNchannel(self):
        return self.__nchannels

    def getSampwidth(self):
        return self.__sampwidth

    def getFrameRate(self):
        return self.__framerate

    def getRawData(self):
        return self.__nchannels, self.__sampwidth, self.__framerate, self.__nframes
