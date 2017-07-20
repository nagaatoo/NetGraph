__author__ = 'nagatoo'

# Реализация полного пути в графике

class FullPath():
    def __init__(self):
        self.NumStateFullPath = []  # Номера состояний полного пути
        self.TimePath = 0  # Время полного пути


    #Передать количество cостояний в полном пути
    def getStatesFullPathCount(self):
        return len(self.NumStateFullPath)


    #Передать номер состояния полного пути по индексу
    def getNumbState(self, index):
        return self.NumStateFullPath[index]


    #Добавить новое состояние
    def appendState(self, NumberState):
        self.NumStateFullPath.append(NumberState)


    #Установить время полного пути
    def setTimePath(self, time):
        self.TimePath = time


    #Передать время полного пути
    def getTimePath(self):
        return self.TimePath