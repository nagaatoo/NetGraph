__author__ = 'nagatoo'

#Класс состояния в сетевом трафике

class State():
    def __init__(self, StateNum):
        self.StateNum = StateNum  # Порядковый номер сосояния
        self.EarlyPeriod = 0  # Ранний срок свершения события
        self.LaterPeriod = 0  # Поздний срок свершения события
        self.IWorks = []  # Входящие в состояние работы
        self.OWorks = []  # Исходящие из состояния работы


    # Ранний срок свершения события
    def setEarlyPeriod(self, EPeriod):
        self.EarlyPeriod = EPeriod


    # Поздний срок свершения соытия
    def setLaterPeriod(self, LPeriod):
        self.LaterPeriod = LPeriod


    #Резерв события
    def getReserve(self):
        return self.LaterPeriod - self.EarlyPeriod


    #Ранний срок свершения события
    def getEarlyPeriod(self):
        return self.EarlyPeriod


    #Поздний срок свершения состояния
    def getLaterPeriod(self):
        return self.LaterPeriod


    #Порядковый номер
    def getStateNum(self):
        return self.StateNum


    #Количество входящих работ
    def getInputWorkCount(self):
        return len(self.IWorks)


    #Передать входящую работу по индексу
    def getInputWork(self, index):
        return self.IWorks[index]


    #Добавить новую входящую работу
    def appendIWork(self, works):
        self.IWorks.append(works)


    #Передать кол - во исходящих работ
    def getOutputWorkCount(self):
        return len(self.OWorks)


    #Передает исходящую работу по индексу
    def getOutputWork(self, index):
        return self.OWorks[index]


    #Добавляет новую исходящую работу
    def appendOWork(self, works):
        self.OWorks.append(works)