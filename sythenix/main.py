#Import libraries used
#### Interface ####
import tkinter as tk
import sounddevice as sd
import soundfile as sf

#### Math ####
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

#### Custom Widgets ####
from custom_widgets.Knob import Knob

# How to play sound:
# fs = 44100
# data = np.random.uniform(-1, 1, fs)
# sd.play(data, fs)
 
## The Sythenix Application ##
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        # define root windows main properties
        self.title("Sythenix")
        self.geometry('1000x500')
        # self.resizable(0,0)

        # configure root window grid layout
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)

        # populate window
        self.populate()

    def populate(self):
        np.random.seed(19680801)

        dt = 0.001
        t = np.arange(0, 10, dt)
        nse = np.random.randn(len(t))
        r = np.exp(-t / 0.05)

        cnse = np.convolve(nse, r) * dt
        cnse = cnse[:len(t)]
        s = 2*np.sin(2 * np.pi * t)

        synthTransformFig = Figure((20,5),dpi=100)

        a1 = synthTransformFig.add_subplot(131)
        a1.plot(t, s)
        a1.label = "Hello"
        a2 = synthTransformFig.add_subplot(132)
        a2.plot(t, cnse)
        a3 = synthTransformFig.add_subplot(133)
        a3.plot(t, nse)

       
    

        '''
        add_subplot(nrows, ncols, index)
            Three integers (nrows, ncols, index). The subplot will take the index 
            position on a grid with nrows rows and ncols columns. 
            index starts at 1 in the upper left corner and increases to the right. 
            index can also be a two-tuple specifying the (first, last) indices 
            (1-based, and including last) of the subplot, e.g., fig.add_subplot(3, 1, (1, 2)) 
            makes a subplot that spans the upper 2/3 of the figure.
        '''

        self.matlabCanvas = FigureCanvasTkAgg(synthTransformFig, master=self)
        self.matlabCanvas.draw()
        tk_matlabCanvas = self.matlabCanvas.get_tk_widget()
        tk_matlabCanvas.grid(column=0,row=0,sticky=tk.E,padx=0,pady=0,ipadx=0,ipady=0)
        
        # tk_matlabCanvas.

        # matlabCanvas.mpl_connect("key_press_event", self.on_key_press)

        # testKnob = Knob(self)
        # testKnob.grid(column=2, row=3)

    # def on_key_press(self, event):
    #     print("you pressed {}".format(event.key))
    # #     key_press_handler(event, self.inputCanvas, self.outputCanvas)


    # def _quit(self):
    #     self.quit()     # stops mainloop
    #     self.destroy()  # this is necessary on Windows to prevent
    #                     # Fatal Python Error: PyEval_RestoreThread: NULL tstate

if __name__ == "__main__":
    fs = 44100 
    seconds = 2
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    sd.play(myrecording, samplerate=fs)
    sd.wait()

    sf.write('sound.wav', myrecording, fs)

    app = App() 
    app.mainloop()