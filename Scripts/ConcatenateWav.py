#!/usr/bin/env python

import wave
import glob

def main():
    wavFiles = glob.glob('Data/*.wav')
    outputWavFile = "Output.wav"

    if not wavFiles:
        return

    wavData = []
    for wavFile in wavFiles:
        inputWav = wave.open(wavFile, 'rb')
        wavData.append( [inputWav.getparams(), inputWav.readframes(inputWav.getnframes())] )
        inputWav.close()

    outputWav = wave.open(outputWavFile, 'wb')
    outputWav.setparams(wavData[0][0])
    for wavDataFrame in wavData:
        outputWav.writeframes(wavDataFrame[1])
    outputWav.close()

if __name__ == '__main__':
    main()
