import pygame
from sorter import Sorter
import random


pygame.init()


class Screen():
    def __init__(self, algorithm, speed, size):

        # Window Settings
        self.height = 600
        self.width = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Sorting Visualliser')

        # Bar settings
        self.screenMargin = 50
        self.barShowingSpaceWidth = self.width - 2 * self.screenMargin
        self.barShowingSpaceHeight = self.height - 2 * self.screenMargin
        self.spacesBetweenBars = 3
        self.speed = speed

        # Pygame functioning settings
        self.isRunning = True
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # List and iterators
        self.sortingTenchnique = algorithm
        self.originalList = list(range(1, size+1))
        random.shuffle(self.originalList)
        self.currentList = self.originalList
        self.listIterator = iter(self.sortingTenchnique(self.currentList))

        self.numberOfBars = len(self.originalList)
        self.numberOfSpaces = self.numberOfBars - 1
        self.widthBarsRequired = self.barShowingSpaceWidth - \
            self.numberOfSpaces*self.spacesBetweenBars
        self.widthOfBar = int(self.widthBarsRequired / self.numberOfBars)

        self.rectangles = self.__setBarsRectangles()
        self.currentRectangles = self.rectangles

        self.__windowLoop()

    def __windowLoop(self):
        while self.isRunning:
            self.__handleEvents()

            # Checking positions of rectangle are right
            if self.rectangles == self.currentRectangles:
                self.__updateCurrentList()
            else:
                self.__updateRectanglesPositions()
            self.__updateWindow()

            self.clock.tick(self.FPS)

        # Helps in quitting the window
        if not self.isRunning:
            pygame.display.quit()

    def __handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

    def __updateWindow(self):
        self.window.fill((0, 0, 0))
        for id, rectangle in self.currentRectangles.items():
            pygame.draw.rect(self.window, (255, 0, 0), rectangle, 5)
        pygame.display.update()

    def __setBarsRectangles(self):
        maximumOfList = max(self.originalList)
        rectangles = {}

        for index, element in enumerate(self.currentList):
            leftOfBar = self.screenMargin + index*self.widthOfBar + \
                (index) * self.spacesBetweenBars

            heightOfBar = (self.barShowingSpaceHeight /
                           maximumOfList) * element
            topOfBar = self.height - self.screenMargin - heightOfBar

            rectangle = [leftOfBar, topOfBar, self.widthOfBar, heightOfBar]

            rectangles[element] = rectangle
        return rectangles

    def __updateCurrentList(self):
        newList = next(self.listIterator, None)
        if newList != None:
            self.currentList = newList
            self.rectangles = self.__setBarsRectangles()

    def __updateRectanglesPositions(self):
        for index in self.rectangles.keys():
            currentRectanglePosition = self.currentRectangles[index]
            rectanglePosition = self.rectangles[index]

            if currentRectanglePosition[0] == rectanglePosition[0]:
                continue

            else:
                # Getting direction of rectangle
                direction = (rectanglePosition[0] - currentRectanglePosition[0]) / abs(
                    rectanglePosition[0] - currentRectanglePosition[0])

                # Updating rectangle position
                currentRectanglePosition[0] += direction * self.speed

                # Checking is rectangle crossed its desired position
                if direction == -1:
                    if rectanglePosition[0] > currentRectanglePosition[0]:
                        currentRectanglePosition[0] = rectanglePosition[0]
                else:
                    if rectanglePosition[0] < currentRectanglePosition[0]:
                        currentRectanglePosition[0] = rectanglePosition[0]
