from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula,velocidadeMaxima,autonomia):
        self.__matricula = matricula
        self.__velocidadeMaxima = velocidadeMaxima
        self.__autonomia = autonomia

@property
def matricula(self):
    return self.__matricula

@matricula.setter
def matricula(self):
    return self.__matricula

@property
def velocidadeMaxima(self):
    return self.__velocidadeMaxima


@velocidadeMaxima.setter
def velocidadeMaxima(self):
    return self.__velocidadeMaxima

@property
def autonomia(self):
    return self.__autonomia

@autonomia.setter
def autonomia(self):
    return self.__autonomia

@abstractmethod
def arrincar (self):
    pass

def deter (self):
    print(f"O vehiculo de {self.__matricula} esta detido")