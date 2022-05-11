class Sorter:

    @staticmethod
    def bubbleSort(list):
        for i in range(len(list) - 1):
            for j in range(len(list) - i - 1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
                yield (list)

    @staticmethod
    def selectionSort(list):
        for iterator in range(len(list)):
            minimum = iterator
            for current in range(iterator, len(list)):
                if list[minimum] > list[current]:
                    minimum = current

            list[iterator], list[minimum] = list[minimum], list[iterator]
            yield list

    @staticmethod
    def insertionSort(list):
        for iterator in range(1, len(list)):
            key = list[iterator]
            j = iterator
            while list[j-1] > key and j >= 1:
                list[j] = list[j-1]
                j -= 1

            list[j] = key
            yield list
