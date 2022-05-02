from abc import ABC,abstractmethod

class Animal(ABC):
    #aca estoy poniendo el metodo sonido como abstracto
    @abstractmethod
    def sonido(self):
        pass

    @abstractmethod
    def ladra(self):
        pass


class Perro(Animal):
    def __init__(self):
        print("Hola soy un perro")
        
    def sonido(self):
       print("Guau,Guau ")

    def ladra(self):
        print("True")


class Gato(Animal):
    def __init__(self):
        print("Hola soy un gatico")
        
    def sonido(self):
       print("Miau, Miau")


    def ladra(self):
        print("False")




perrito = Perro()
perrito.sonido()
perrito.ladra()

gatico = Gato()
gatico.sonido()
gatico.ladra()