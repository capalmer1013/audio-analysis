import wave
import struct

class Reader(object):
    def __init__(self):
        self.samples = []
        self.sampwidth = 0
        self.channels = 0
        self.framerate = 0
        self.framecount = 0

    def read(self, filename):
        waveRead = wave.open(filename, 'rb')
        self.sampwidth = waveRead.getsampwidth()
        self.channels = waveRead.getnchannels()
        self.framerate = waveRead.getframerate()
        self.framecount = waveRead.getnframes()

        frame = waveRead.readframes(1)
        while frame != b'':
            self.samples.append(struct.unpack_from("<h"+"h"*(self.channels-1), frame))
            frame = waveRead.readframes(1)




    def outputChannel(self, channel, outfileName):
        pass
