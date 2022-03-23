from tkinter import Frame
from tkinter import Label
from tkinter import Canvas
from tkinter import BOTH


class Knob(Frame):
    def __init__(self, parent, high=1, low=0, text=""):
        super(Knob, self).__init__()

        self.isDiscrete = False
        self.high = high
        self.low = low
        self.currentValue = low
        self.text = text

        self.canvas = Canvas(self)

        self.drawButton()

    def drawButton(self):

        x = self.canvas.winfo_width()/2
        y = self.canvas.winfo_height()/2

        r = 100
        
        self.canvas.create_oval(r/2+5*x,r/2+5*y,r,r,fill="red")
        self.canvas.configure(bg="cyan")
        self.canvas.grid()



