class Persona:

  def inicializar(self,nom):
    self.nombre=nom

  def imprimir(self):
    print("Nombre",self.nombre)

#Bloque Principal

persona1=Persona()
persona1.inicializar("Nicolas")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()