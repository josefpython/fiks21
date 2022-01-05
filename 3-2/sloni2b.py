from copy import deepcopy

class Playground:

    def __init__(self, xbounds, ybounds):
        
        #Create an array keeping track of all the elephants ingame
        self.elephants = []
        self.mapSize = [xbounds,ybounds]

        #Create a 2d array x*y
        self.map = []
    
    def addElephant(self,x,y):

        #Adds an elephant to given coords

        if x < 0 or y < 0:
            raise IndexError

        if [x,y] not in self.elephants:
            self.elephants.append([x,y])

    def killElephant(self, x,y):

        #Murder elephant at given coords
        self.elephants.remove([x,y])

    def moveElephant(self,count):
        for i in range(count):   
            for elephant in deepcopy(self.elephants):
                x,y = elephant
                self.killElephant(x,y)
                #Try to create 4 new elephants, up down left right
                try:
                    self.addElephant(x,y+1)
                except IndexError:
                    pass
                try:
                    self.addElephant(x,y-1)
                except IndexError:
                    pass
                try:
                    self.addElephant(x+1,y)
                except IndexError:
                    pass
                try:
                    self.addElephant(x-1,y)
                except IndexError:
                    pass

    def countElephants(self):
        return len(self.elephants)

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        raw = f.read().split("\n")

        zadaniArr = raw[1:]


        for zadani in zadaniArr:

            W, H, X, Y, T = [int(i) for i in zadani.split(" ")]

            gaming = Playground(W,H)
            gaming.addElephant(X,Y)

            gaming.moveElephant(T)

            with open("output.txt", "a") as nf:
                print(gaming.countElephants())
                nf.write(str(gaming.countElephants()) + "\n")