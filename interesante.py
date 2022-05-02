#uso de **kwargs  y *args aunque kwargs y args se pueden remplazar poor cualquier otra palabra
# **kwargs permite pasar argumentos de longitud variable asociados con un nombre o key a una función. Deberías usar **kwargs si quieres manejar argumentos con nombre como entrada a una función.

def sumador(**kwargs):
    inicial = kwargs["inicial"] if 'inicial' in kwargs else 0
    final = kwargs["final"] if 'final' in kwargs else 0
    
    return inicial + final

#inicial y final es el nombre o key asociado al argumento que va a manejar la funcion 
print(sumador(inicial=12, final=2))

