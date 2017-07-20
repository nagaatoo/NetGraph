__author__ = 'nagatoo'


class Optimizition():
    def __init__(self, WorkerCount, OldWorkNum, NewWorkNum):
        self.WorkerCount = WorkerCount
        self.OldWorkNum = OldWorkNum
        self.NewWorkNum = NewWorkNum
        self.Intensity = 0
        self.CriticPathTime = 0
        self.SumFreeReserve = 0


    def getNewWorkNumber(self):
        return self.NewWorkNum



    def getOldWorkNumb(self):
        return self.OldWorkNum



    def getIntesity(self):
        return self.Intensity



    def  getCriticPathTime(self):
        return self.CriticPathTime



    def getSumFreeReserve(self):
        return self.SumFreeReserve



    def setIntensity(self, intensity):
        self.Intensity = intensity


    def setCritPathTime(self, time):
        self.CriticPathTime = time


    def setSumFreeReserve(self, sumfree):
        self.SumFreeReserve = sumfree
