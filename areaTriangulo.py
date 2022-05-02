import math

def areaTriangulo(altura, base):
    return (base*altura)/2
    
print('El area del triangulo es:',areaTriangulo(2,4))

#---------------------------------------------------------------------#

def areaCirculo(radio):
    return round(math.pi*(radio**2),3)
    
print('El area del circulo es:',areaCirculo(6))