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
        self.top = Frame(master, bd=1,relief=SUNKEN,padx=1,pady=1)
        self.bottom = Frame(master, bd=1,relief=SUNKEN,padx=1,pady=1)
        self.top.pack(side=TOP,fill=BOTH, expand=True)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

        # top in nog meer frames opdelen links en rechts
        self.leftTOP = Frame(self.top, bd=1,relief=SUNKEN,padx=1,pady=1)
        self.rightTOP = Frame(self.top, bd=1,relief=SUNKEN,padx=1,pady=1)
        self.leftTOP.pack(side=LEFT,fill=BOTH, expand=True)
        self.rightTOP.pack(side=RIGHT,fill=BOTH, expand=True)

        # uitleg
        w = Label(self.rightTOP, text="Enter the path to to input file in the first field"+"\n" +"Enter the path to the output file in the second field" + "\n" + "push the START button to start")
        w.pack()

        # buttons 
        self.buttontext = StringVar()
        self.buttontext.set("START")
        self.startbutton = Button(master, textvariable=self.buttontext, command=self.clicked1,height = 2)
        
        self.buttontext1 = StringVar()
        self.buttontext1.set("Browse")
        self.browsebutton = Button(master, textvariable=self.buttontext1, height = 1)
        
        self.startbutton.pack(in_= self.rightTOP)
        self.browsebutton.pack(in_= self.leftTOP, side = RIGHT)

        self.inputframe = Frame(master,width=500, height=500, bd=1,relief=SUNKEN,padx=1,pady=1,bg="blue")
        self.inputframe.pack(in_= self.bottom, side = LEFT)
        
        self.outputframe = Frame(master,width=500, height=500, bd=1,relief=SUNKEN,padx=1,pady=1,bg="blue")
        self.outputframe.pack(in_= self.bottom, side = LEFT)

        #entry fields 
        self.entrytext = StringVar()
        self.inputEntry = Entry(master, textvariable=self.entrytext, width = 50).pack(in_= self.leftTOP)

        self.entrytext1 = StringVar()
        self.outputEntry = Entry(master, textvariable=self.entrytext1, width = 50).pack(in_= self.leftTOP)

    def output(self, path):
         print (path)

    def process(self,path):
        count = 0
        path = path.replace("\"", "")
        self.algo = 1
        for line in fileinput.input(files = (path)):
            if count == 0:
                 self.algo = int(line[0])
            else:
                if " " in line:
                    cir = line.split( ' ' , 2)
                    pos = Position( float(cir[0]), float(cir[1]))
                    cir = Circle( pos , float(cir [2]))
                    self.cirkels.append(cir)
            count = count + 1 
        self.solver = Solver(self.algo, self.cirkels)
        self.intersections = self.solver.find_intersect()

    def clicked1(self):

        self.process(self.entrytext.get())
        self.output(self.entrytext1.get())

        self.algoLabel = Label(self.master,text = "Het gebruikte algoritme is: " + str(self.algo))
        self.algoLabel.pack(in_= self.rightTOP)

        self.timeLabel = Label(self.master,text = "Het vinden van de snijpunten nam: " + str(self.intersections[1]) + " in beslag")
        self.timeLabel.pack(in_= self.rightTOP)

        cirkeltext = Text(self.inputframe)
        cirkeltext.insert(END,'Uw Cirkels:')
        cirkeltext.pack()

        fig = plt.gcf()
                
        count = 1
        for circle in self.cirkels:
            cirkeltext.insert(END,"\n" +str(count)+" => "+ circle.to_string())
            fig.gca().add_artist(circle.getPlot())
            count+=1

        intertext = Text(self.outputframe)
        intertext.insert(END,'De Snijpunten:')
        intertext.pack()
        
        count = 1
        for inter in self.intersections[0]:
            intertext.insert(END,"\n" +str(count)+" => "+ inter.to_string())
            count+=1

        plt.show()
        self.master.update_idletasks()

        

    def button_click(self, e):
        pass


