class Punto2:
    def __init__(self,x,y):
        self.__x = self.setX(x)
        self.__y = self.setY(y)


    def setX(self,x):
        if type(x) == int or type(x) == float:
            if x >= 0:
                self.__x = x
            else:
                self.__x = 0
        else:
            self.__x = x


    def setY(self,y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__x = y
            else:
                self.__x = 0
        else:
            self.__x = y


    def getX(self):
        return self.__x


    def getY(self):
        return self.__y

    def toString(self):
        cadeaPunto = "As coordenadas do punto son: \n\t x ="+ str(self.__x) + " \n\t y ="+ str(self.__y) # defino variable, collo string e o concateno co valor de x convertido string e o concateno con outra cadea + o valor de y unido al otro string.
        return cadeaPunto


    def __str__(self):
        return self.toString()

    def __eq__(self, otro):
        return self.__x == otro.x and self.__y == otro.y

    x = property(getX, setX)
    y = property(getY, setY)