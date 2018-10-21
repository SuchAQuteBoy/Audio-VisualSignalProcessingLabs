import math
import wave
import struct
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt

STATE = Enum('STATE',('Mute',
             'Transition',
             'Speech',
             'End'))


def sgn(a):
    if a >= 0:
        return 1
    else:
        return -1


def waveData(filename):
    file = wave.open(filename,"rb")
    params = file.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = file.readframes(nframes)
    file.close()

    wave_data = np.fromstring(str_data, dtype=np.short)
    return wave_data


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
            frameSize = l - loop
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
    # file = wave.open(fileName,"rb")
    # params = file.getparams()
    # nchannels, sampwidth, framerate, nframes = params[:4]
    # str_data = file.readframes(nframes)
    # file.close()

    # wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data = waveData(fileName)
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
            frameSize = l - loop
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
    # file = wave.open(fileName,"rb")
    # params = file.getparams()
    # nchannels, sampwidth, framerate, nframes = params[:4]
    # str_data = file.readframes(nframes)
    # file.close()

    # wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data = waveData(fileName)
    # wave_data.shape = -1,1
    frameSize = 256
    result = Energy(wave_data, frameSize)
    file = open(outputName,"w+")
    for i in range(len(result)):
        file.write(str(result[i]) + '\n')
    file.close


def getState(zerodata, engdata, zero_low, zero_high, eng_low, eng_high):
    state = STATE.Mute
    if(zerodata < zero_low and engdata < eng_low):
        state = STATE.Mute
    if(zerodata >= zero_low or engdata >= eng_low):
        state = STATE.Transition
    if(zerodata >= zero_high and engdata >= eng_high):
        state = STATE.Speech
    if(state == STATE.Transition):
        if(zerodata >= zero_high or engdata >= eng_high):
            state == STATE.Speech
        elif(zerodata < zero_low and engdata < eng_low):
            state == STATE.Mute
    return state


def DoubleCheck(name):
    zero_txt = name + '_zero.txt'
    eng_txt = name + '_en.txt'
    wav_name = name + '.wav'
    pcm_name = name + '.pcm'
    state = STATE.Mute
    wave_data = waveData(wav_name)
    print(wave_data)

    zfile = open(zero_txt, 'r')
    efile = open(eng_txt, 'r')

    zero_low = 0.3
    zero_high = 0.5
    eng_low = 50
    eng_high = 100

    zerodata = zfile.readlines()
    engdata = efile.readlines()

    zfile.close()
    efile.close()

    result = []

    for i in range(len(zerodata)):
        state = getState(float(zerodata[i]), float(engdata[i]), zero_low, zero_high, eng_low, eng_high)
        if(state == STATE.Speech):
            for j in range(1, 6):
                if i + j >= len(zerodata):
                    s = len(zerodata)
                else:
                    s = i + j
                state = getState(float(zerodata[s]), float(engdata[s]), zero_low, zero_high, eng_low, eng_high)
                if state == STATE.Mute:
                    break
                else:
                    state = STATE.Speech
        elif(state == STATE.Transition and i > 0 and result[i - 1] == STATE.Speech):
            state = STATE.Speech
        else:
            state = STATE.Mute
        print (str(i + 1) + ' ' + str(state) + '\n')
        result.append(state)
    # print(result)
    begin = []
    end = []
    for i in range(len(result)):
        if i > 0 and result[i] == STATE.Speech:
            if result[i - 1] != STATE.Speech:
                begin.append(i * 256) 
        if i > 0 and result[i] == STATE.Mute:
            if i > 1 and result[i - 1] != STATE.Mute and result[i - 2] == STATE.Speech:
                end.append(i * 256)
    print(begin)
    print(end)
    print(len(wave_data))
    pfile = open(pcm_name, 'wb+')
    for i in range(len(begin)):
        if end[i] > len(wave_data):
            end[i] = len(wave_data)
        for j in range(begin[i], end[i]):
            a = struct.pack('h', wave_data[j])
            pfile.write(a)
    pfile.close()
        

def main():
    for i in range(1, 11):
        name = str(i)
        # ZCR(name, ".wav")
        # ENG(name, ".wav")
        DoubleCheck(name)


if __name__=="__main__":
    main()
