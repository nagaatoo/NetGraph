__author__ = 'nagatoo'

import State, Work, FullPath, Optimizition, sys

# Класс сетевого графика

class NetGraph():
    def __init__(self, StateCount):  # StateCount - count состояний
        self.States = []  # Состояния сетевого графика
        self.Works = []  # Работы с.г.
        self.FullPaths = []  # Полные пути
        self.CriticalPathTime = None  # Время кр. пути
        self.CriticalPathNumb = None  # Номер кр. пути
        self.ShortedPathTime = None  # Время кратчайшего пути
        for i in range(StateCount):
            self.States.append(State.State(len(self.States)))



    #Новая работа
    def addWork(self, BeginStNum, EndStNum, HumanCount, WorkSize, Productivity):
        NewWork = Work.Work(len(self.Works), self.States[BeginStNum], self.States[EndStNum], HumanCount, WorkSize, Productivity)
        self.States[BeginStNum].appendOWork(NewWork)
        self.States[EndStNum].appendIWork(NewWork)
        self.Works.append(NewWork)



    #Передать номер работы между состояниями
    def getWorkNum(self, BeginState, EndState):
        for i in range(self.States[BeginState].getOutputWorkCount()):
            for j in range(self.States[EndState].getInputWorkCount()):
                if self.States[BeginState].getOutputWork(i) == self.States[EndState].getInputWork(j):
                    return self.States[BeginState].getOutputWork(i).getWorkNum()

        return -1



    #Определить полные пути сетевого гр
    def defineFullPath(self):
        def defineFullPathRec(self, NowState, Buff):
            if NowState.getInputWorkCount() == 0:
                self.FullPaths.append(FullPath.FullPath())

            if NowState.getOutputWorkCount() == 0:
                for i in range(len(Buff)):
                    self.FullPaths[len(self.FullPaths)-1].appendState(Buff[i])
                self.FullPaths.append(FullPath.FullPath())

            for i in range(NowState.getOutputWorkCount()):
                NewBuffer = []
                for ij in range(len(Buff) - 1):
                    NewBuffer.append(Buff[ij])
                NewBuffer.append(NowState.getStateNum())
                NewBuffer.append(len(self.States) - 1)
                defineFullPathRec(self, NowState.getOutputWork(i).getEndState(), NewBuffer)

        defineFullPathRec(self, self.States[0], [])

        #Расчет времени путей
        for i in range(len(self.FullPaths) - 1):
            Buff = 0
            for j in range(self.FullPaths[i].getStatesFullPathCount() - 1):
                Buff += self.Works[self.getWorkNum(self.FullPaths[i].getNumbState(j), self.FullPaths[i].getNumbState(j + 1))].getTimeWork()
            self.FullPaths[i].setTimePath(Buff)

        #Определение номера и времени крит. пути
        self.CriticalPathTime = 0
        self.CriticalPathNumb = 0
        for i in range(len(self.FullPaths)):
            if self.FullPaths[i].getTimePath() >= self.CriticalPathTime:
                self.CriticalPathTime = self.FullPaths[i].getTimePath()
                self.CriticalPathNumb = i


        #Определение времени кратчайшего пути
        self.ShortedPathTime = self.FullPaths[0].getTimePath()
        for i in range(1, len(self.FullPaths) - 1):
            if self.FullPaths[i].getTimePath() == 0:
                break
            if self.FullPaths[i].getTimePath() <= self.ShortedPathTime:
                self.ShortedPathTime = self.FullPaths[i].getTimePath()




    #Вывод на экран полных путей сетевого графика!!!
    def returnFullPath(self):
        if self.FullPaths == []:
           print("Нету полных путей")
           return
        else:
            print("Полные пути:  ")
            for i in range(len(self.FullPaths)):
                if i > 4:
                    break
                if i != len(self.FullPaths) - 1:
                    print("Путь - ", i + 1, "; t = ", round(self.FullPaths[i].getTimePath(), 2))

                for j in range(self.FullPaths[i].getStatesFullPathCount()):
                    print("  ", self.FullPaths[i].getNumbState(j), " ")
                  #  if j != range(self.FullPaths[i].getStatesFullPathCount() - 1):
                   #     fp.append("\033[1m -> \033[0m")

            if self.CriticalPathNumb > 4:
                print("Критический",  self.CriticalPathNumb - 41, "-й путь, Время - ",  round(self.CriticalPathTime, 2))
            else:
                print("Критический",  self.CriticalPathNumb + 1, "-й путь, Время - ",  round(self.CriticalPathTime, 2))



    #Определение параметров событий сетевого графика
    def defineStatePar(self):
        #Рекурсивное определение ранних сроков свершения событий
        def defineEarlyPeriodStateRec(NowState):
            if NowState.getInputWorkCount() == 0:
                NowState.setEarlyPeriod(0)

            MaxValue = 0
            for i in range(NowState.getInputWorkCount()):
                if MaxValue <= NowState.getInputWork(i).getBeginState().getEarlyPeriod() + NowState.getInputWork(i).getTimeWork():
                    MaxValue = NowState.getInputWork(i).getBeginState().getEarlyPeriod() + NowState.getInputWork(i).getTimeWork()

            NowState.setEarlyPeriod(MaxValue)
            for i in range(NowState.getOutputWorkCount()):
                defineEarlyPeriodStateRec(NowState.getOutputWork(i).getEndState())

        # Рекурсивное определение поздних сроков свершения событий
        def defineLaterPeriodStatesRec(NowState):
            if NowState.getOutputWorkCount() == 0:
                NowState.setLaterPeriod(self.CriticalPathTime)
                return

            for i in range(NowState.getOutputWorkCount()):
                defineLaterPeriodStatesRec(NowState.getOutputWork(i).getEndState())

            MinValue = NowState.getOutputWork(0).getEndState().getLaterPeriod() - NowState.getOutputWork(0).getTimeWork()
            for i in range(NowState.getOutputWorkCount()):
                if MinValue >= NowState.getOutputWork(i).getEndState().getLaterPeriod() - NowState.getOutputWork(i).getTimeWork():
                    MinValue = NowState.getOutputWork(i).getEndState().getLaterPeriod() - NowState.getOutputWork(i).getTimeWork()

            NowState.setLaterPeriod(MinValue)

        defineEarlyPeriodStateRec(self.States[0])
        defineLaterPeriodStatesRec(self.States[0])



    # Вывод на экран параметров событий сетевого графика
    def printParameters(self):
        print("Параметры событий Сет. графика:")
        for i in range(len(self.States)):
            print("Событие ", self.States[i].getStateNum(), ":  Ранний срок - ", round(self.States[i].getEarlyPeriod(), 2), "  Поздний срок - ", round(self.States[i].getLaterPeriod(), 2), " Резерв события - ", round(self.States[i].getReserve(),2))




    # Определение параметров работ сетевого графика!!
    def defineWorkPar(self):
        for i in range(len(self.Works)):
            self.Works[i].setFreeReserve(self.Works[i].getEndState().getEarlyPeriod() - self.Works[i].getBeginState().getLaterPeriod() - self.Works[i].getTimeWork())
            self.Works[i].setFullReserve(self.Works[i].getEndState().getLaterPeriod() - self.Works[i].getBeginState().getEarlyPeriod() - self.Works[i].getTimeWork())




    # Вывод на экран параметров работ сетевого графика
    def printWorkPar(self):
        print("Парамеры работ сетевого графика:")
        for i in range(len(self.Works)):
            print("Работа ", self.Works[i].getWorkNum() + 1, " :   Объем работ - ", self.Works[i].getWorkSize(), ",   Исполнителей - ", self.Works[i].getHumansCount(), ",  Производительность - ",self.Works[i].getProductivity() , ",   Время работы - ", round(self.Works[i].getTimeWork(), 2), ",  Свободный резерв - ",  round(self.Works[i].getFreeReserve(), 2), ",   Полный резерв - ", round(self.Works[i].getFullReserve(), 2))



    # Выдает суммарный совободный резерв сетевого графика
    def getSummFreeRes(self):
        Buff = 0
        for i in range(len(self.Works)):
            Buff += self.Works[i].getFreeReserve()
        return Buff



    # Перевод исполнителей с одной работы на другую
    def transWorker(self, WorkerCount, OldWorkerNum, NewWorkerNum):
        self.Works[OldWorkerNum].setHumansCount(self.Works[OldWorkerNum].getHumansCount() - WorkerCount)
        self.Works[NewWorkerNum].setHumansCount(self.Works[NewWorkerNum].getHumansCount() + WorkerCount)




    # Оптимизация сетевого графика
    def optimizitionGraph(self):
        optiIteration = []  # Итерации оптимизации сетевого графика
        MaxFreeResNumb = 0  # Значение номера работы с максимальным свободным резервом
        MaxWorkSize = 0  # Значение номера работы с максимальным временем выполнения на критическом пути
        FirstCryPathTime = self.CriticalPathTime  # Время крит пути
        FirstIntensity = round(self.ShortedPathTime, 2) / round(self.CriticalPathTime, 2)  # Напряженность исходного
        FirstSummFreeRes = self.getSummFreeRes()
        Count = -1

        while True:
            # Определение номера работы с максимальным свободным резервом и наличием более 1 работника
            MaxFreeReserv = self.Works[0].getFreeReserve()
            for i in range(1, len(self.Works)):
                if MaxFreeReserv <= self.Works[i].getFreeReserve() and self.Works[i].getHumansCount() > 1:
                    MaxFreeReserv = self.Works[i].getFreeReserve()
                    MaxFreeResNumb = i

            # Определение номера работы с максимальным временем выполнения на критическом пути
            MaxWorkSizeValue = self.Works[self.getWorkNum(self.FullPaths[self.CriticalPathNumb].getNumbState(0), self.FullPaths[self.CriticalPathNumb].getNumbState(1))].getTimeWork()
            MaxWorkSize = self.Works[self.getWorkNum(self.FullPaths[self.CriticalPathNumb].getNumbState(0), self.FullPaths[self.CriticalPathNumb].getNumbState(1))].getWorkNum()
            for i in range(1, self.FullPaths[self.CriticalPathNumb].getStatesFullPathCount() - 1):
                if self.Works[self.getWorkNum(self.FullPaths[self.CriticalPathNumb].getNumbState(i), self.FullPaths[self.CriticalPathNumb].getNumbState(i + 1))].getTimeWork() >= MaxWorkSizeValue:
                    MaxWorkSizeValue = self.Works[self.getWorkNum(self.FullPaths[self.CriticalPathNumb].getNumbState(i), self.FullPaths[self.CriticalPathNumb].getNumbState(i + 1))].getTimeWork()
                    MaxWorkSize = self.Works[self.getWorkNum(self.FullPaths[self.CriticalPathNumb].getNumbState(i), self.FullPaths[self.CriticalPathNumb].getNumbState(i + 1))].getWorkNum()

            # выполнение итерации
            self.transWorker(1, MaxFreeResNumb, MaxWorkSize)# перепутаны в параметров.

            self.defineFullPath()#!!!
            self.defineStatePar()
            self.defineWorkPar()

            # сохраненеие итерации c увеличением счетчика
            Count += 1
            optiIteration.append(Optimizition.Optimizition(1, MaxFreeResNumb, MaxWorkSize))
            optiIteration[Count].setCritPathTime(self.CriticalPathTime)
            optiIteration[Count].setIntensity(self.ShortedPathTime/self.CriticalPathTime)
            optiIteration[Count].setSumFreeReserve(self.getSummFreeRes())

            if len(optiIteration) > 3 and optiIteration[Count - 2].getCriticPathTime() == optiIteration[Count].getCriticPathTime() and optiIteration[Count - 2].getIntesity() == optiIteration[Count].getIntesity() and optiIteration[Count - 2].getSumFreeReserve() == optiIteration[Count].getSumFreeReserve():
                break

            if not (len(optiIteration) == 1 or optiIteration[Count].getCriticPathTime() < optiIteration[Count].getCriticPathTime() or optiIteration[Count].getIntesity() > optiIteration[Count - 1].getIntesity() or optiIteration[Count].getSumFreeReserve() < optiIteration[Count - 1].getSumFreeReserve()):
                break

        print("Оптимизация графика : Время крит. пути - ", round(FirstCryPathTime,2),  " Напряженность - ", round(FirstIntensity,2), "Суммарный свободный резерв - ", round(FirstSummFreeRes, 2))
        MinCryPathTimeNumb = 0
        for i in range(len(optiIteration)):
            print(" Итерация № ", i+1, "   Время критического пути - ", round(optiIteration[i].getCriticPathTime(), 2), "  Коффициент напряженности - ",  round(optiIteration[i].getIntesity(), 2), " Суммарный свободный резерв - ", round(optiIteration[i].getSumFreeReserve(), 2))

        MinCryPathTime = optiIteration[0].getCriticPathTime()
        for i in range(len(optiIteration) - 1):
            if optiIteration[i].getCriticPathTime() <= MinCryPathTime:
                MinCryPathTime = optiIteration[i].getCriticPathTime()
                MinCryPathTimeNumb = i

        i = len(optiIteration) - 1
        while i >= MinCryPathTimeNumb + 1:
            self.transWorker(1, optiIteration[i].getNewWorkNumber(), optiIteration[i].getOldWorkNumb())
            i -= 1

        self.defineFullPath()
        self.defineStatePar()
        self.defineWorkPar()

        if len(optiIteration) > 3 and optiIteration[Count - 2].getCriticPathTime() == optiIteration[Count].getCriticPathTime() and optiIteration[Count - 2].getIntesity() == optiIteration[Count].getIntesity() and optiIteration[Count - 2].getSumFreeReserve() == optiIteration[Count].getSumFreeReserve():
            print("Оптимизация  завершена: зацикливание на № ", len(optiIteration))
        else:
            print("Оптимизация завершена: результат итерации № ", len(optiIteration), " соответствует оптимальности")

        print("Оптимальный результат достигнут: № ", MinCryPathTimeNumb + 1, "\nЗначения критериев оптимальности графа: \nВремя крит. пути -  ", round(self.CriticalPathTime, 2), " \n Напряженность - ", round(self.ShortedPathTime/self.CriticalPathTime, 2), "\nСуммарный всободный резерв - ", round(self.getSummFreeRes(), 2))


