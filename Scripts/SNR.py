#!/usr/bin/env python

import scipy.io.wavfile as wavfile
import scipy.stats as stats
import numpy as np

def soundToNoise(fileName):
     data = wavfile.read(fileName)[1]
     npData = np.asanyarray(data)
     mean = npData.mean(axis=0)
     sd = npData.std(axis=0, ddof=0)
     return np.where(sd == 0, 0, mean/sd)

def main():
    for fileName in [ "Output.wav", "Lossy.wav" ]:
        print(fileName, "=>", soundToNoise(fileName))

if __name__ == '__main__':
    main()
