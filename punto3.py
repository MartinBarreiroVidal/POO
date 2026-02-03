class Punto3:
    def __init__(self,x,y):
        self.setX(x)
        self.setY(y)

    def setX(self,x):
        if type(x) == int or type(x) == float:
            if x > 0:
                self.__x = x
            else:
                self.__x = 0
        else:
            raise TypeError("O tipo da coordenada x ten que ser un int o float")

    def setY(self,y):
        if type(y) == int or type(y) == float:
            if y > 0:
                self.__y = y
            else:
                raise TypeError(f"O valor de y={y} ten que ser un int o float")




class Punto4:
    def __init__(self,x,y):
        self.x(x)
        self.setY(y)

    def setX(self,x):
        if type(x) == int or type(x) == float:
            if x > 0:
                self.__x = x
            else:
                self.__x = 0
        else:
            raise TypeError("O tipo da coordenada x ten que ser un int o float")

    def setY(self,y):
        if type(y) == int or type(y) == float:
            if y > 0:
                self.__y = y
            else:
                raise TypeError(f"O valor de y={y} ten que ser un int o float")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if type(x) == int or type(x) == float:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError(f"O valor de x={x} non pertence ao primeiro cuadrante")
        else:
            raise TypeError ("O valor de x ten que ser un int o float")

    def y(self,y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError(f"O valor de x={y} non pertence ao primeiro cuadrante")
        else:
            raise TypeError ("O valor de x ten que ser un int o float")

