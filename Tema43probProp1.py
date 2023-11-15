class Alumno:

  def inicializar(self,nombre,nota):
    self.nombre=nombre
    self.nota=nota

  def imprimir(self):
    print("Nombre:",self.nombre)
    print("Nota:",self.nota)

  def mostrar_resultado(self):
    if self.nota<=4:
      print("Regular")
    else:
      print("Libre")

#Bloque Principal
alumno1=Alumno()
alumno1.inicializar("Nicolás",10)
alumno1.imprimir()
alumno1.mostrar_resultado()

alumno2=Alumno()
alumno2.inicializar("Lucas",4)
alumno2.imprimir()
alumno2.mostrar_resultado()