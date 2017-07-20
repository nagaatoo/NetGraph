__author__ = 'nagatoo'

import NetGraph

var17 = NetGraph.NetGraph(8)
Productivity = 2
var17.addWork(0, 1, 15, 100, Productivity)
var17.addWork(1, 3, 18, 29, Productivity)
var17.addWork(3, 7, 23, 40, Productivity)
var17.addWork(0, 2, 15, 80, Productivity)
var17.addWork(2, 5, 32, 120, Productivity)
var17.addWork(5, 6, 25, 6, Productivity)
var17.addWork(6, 7, 35, 7, Productivity)
var17.addWork(1, 2, 50, 23, Productivity)
var17.addWork(1, 5, 7, 30, Productivity)
var17.addWork(3, 4, 25, 14, Productivity)
var17.addWork(4, 5, 20, 50, Productivity)

#Полные пути
var17.defineFullPath()
var17.returnFullPath()

#Параметры событий
var17.defineStatePar()
var17.printParameters()


#параметры работ
var17.defineWorkPar()
var17.printWorkPar()


#Оптимизация
var17.optimizitionGraph()


#Полные пути
var17.defineFullPath()
var17.returnFullPath()

#Параметры событий
var17.defineStatePar()
var17.printParameters()


#параметры работ
var17.defineWorkPar()
var17.printWorkPar()