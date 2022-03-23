#Import libraries used
#### Interface ####
from cgi import test
from contextlib import nullcontext
from curses.ascii import NUL
import tkinter as tk
import sounddevice as sd

#### Math ####
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#### Custom Widgets ####
from custom_widgets.Knob import Knob

# How to play sound:
# fs = 44100
# data = np.random.uniform(-1, 1, fs)
# sd.play(data, fs)
 
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        # define root windows main properties
        self.title("Sythenix")
        self.geometry('1000x500')
        # root.resizable(0,0)

        # configure root window grid layout
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)

        self.inputCanvas = NUL
        self.outputCanvas = NUL

        # populate window
        self.generate_waveforms()

    def generate_waveforms(self):
        synthTransformFig = Figure( dpi=100)
        t = np.arange(0, 3, .01)
        synthTransformFig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        synthTransformFig2 = Figure( dpi=100)
        synthTransformFig2.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * -1*t))
        '''
        add_subplot(nrows, ncols, index)
            Three integers (nrows, ncols, index). The subplot will take the index 
            position on a grid with nrows rows and ncols columns. 
            index starts at 1 in the upper left corner and increases to the right. 
            index can also be a two-tuple specifying the (first, last) indices 
            (1-based, and including last) of the subplot, e.g., fig.add_subplot(3, 1, (1, 2)) 
            makes a subplot that spans the upper 2/3 of the figure.
        '''

        inputCanvas = FigureCanvasTkAgg(synthTransformFig, master=self)
        inputCanvas.draw()
        inputCanvas.get_tk_widget().grid(column=0,row=0,columnspan=2,sticky=tk.NW)

        outputCanvas = FigureCanvasTkAgg(synthTransformFig2, master=self)
        outputCanvas.draw()
        outputCanvas.get_tk_widget().grid(column=3,row=0,columnspan=2,sticky=tk.NE)

        inputCanvas.mpl_connect("key_press_event", self.on_key_press)

        testKnob = Knob(self)
        testKnob.grid(column=2, row=3)

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.inputCanvas, self.outputCanvas)


    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

if __name__ == "__main__":
    app = App()
    app.mainloop()