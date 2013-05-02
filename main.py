from GUI import *
from tkinter import *

def main():
    root = Tk()
    w = Label(root, text="Enter the path to to input file and hit enter to continue")
    w.pack()
    gui = GUI(root)
    root.title("Bavo and Sander: Circle Processor")
    root.mainloop()
    


if __name__ == "__main__":
    main()





