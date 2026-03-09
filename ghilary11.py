import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def crear_estrella():
  print("haciendo una estrella")
def crear_cuadrado():
  print("haciendo un cuadrado")
def crear_triangulo():
  print("haciendo un triangulo")

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
def menu():
  print("menu de figuras geometricas")
  print ("crea un increible circulo")
  print("seleccionar una figura")
  print("1. estrella")
  print("2 cuadrado")
  print("3 triangulo")
  print("4 circulo")
  print("5 salir")
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
        print("saliendo")
        break
      case _:
        print("opcion no valida")
  except ValueError:
    print("entrada invalida") 
    break # 0 continuar, segun desees 




 