# Import libraries used

#### System ####
import queue
import sys

#### Interface ####
import tkinter as tk
import sounddevice as sd
import soundfile as sf

#### Math ####
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler # Used to implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
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

        # randomizes at this point
        np.random.seed(19680801)

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

        # Define menu bar
        menubar = tk.Menu(self, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
        file = tk.Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")    
        file.add_separator()  
        file.add_command(label="Exit", command=self._quit)  
        menubar.add_cascade(label="File", menu=file)  

        edit = tk.Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        edit.add_separator()     
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        menubar.add_cascade(label="Edit", menu=edit)  

        help = tk.Menu(menubar, tearoff=0)  
        help.add_command(label="About", command=self.about)  
        menubar.add_cascade(label="Help", menu=help)  

        self.config(menu=menubar)

        # populate window
        self.populate()

    def populate(self):
        
        dt = 0.0001
        t = np.arange(-10, 10, dt)
        f1 = 220
        s = 2*np.sin(2 * np.pi * f1 * t)

        fs = 1/dt
        # sd.play(s, fs)

        outputFigure, ax1 = plt.subplots(figsize=(20,5), dpi=40)
        outputFigure.suptitle('Output Signal', fontsize=16)

        ax1.plot(t,s) 
        
        ax1.set_xlim((-0.1,0.1))
        ax1.set_ylim((-4,4))

        outputCanvas = FigureCanvasTkAgg(outputFigure, master=self)
        outputCanvas.draw()

        tk_outputCanvas = outputCanvas.get_tk_widget()
        tk_outputCanvas.grid(column=0,row=0,sticky=tk.N,columnspan=5,padx=0,pady=0,ipadx=0,ipady=0)

        amplitude = tk.DoubleVar()
        scale = tk.Scale( self, variable = amplitude )
        scale.grid(column=0,row=2,sticky=tk.NSEW,padx=0,pady=0,ipadx=0,ipady=0)
                
        # tk_matlabCanvas.

        # matlabCanvas.mpl_connect("key_press_event", self.on_key_press)

        # testKnob = Knob(self)
        # testKnob.grid(column=2, row=3)

    # def on_key_press(self, event):
    #     print("you pressed {}".format(event.key))
    # #     key_press_handler(event, self.inputCanvas, self.outputCanvas)


    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()  # this is necessary on Windows to prevent

    def about(self):
        tk.messagebox.showinfo('Sythenix', 'A GUI for modifying audio signals.')

if __name__ == "__main__":

    app = App() 
    app.mainloop()


######################################################## Sound Visualizer Code ################################################################

"""

q = queue.Queue()


def audio_callback(indata, frames, time, status):

    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::10, mapping])


def update_plot(frame):

    global plotdata
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])
    return lines


    
device_info = sd.query_devices(3, 'input')
samplerate = device_info['default_samplerate']
length = int(200 * samplerate / (1000 * 10))
plotdata = np.zeros((length, 1))
fig, ax = plt.subplots()
lines = ax.plot(plotdata)

ax.axis((0, len(plotdata), -1, 1))
ax.set_yticks([0])
ax.yaxis.grid(True)
ax.tick_params(bottom=False, top=False, labelbottom=False,
               right=False, left=False, labelleft=False)
fig.tight_layout(pad=0)

stream = sd.InputStream(
    device=3, channels=1,
    samplerate=samplerate, callback=audio_callback)
ani = FuncAnimation(fig, update_plot, interval=30, blit=True)

with stream:
    plt.show()

"""