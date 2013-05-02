from tkinter import *
from Position import *
from Circle import *
import fileinput

class GUI(object):
    """description of class"""

    def __init__(self,master):
        frame = Frame(master,width=500, height=500)
        frame.pack()
        self.entry = Entry(frame)
        self.entry.bind("<return>", self.process())
        self.entry.pack() 
        self.canvas = Canvas(frame)
        self.canvas.pack()
        
    

    def process(self):
        path = self.entry.get()
        count = 0
        cirkels = []
        if len(path) > 4 :
            for line in fileinput.input(files = (path)):
                if count == 0:
                     algo = line[0]
                else:
                    if len(line) > 2:
                        cir = line.split( ' ' , 2)
                        pos = Position( float(cir[0]), float(cir[1]))
                        cir = Circle( pos , float(cir [2]))
                        print(cir.to_string())
                        cirkels.append(cir)
            count = count + 1 


