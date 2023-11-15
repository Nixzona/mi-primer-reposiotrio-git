class Persona:

 def inicializar (self,nombre,edad):
    self.nombre=nombre
    self.edad=edad

 def imprimir_info (self):
    print("Nombre:", self.nombre)
    print("Edad: ", self.edad)

 def estado_persona (self):
    if self.edad>=18:
      print ("Es mayor de edad")
    else:
      print ("No es mayor de edad")

#Bloque Principal

Persona1=Persona()
Persona1.inicializar ("Nicolás",18)
Persona1.imprimir_info()
Persona1.estado_persona()