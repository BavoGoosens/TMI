from GUI import *
from tkinter import *

def main():
    root = Tk()
    w = Label(root, text="Enter the path to to input file")
    w.pack()
    gui = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()





