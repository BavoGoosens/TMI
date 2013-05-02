from tkinter import *
from Position import *
from Circle import *
import fileinput

class GUI(object):
    """description of class"""

    def __init__(self,master):
        self.cirkels = []
        frame = Frame(master,width=500, height=500)
        frame.pack()
        self.master = master
        self.entrytext = StringVar()
        self.entry = Entry(master, textvariable=self.entrytext, width = 50).pack()
        self.buttontext = StringVar()
        self.buttontext.set("Start")
        Button(master, textvariable=self.buttontext, command=self.clicked1).pack()
        self.canvas = Canvas(frame)
        self.canvas.pack()
        self.labeltext = StringVar()
        self.label = Label(frame, text = self.labeltext).pack()


        
    

    def process(self,path):
        count = 0
        for line in fileinput.input(files = (path)):
            if count == 0:
                 algo = line[0]
            else:
                if len(line) > 2:
                    cir = line.split( ' ' , 2)
                    pos = Position( float(cir[0]), float(cir[1]))
                    cir = Circle( pos , float(cir [2]))
                    self.cirkels.append(cir)
            count = count + 1 

    def clicked1(self):
        input = self.entrytext.get()
        self.process(input)
        for circle in self.cirkels:
            self.labeltext.set(self.labeltext.get() +"\n" + circle.to_string())

        self.master.update_idletasks()

        

    def button_click(self, e):
        pass


