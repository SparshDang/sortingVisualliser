from tkinter import *
import threading

from sorterVisualliserScreen import Screen
from sorter import Sorter


class ControlWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Sorting Visualiser')
        self.geometry('400x200')
        self.resizable(0, 0)

        self.algorithm = StringVar()
        self.speed = IntVar()
        self.size = IntVar()
        self.algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort']
        self.algorithm.set('Bubble Sort')

        self.__createTitle()
        self.__createDropdown()
        self.__createSpeedBar()
        self.__createNumberBar()
        self.__createButton()

    def __createTitle(self):
        Label(self, text='Sorting Visualliser',
              font=('Arial', 30, 'bold')).pack()

    def __createDropdown(self):
        sortingAlgoFrame = Frame(self)
        sortingAlgoFrame.pack(fill='x')

        Label(sortingAlgoFrame, text='Algorithm', ).pack(side=LEFT)

        dropdown = OptionMenu(
            sortingAlgoFrame, self.algorithm, *self.algorithms)
        dropdown.pack(side=RIGHT, fill='x')

    def __createSpeedBar(self):

        speedFrame = Frame(self)
        speedFrame.pack(fill='x')

        Label(speedFrame, text='Speed', ).pack(side=LEFT)

        slider = Scale(speedFrame, from_=1, to=20,
                       orient=HORIZONTAL, variable=self.speed)
        slider.pack(side=RIGHT, fill='x')

    def __createNumberBar(self):
        sizeFrame = Frame(self)
        sizeFrame.pack(fill='x')

        Label(sizeFrame, text='Number of elements', ).pack(side=LEFT)

        slider = Scale(sizeFrame, from_=4, to=50,
                       orient=HORIZONTAL, variable=self.size)
        slider.pack(side=RIGHT, fill='x')

    def __createButton(self):
        self.startButton = Button(self, text='Start')
        self.startButton.pack()
        self.startButton.bind('<Button-1>', self.__startTheVisualliser)

    def __startTheVisualliser(self, event):
        methodsDictionary = {
            "Bubble Sort": Sorter.bubbleSort,
            "Insertion Sort": Sorter.insertionSort,
            "Selection Sort": Sorter.selectionSort
        }
        algorithm = methodsDictionary[self.algorithm.get()]
        Screen(algorithm, self.speed.get(), self.size.get())


if __name__ == '__main__':
    main = ControlWindow()
    main.mainloop()
