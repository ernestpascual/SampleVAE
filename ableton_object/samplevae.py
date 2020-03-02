import numpy as np
import pyqtgraph as pg
from PyQt5 import QtGui
from player import *
import os
import sys
import signal
import time
import csv

# Import a bunch of helpful modules for visualizing
import IPython.display as ipd
import librosa
import matplotlib.pyplot as plt
import librosa.display
# Import the tool class
from tool_class import *

from player import *

PD_HOST_ADDR="127.0.0.1"
PD_OSC_PORT=7788


def utcnow():
    return round(datetime.datetime.utcnow().timestamp() * 1000)

class SampleVAE():
    def __init__(self):
        self.tmp = 0
        self.tool = SoundSampleTool('model_drum_machines')        
        # Setup OSC
        self.player = Player(PD_HOST_ADDR, PD_OSC_PORT)
        self.wait_time = utcnow()
        self.trigger = False

    def update(self,data,pathname,var):
        if data == 1:
            generate_file = 'generate.wav'
            input_files = [pathname]
            filename = f'{pathname}_var{var}.wav'
            print(filename)
            self.tool.generate(filename, audio_files=input_files, variance=var)
            self.wait_time = utcnow()
            self.trigger = True
        
        if self.trigger == True and utcnow() - self.wait_time > 500:
            print("generate sample !!")
            self.player.playSampleVAE_Sample()
            self.trigger = False

            
        