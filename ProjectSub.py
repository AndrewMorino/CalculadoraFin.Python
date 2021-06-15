import ProjectMain
import os

inicio = int(input("Qual operação deseja realizar ? "))
if inicio == 1:
    ProjectMain.calculos1()
elif inicio == 2:
    ProjectMain.calculos2()
else:
    ProjectMain.invalido()


