#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

#Color

#Ruedas

#Puertas

#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

#Velocidad

#Cilindrada

#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.





class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    Velocidad = 120
    Cilindrada = 520


coche1 = Coche()
print("El color del coche1 es: ", coche1.color, "tiene", coche1.puertas,"puertas y ", coche1.ruedas,"ruedas su velocidad es de", coche1.Velocidad, "km/h y tiene una cilindrada de", coche1.Cilindrada)


#-------------------------------------------------------------------------#

#Esta es otra forma de hacer elñ ejercicio aunque esta lleva contructores y metodos para su ejecucion 

# inicializamos la clase
class Vehiculo():
    # inicializamos los atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas, self.puertas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        #envio los parametros a la clase padre (Vehiculo())
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def ver(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

# bloque principal
# creamos el nuevo objeto, lo inicializamos y se imprime
coche = Coche("azul", 4, 4, 150, 1200)
print(coche.ver())