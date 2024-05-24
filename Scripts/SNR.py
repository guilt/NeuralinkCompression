#!/usr/bin/env python

try:
    import os

    import numpy as np
    import scipy.io.wavfile as wavfile
    import scipy.stats as stats
except ImportError:
    print("Please run: pip install scipy")
    exit(1)

def soundToNoise(fileName):
    if not os.path.exists(fileName):
        return -1.0     
    npData = wavfile.read(fileName)[1]
    mean = npData.mean(axis=0)
    sd = npData.std(axis=0, ddof=0)
    return np.where(sd == 0, 0, mean/sd)

def main():
    for fileName in [ "Output.wav", "Lossy.wav" ]:
        print(fileName, "=>", soundToNoise(fileName))

if __name__ == '__main__':
    main()
