__author__ = 'nagatoo'

#Класс работ сетевого графика

class Work():
    def __init__(self, StateNum, BeginState, EndState, HumanCount, WorkSize, Productivity):
        self.StateNum = StateNum  # Порядковый номер работы
        self.BeginState = BeginState  # Начальное состояние
        self.EndState = EndState  # Конечное состояние
        self.HumanCount = HumanCount  # Количество исполнителей
        self.WorkSize = WorkSize  # Объем работ
        self.Productivity = Productivity  # Производительность
        self.FreeReserve = 0  # Свободный резерв
        self.FullReserve = 0  # Полный резерв


    #Передать производительность
    def getProductivity(self):
        return self.Productivity


    #Установить свободный резерв
    def setFreeReserve(self, FreeReserve):
        self.FreeReserve = FreeReserve


    #Установить полный резерв
    def setFullReserve(self, FullReserve):
        self.FullReserve = FullReserve


    #Передать кол - во исполнителей
    def getHumansCount(self):
        return self.HumanCount

    def setHumansCount(self, humans):
        self.HumanCount = humans


    #Передать начальное состояние
    def getBeginState(self):
        return self.BeginState


    #передать конечное состояние
    def getEndState(self):
        return self.EndState


    #Передать объем работ
    def getWorkSize(self):
        return self.WorkSize


    #Передать свободный резерв
    def getFreeReserve(self):
        return self.FreeReserve


    #Передать полный резерв
    def getFullReserve(self):
        return self.FullReserve


    #Передать порядковый номер
    def getWorkNum(self):
        return self.StateNum


    #Передать время выполнения работы
    def getTimeWork(self):
        return self.WorkSize/(self.HumanCount*self.Productivity)
