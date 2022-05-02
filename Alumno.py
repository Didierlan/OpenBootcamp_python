#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.



class Alumno:
    nota = None; 
    def __init__(self, nombre, nota) :
        self.nombre = nombre; 
        self.nota = nota; 

    def _aprobacion (self):
        if self.nota >= 6:
            return f"aprobo la materia con { self.nota}"
        else:
            return f"no aprobo la materia con { self.nota}"

    def mostar(self):
        return f"El alumno {self.nombre} {self._aprobacion()}"

a = Alumno("Pepe", 8)
b = Alumno("Dani", 3)
print(a.mostar())
print(b.mostar())


