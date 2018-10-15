import math
import wave
import numpy as np


def ZeroCR(waveData,frameSize,overLap):
  wlen = len(waveData)
  step = frameSize - overLap
  frameNum = math.ceil(wlen/step)
  zcr = np.zeros((frameNum,1))
  for i in range(frameNum):
    curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
    # curFrame = curFrame - np.mean(curFrame) # zero-justified
    # if i == 1:
    #   print(curFrame)
    #   print('---')
    #   print(curFrame[1::])

    zcr[i] = sum(curFrame[0:-1]*curFrame[1::]<0)
  return zcr 


fw = wave.open('1.wav','rb')
params = fw.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = fw.readframes(nframes)
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 1
#wave_data = wave_data.T
fw.close()
# calculate Zero Cross Rate
frameSize = 256
overLap = 0
zcr = ZeroCR(wave_data,frameSize,overLap)
print(zcr / 255)
