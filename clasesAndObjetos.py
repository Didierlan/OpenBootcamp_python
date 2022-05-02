#una clase en python por debajo es un diccionario

class Bombillo:
    _luz = True

    def __init__(self, _luz):
        self._luz = _luz
        print("Hola estoy en la clase Bombillo")
        print("Hay luz", _luz)

    def apagado(self):
        self._luz = False

    def ensendido(self):
        self._luz = True

    def isEnsendido(self):
        return self._luz;
        




class Lampara(Bombillo):
    _cordon = False 
    
    #asi se hace un contructor importante el metodo __init__
    def __init__(self, _cordon):
        #con esto estoy llamdo al contructor de la clase padre
        super().__init__("False")
        self._cordon = _cordon
        print("Estoy en el contructor de Lampara")




    def cordon(self):
        return self._cordon


lampara1 = Lampara("False")

lampara1.ensendido()
print("la lampara esta ensendida",lampara1.isEnsendido())
print(lampara1.cordon())





