from tkinter import *
from Position import *
from Circle import *
from Solver import *
import fileinput
import matplotlib.pyplot as plt


class GUI(object):
    """description of class"""

    def __init__(self,master):
        # aanmaak list voor de ingelezen cirkels
        self.cirkels = []

        # de parent van deze GUI = root
        self.master = master

        # bottom en top frames om zo de layout wat te verbeteren
        top = Frame(master)
        bottom = Frame(master)
        top.pack(side=TOP)
        bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
        
        # buttons 
        self.buttontext = StringVar()
        self.buttontext.set("Start")
        self.startbutton = Button(self.master, textvariable=self.buttontext, command=self.clicked1)
        self.buttontext1 = StringVar()
        self.buttontext1.set("Browse")
        self.browsebutton = Button(self.master, textvariable=self.buttontext1)
        self.startbutton.pack(in_= top, side = LEFT)
        self.browsebutton.pack(in_=top, side = LEFT)

        self.inputframe = Frame(master,width=500, height=500)
        self.inputframe.pack()
        self.entrytext = StringVar()
        self.entry = Entry(self.inputframe, textvariable=self.entrytext, width = 50).pack()
        self.canvas = Canvas(self.inputframe)
        self.canvas.pack()


        
    

    def process(self,path):
        count = 0
        path = path.replace("\"", "")
        algo = 1
        for line in fileinput.input(files = (path)):
            if count == 0:
                 algo = int(line[0])
            else:
                if len(line) > 2:
                    cir = line.split( ' ' , 2)
                    pos = Position( float(cir[0]), float(cir[1]))
                    cir = Circle( pos , float(cir [2]))
                    self.cirkels.append(cir)
            count = count + 1 
        self.solver = Solver(algo, self.cirkels)
        self.intersections = self.solver.find_intersect()

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


