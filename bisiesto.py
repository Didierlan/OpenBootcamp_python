def bisiesto(anno):
    if anno >=1582:
        #esto se pued modificar por lo que puese
        #total = (anno-1582)
        #if(total%4 == 2):
        if anno%4 == 0:
            return "Es un año bisiesto"
        else:
            return "no es un año bisiesto"


print(bisiesto(2096))



