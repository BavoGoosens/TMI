from tkinter import *
from Position import *
from Circle import *
import fileinput

class GUI(object):
    """description of class"""

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.canvas = Canvas(frame)
        self.canvas.pack(side= LEFT)
        self.entry = Entry(frame)
        self.entry.pack(side=LEFT) 
        self.button = Button(frame, name="go", text="GO", fg="red", command=self.process(self.entry.get))
        self.button.pack(side=RIGHT) 
        
      

    def process(self,path):
        count = 0
        cirkels = []
        for line in fileinput.input(files = ('c:/Users/Bavo/Dropbox/Projecten/TMI 1/testfile1.txt')):
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


