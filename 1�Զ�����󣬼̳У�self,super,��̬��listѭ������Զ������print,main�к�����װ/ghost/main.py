from ag687 import Ag
from ghost import Ghost


def initPR():
    global ghost
    ghost = Ghost("张志华", 50)

def printPR():
    print(ghost.getName(), ghost.getAge())

def initAG():
    global list, ghost
    list = []
    for i in range(5):
        ghost = Ag("梁冠明" + str(i), i, "E91996")
        list.append(ghost)
        ghost = None

def printAG():
    global ghost
    for ghost in list:
        print(ghost.getAge(), ghost.getName(), ghost.getCar())


initPR()
printPR()
initAG()
printAG()