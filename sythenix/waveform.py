import numpy as np
from matplotlib.figure import Figure

class Waveform():
    def __init__(self, data, fs):
        self.data = data
        self.fs = fs