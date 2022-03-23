import tkinter as tk

class Knob(tk.Frame):
    def __init__(self, parent=None, high=1, low=0, text=""):
        tk.Frame.__init__(self, parent)
        self.isDiscrete = False
        self.high = high
        self.low = low
        self.currentValue = low
        self.text = tk.Label(self)

        self.canvas = tk.Canvas(self)
        

        self.drawButton()

    def drawButton(self):
        self.canvas.create_oval(100,60,180,140,fill="red")
        self.canvas.configure(bg="cyan")
        


    

