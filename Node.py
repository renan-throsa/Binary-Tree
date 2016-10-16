#classe Node
class Node():
    def __init__(self,digimon):
        self.obj = digimon
        self.esquerda = None  #left child
        self.direita = None     #right child

    def getEsquerda(self):
        return self.esquerda

    def setEsquerda(self,no):
        self.esquerda = no

    def getDireita(self):
        return self.direita

    def setDireita(self,no):
        self.direita = no

    def ehfolha(self):
        if self.getEsquerda() is None and self.getDireita() is None:
            return True
        else:
            return False
    def __str__(self):
        return ("%i %s"%(self.obj.xp,self.obj.nome))
