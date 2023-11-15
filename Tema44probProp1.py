class Cuadrado:

  def __init__(self,lado):
    self.lado=lado

  def mostrar_perimetro(self):
    perimetro=self.lado*4
    print("El perimetro del cuadro es",perimetro)

  def mostrar_superficie(self):
    superficie=self.lado*self.lado
    print("La superficie del cuadro es", superficie)

#Bloque principal
cuadrado1=Cuadrado(50)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
