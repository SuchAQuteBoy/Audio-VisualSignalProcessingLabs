import math
import wave
import numpy as np
import matplotlib.pyplot as plt

def sgn(a):
    if a >= 0:
        return 1
    else:
        return -1


def ZeroCR(waveData, frameSize):
    wave_len = len(waveData)
    frameNum = math.ceil(wave_len / frameSize)
    ZRresult = []
    f = []
    loop = 1
    result = 0
    for i in range(frameNum):
        l = loop + frameSize
        if l > wave_len:
            l = wave_len
        for j in range(loop, l):
            result = result + (waveData[j]*waveData[j-1] < 0)
        f.append(result)
        result = 0
        loop += frameSize
    
    for i in range(len(f)):
        ZRresult.append(f[i] / (frameSize - 1))
    return ZRresult


def ZCR(inputName, extension):
    fileName = inputName + extension
    outputName = inputName + '_' + "zero.txt"
    file = wave.open(fileName,"rb")
    params = file.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = file.readframes(nframes)
    file.close()

    wave_data = np.fromstring(str_data, dtype=np.short)
    # wave_data.shape = -1,1
    frameSize = 256
    result = ZeroCR(wave_data, frameSize)
    file = open(outputName,"w+")
    for i in range(len(result)):
        file.write(str(result[i]) + '\n')
    file.close


def Energy(waveData, frameSize):
    wave_len = len(waveData)
    frameNum = math.ceil(wave_len / frameSize)
    ENresult = []
    loop = 0
    result = 0
    for i in range(frameNum):
        l = loop + frameSize
        if l > wave_len:
            l = wave_len
        for j in range(loop, l):
            # if i == 162: print(str(j) + ' ' + str(waveData[j]) + ' ' + str(pow(waveData[j], 2)))
            result = result + pow(waveData[j], 2) * pow(1.0 / (2 * frameSize), 2)
        ENresult.append(result)
        result = 0
        loop += frameSize
    # print(ENresult)
    return ENresult

def ENG(inputName, extension):
    fileName = inputName + extension
    outputName = inputName + '_' + "en.txt"
    file = wave.open(fileName,"rb")
    params = file.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = file.readframes(nframes)
    file.close()

    wave_data = np.fromstring(str_data, dtype=np.short)
    # wave_data.shape = -1,1
    frameSize = 256
    result = Energy(wave_data, frameSize)
    file = open(outputName,"w+")
    for i in range(len(result)):
        file.write(str(result[i]) + '\n')
    file.close

def main():
    for i in range(1, 11):
        name = str(i)
        ZCR(name, ".wav")
        ENG(name, ".wav")


if __name__=="__main__":
    main()
