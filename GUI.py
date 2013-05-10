from tkinter import *
from Position import *
from Circle import *
import fileinput
import matplotlib.pyplot as plt


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


        
    

    def process(self,path):
        count = 0
        path = path.replace("\"", "")
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
        
        var = StringVar()
        var.set('Uw cirkels:')

        l = Label(self.master, textvariable = var)
        l.pack()

        fig = plt.gcf()
        
        for circle in self.cirkels:
            var.set(var.get() +"\n" + circle.to_string())
            fig.gca().add_artist(circle.getPlot())

        plt.show()
        self.master.update_idletasks()

        

    def button_click(self, e):
        pass


