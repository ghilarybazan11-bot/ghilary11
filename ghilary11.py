
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollectio
def crear_estrella():
  print("haciendo una estrella")

  def crear_triangulo():
    print("haciendo un triangulo")
  x = [0, 1, 0.5, 0] 
  y = [0, 0, 1, 0]
  plt.figure()
  # Dibujar el triángulo
  plt.plot(x, y, marker='o') # 'marker' es opcional para ver los vértices
  # Rellenar el triángulo (opcional)
  plt.fill(x, y, 'b', alpha=0.3) # 'b' es azul, alpha es transparencia
  plt.title("Triángulo en Matplotlib")
  plt.grid(True)
  plt.show()
  def crear_circulo():
    print("haciendo un circulo")
  fig, ax = plt.subplots()
  # Crear círculo: Circle((x, y), radio, ...)
  circulo = Circle((0.5, 0.5), 0.2, color='blue', fill=False)
  # Añadir el círculo a los ejes
  ax.add_patch(circulo)
  # Configurar aspecto igual y límites
  ax.set_aspect('equal')
  ax.set_xlim(0, 1)
  ax.set_ylim(0, 1)
  plt.show(block=False)
  def crear_rectangulo():
    print("haciendo un rectangulo")
  # Crear figura
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
   # Definir dimensiones del rectángulo
  x = [0, 5, 5, 0, 0]
  y = [0, 0, 3, 3, 0]
  z = [0, 0, 0, 0, 0] # Cara inferior
  # Graficar la cara base (plana, se puede extruir)
  ax.plot_trisurf(x, y, z, color='blue', alpha=0.5)
  # Añadir etiquetas
  ax.set_xlabel('Eje X')
  ax.set_ylabel('Eje Y')
  ax.set_zlabel('Eje Z')
  plt.show()
def menu():
  print("menu de figuras geometricas")
  print ("crea un increible circulo")
  print("seleccionar una figura")
  print("1. estrella")
  print("2 cuadrado")
  print("3 triangulo")
  print("4 circulo")
  print("5 rectangulo")
  print("6 salir")
while True:
  menu()
  try:
    opcion = int(input("ingrese un numero de la figura que debe realizar"))
    print(opcion)
    match opcion:
      case 1:
        crear_estrella()
      case 2:
        crear_cuadrado()
      case 3:
        crear_triangulo()
      case 4:
        crear_circulo()
      case 5:
        crear_rectangulo()
      case 6:
        print("saliendo")
        break
      case _:
        print("opcion no valida")
  except ValueError:
    print("entrada invalida") 
    break # 0 continuar, segun desees 




 